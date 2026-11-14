#!/usr/bin/env python3
"""Deterministic and report-only steps of the copy audit contract.

`check` turns audit items (JSONL) into findings: context gaps, the decision
owner of the item's content type, forbidden or legacy labels mapped to approved
terminology labels, a priority and, for content types that allow it, a rewrite
copy brief. `prepare` writes semantic-evaluator tasks for items with full
context. `summarize` aggregates findings, optionally merged with semantic
evaluator responses, into a report. Inventories, findings and reports are
inputs and outputs of the tool; they are not stored in this repository.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tooling.content_rule_index import contracts_by_id  # noqa: E402
from tooling.evals.run_content_semantic_eval import (  # noqa: E402
    EVALUATOR_VERSION,
    EvalError,
    read_jsonl,
    write_jsonl,
)
from tooling.validators.check_copy_briefs import Context, anatomy_roles  # noqa: E402

AUDIT_CONTRACT = ROOT / "foundations" / "content" / "copy-audit.yml"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FINDING_STATUSES = ("finding", "no_issue", "needs_context")


def load_contract() -> dict[str, Any]:
    return yaml.safe_load(AUDIT_CONTRACT.read_text(encoding="utf-8"))


def _labels(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for item in value.values() for s in _labels(item)]
    if isinstance(value, list):
        return [s for item in value for s in _labels(item.get("label") if isinstance(item, dict) else item)]
    return []


def validate_item(item: Any, contract: dict[str, Any]) -> list[str]:
    if not isinstance(item, dict):
        return ["audit item must be a mapping"]
    schema = contract["audit_item_schema"]
    where = f"item `{item.get('id')}`"
    errors = [f"{where}: missing `{key}`" for key in schema["required"] if not item.get(key)]
    known = set(schema["required"]) | set(schema["context"]) | set(schema["optional"])
    if unknown := sorted(set(item) - known):
        errors.append(f"{where}: unknown keys {unknown}")
    if item.get("captured_on") and not DATE_RE.fullmatch(str(item["captured_on"])):
        errors.append(f"{where}: captured_on must be YYYY-MM-DD")
    location = str(item.get("location", ""))
    if "://" in location or location.startswith("www."):
        errors.append(f"{where}: location must be an opaque inventory id, not a URL")
    return errors


def context_gaps(item: dict[str, Any], ctx: Context, contract: dict[str, Any]) -> list[str]:
    gaps = [key for key in contract["audit_item_schema"]["context"] if not item.get(key)]
    content_type = item.get("content_type")
    if content_type and content_type not in contract["content_types"]:
        gaps.append("unknown_content_type")
    elif content_type:
        required = contract["content_types"][content_type].get("required_context") or []
        gaps += [key for key in required if not item.get(key)]
    product = item.get("product")
    if product and ctx.layers.get(product, {}).get("status") != "available":
        gaps.append("product_layer_missing")
    if item.get("contract") and item["contract"] not in ctx.contracts:
        gaps.append("unknown_contract")
    return gaps


def judges(rule_id: str, content_type: dict[str, Any]) -> bool:
    """Whether a rule is judged for a content type (AUD-006)."""
    return any(fnmatch.fnmatchcase(rule_id, pattern) for pattern in content_type.get("judged_rules") or [])


def label_findings(item: dict[str, Any], ctx: Context) -> list[dict[str, Any]]:
    concepts = [c for c in item.get("concepts") or [] if c in ctx.terms]
    text = str(item.get("observed_text", ""))
    # A forbidden label is skipped only when it lies inside an approved label
    # (درخواست in درخواست شغلی). Masking approved labels first would also hide a
    # forbidden phrase that contains a short approved label (آگهی in آگهی استخدام).
    approved_spans = [
        (m.start(), m.end())
        for concept in concepts
        for label in ctx.preferred(concept)
        if label
        for m in re.finditer(re.escape(label), text)
    ]

    def outside_approved(label: str) -> bool:
        return any(
            not any(start <= m.start() and m.end() <= end for start, end in approved_spans)
            for m in re.finditer(re.escape(label), text)
        )

    found: list[dict[str, Any]] = []
    for concept in concepts:
        term = ctx.terms[concept]
        preferred = term.get("preferred")
        approved = _labels(preferred.get("default")) if isinstance(preferred, dict) and "default" in preferred else []
        approved += [label for label in _labels(preferred) if label not in approved]
        entries = [
            ("forbidden", f.get("label") if isinstance(f, dict) else f, f.get("scope", "concept") if isinstance(f, dict) else "concept")
            for f in term.get("forbidden") or []
        ] + [
            ("legacy", f.get("label") if isinstance(f, dict) else f, "concept")
            for f in term.get("legacy_labels") or []
        ]
        for kind, label, scope in entries:
            if label and outside_approved(label):
                found.append({
                    "concept": concept,
                    "label": label,
                    "kind": kind,
                    "scope": scope,
                    "approved_labels": approved,
                    "needs_review": scope != "concept",
                })
    return found


def priority(dimensions: list[str], surface: str | None, model: dict[str, Any]) -> str | None:
    ranks = [model["dimension_rank"][d] for d in dimensions if d in model["dimension_rank"]]
    if not ranks:
        return None
    return f"P{min(4, min(ranks) + model['surface_offset'].get(surface or '', 1))}"


def rewrite_brief(item: dict[str, Any], ctx: Context) -> dict[str, Any]:
    contract = ctx.contracts.get(item["contract"], {})
    _, required = anatomy_roles(contract.get("anatomy"))
    brief = {
        "id": f"rewrite_{item['id']}",
        "product": item["product"],
        "audience": list(item["audience"]),
        "surface": item["surface"],
        "contract": item["contract"],
        "states": [{"id": item["state"], "slots": sorted(required | {item["slot"]})}],
        "concepts": list(item.get("concepts") or []),
        "context": f"بازنویسی copy دیده‌شده: {item['observed_text']}",
    }
    if item.get("product_facts"):
        brief["product_facts"] = item["product_facts"]
    return brief


def check_item(item: dict[str, Any], ctx: Context, contract: dict[str, Any]) -> dict[str, Any]:
    ctx = ctx.for_product(item.get("product"))
    finding: dict[str, Any] = {
        "item_id": item["id"],
        "location": item["location"],
        "surface": item.get("surface"),
        "content_type": item.get("content_type"),
    }
    gaps = context_gaps(item, ctx, contract)
    if gaps:
        return {**finding, "status": "needs_context", "context_gaps": gaps}
    content_type = contract["content_types"][item["content_type"]]
    model = contract["priority_model"]
    finding["decision_owner"] = content_type["decision_owner"]
    # Only content types that allow a rewrite get a brief (AUD-004, AUD-006); for
    # the others the approved terminology label is the whole correction.
    brief = {"rewrite_brief": rewrite_brief(item, ctx)} if content_type.get("rewrite") else {}
    labels = label_findings(item, ctx) if judges(model["default_rule_for_labels"], content_type) else []
    if not labels:
        # The brief is kept so a later semantic finding can still be rewritten (AUD-004).
        return {**finding, "status": "no_issue", "rule_ids": [], "dimensions": [], **brief}
    return {
        **finding,
        "status": "finding",
        "rule_ids": [model["default_rule_for_labels"]],
        "dimensions": ["terminology"],
        "label_findings": labels,
        "priority": priority(["terminology"], item["surface"], model),
        **brief,
    }


VOICE_CONTRACT = "content.foundation.product_voice"


def semantic_task(item: dict[str, Any], repository_commit: str, contract: dict[str, Any]) -> dict[str, Any]:
    content_type = contract["content_types"][item["content_type"]]
    return {
        "case_id": item["id"],
        "fixture_path": "audit",
        "repository_commit": repository_commit,
        "evaluator_version": EVALUATOR_VERSION,
        "policy_refs": [item.get("contract") or VOICE_CONTRACT],
        "judged_rules": list(content_type.get("judged_rules") or []),
        "input": {
            "context": {
                k: item[k] for k in ("product", "audience", "surface", "content_type", "state", "slot") if k in item
            },
            "concepts": item.get("concepts") or [],
            "content": {item.get("slot") or "text": item["observed_text"]},
        },
        "response_contract": {
            "case_id": "string",
            "valid": "boolean",
            "violations": "string[]",
            "rationale": "non-empty string",
            "corrected_example": "required when invalid; null when valid",
            "unsupported_product_or_runtime_claim": "boolean",
            "guideline_gap": "optional string when a real problem matches no rule",
        },
    }


def rule_dimensions() -> dict[str, str]:
    return {
        rule["id"]: rule.get("dimension", "")
        for data in contracts_by_id().values()
        for rule in data.get("rules") or []
        if isinstance(rule, dict) and "id" in rule
    }


def summarize(findings: list[dict[str, Any]], semantic: list[dict[str, Any]], contract: dict[str, Any]) -> dict[str, Any]:
    by_id = {f["item_id"]: dict(f) for f in findings}
    dims = rule_dimensions()
    model = contract["priority_model"]
    types = contract["content_types"]
    claims = contract["claim_routing"]
    for response in semantic:
        finding = by_id.get(response.get("case_id"))
        if finding is None or finding["status"] == "needs_context":
            continue
        content_type = types.get(finding.get("content_type") or "", {})
        # A violation outside the rules judged for the content type is dropped (AUD-006).
        violations = [
            v for v in response.get("violations") or [] if isinstance(v, str) and judges(v, content_type)
        ]
        gap = str(response.get("guideline_gap") or "").strip()
        if not violations and not gap:
            continue
        finding["status"] = "finding"
        claim_rules = [r for r, d in dims.items() if d == claims["dimension"] and judges(r, content_type)]
        if response.get("unsupported_product_or_runtime_claim") is True and claim_rules:
            finding["decision_owner"] = claims["decision_owner"]  # AUD-005
        finding["rule_ids"] = sorted(set(finding.get("rule_ids") or []) | set(violations))
        finding["dimensions"] = sorted({dims.get(r, "") for r in finding["rule_ids"]} - {""})
        if gap:
            finding["guideline_gap"] = gap
        finding["priority"] = priority(finding["dimensions"], finding.get("surface"), model) or finding.get("priority")
    for finding in by_id.values():
        if finding["status"] == "finding" and claims["dimension"] in (finding.get("dimensions") or []):
            finding["decision_owner"] = claims["decision_owner"]  # AUD-005
    merged = list(by_id.values())
    for finding in merged:
        if finding["status"] == "finding" and not finding.get("rule_ids") and not finding.get("guideline_gap"):
            raise EvalError(f"{finding['item_id']}: finding needs rule_ids or guideline_gap (AUD-001)")
    status = Counter(f["status"] for f in merged)
    return {
        "mode": "report-only",
        "items": len(merged),
        "status": dict(sorted(status.items())),
        "priority": dict(sorted(Counter(f["priority"] for f in merged if f.get("priority")).items())),
        "dimensions": dict(sorted(Counter(d for f in merged for d in f.get("dimensions") or []).items())),
        "content_type": dict(sorted(Counter(f["content_type"] for f in merged if f.get("content_type")).items())),
        "decision_owner": dict(sorted(
            Counter(f["decision_owner"] for f in merged if f["status"] == "finding" and f.get("decision_owner")).items()
        )),
        "guideline_gaps": sorted(f["item_id"] for f in merged if f.get("guideline_gap")),
        "context_gaps": dict(sorted(Counter(g for f in merged for g in f.get("context_gaps") or []).items())),
        "findings": merged,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = ["# Copy audit summary (report-only)", "", f"- Items: {report['items']}"]
    for key in ("status", "priority", "dimensions", "content_type", "decision_owner", "context_gaps"):
        values = ", ".join(f"{k}: {v}" for k, v in report[key].items()) or "—"
        lines.append(f"- {key.replace('_', ' ').capitalize()}: {values}")
    lines.append(f"- Guideline gaps: {', '.join(report['guideline_gaps']) or '—'}")
    lines += ["", "| Item | Location | Type | Owner | Priority | Rules | Labels |", "|---|---|---|---|---|---|---|"]
    for f in sorted(report["findings"], key=lambda f: (f.get("priority") or "P9", f["item_id"])):
        if f["status"] != "finding":
            continue
        labels = "، ".join(f"{x['label']} → {' / '.join(x['approved_labels']) or '?'}" for x in f.get("label_findings") or [])
        lines.append(f"| `{f['item_id']}` | `{f['location']}` | {f.get('content_type') or '—'} | {f.get('decision_owner') or '—'} | {f.get('priority') or '—'} | {', '.join(f.get('rule_ids') or []) or 'gap'} | {labels or '—'} |")
    return "\n".join(lines) + "\n"


def load_items(path: Path, contract: dict[str, Any]) -> list[dict[str, Any]]:
    items = read_jsonl(path)
    errors = [e for item in items for e in validate_item(item, contract)]
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append("duplicate audit item ids")
    if errors:
        raise EvalError("; ".join(errors))
    return items


def command_check(args: argparse.Namespace) -> int:
    contract, ctx = load_contract(), Context.from_repository()
    findings = [check_item(item, ctx, contract) for item in load_items(args.items, contract)]
    write_jsonl(findings, args.output)
    counts = Counter(f["status"] for f in findings)
    print(f"Checked {len(findings)} audit items: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


def command_prepare(args: argparse.Namespace) -> int:
    contract, ctx = load_contract(), Context.from_repository()
    items = [i for i in load_items(args.items, contract) if not context_gaps(i, ctx, contract)]
    write_jsonl([semantic_task(i, args.repository_commit, contract) for i in items], args.output)
    print(f"Prepared {len(items)} semantic audit tasks at {args.output}")
    return 0


def command_summarize(args: argparse.Namespace) -> int:
    contract = load_contract()
    semantic = read_jsonl(args.semantic) if args.semantic else []
    report = summarize(read_jsonl(args.findings), semantic, contract)
    args.report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if args.report_markdown:
        args.report_markdown.write_text(render_markdown(report), encoding="utf-8")
    print(f"Summarized {report['items']} audit items in report-only mode")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--items", type=Path, required=True)
    check.add_argument("--output", type=Path, required=True)
    check.set_defaults(func=command_check)
    prepare = sub.add_parser("prepare")
    prepare.add_argument("--items", type=Path, required=True)
    prepare.add_argument("--repository-commit", required=True)
    prepare.add_argument("--output", type=Path, required=True)
    prepare.set_defaults(func=command_prepare)
    summary = sub.add_parser("summarize")
    summary.add_argument("--findings", type=Path, required=True)
    summary.add_argument("--semantic", type=Path)
    summary.add_argument("--report-json", type=Path, required=True)
    summary.add_argument("--report-markdown", type=Path)
    summary.set_defaults(func=command_summarize)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except EvalError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
