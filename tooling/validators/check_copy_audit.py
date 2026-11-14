#!/usr/bin/env python3
"""Validate the copy audit contract and its deterministic regression cases.

Each case runs the real audit checker on a sample item and compares the result
with the expected status, context gaps, decision owner, label findings,
priority and rewrite brief. Every rewrite brief must also pass the copy-brief validator, and every
blocking `AUD` rule must be covered by at least one case.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tooling.audit.run_copy_audit import (  # noqa: E402
    FINDING_STATUSES,
    judges,
    check_item,
    load_contract,
    validate_item,
)
from tooling.content_rule_index import contracts_by_id  # noqa: E402
from tooling.validators.check_content_contracts import RULE_DIMENSIONS  # noqa: E402
from tooling.validators.check_copy_briefs import Context, validate_brief  # noqa: E402

CASES_DIR = ROOT / "ai" / "evals" / "content" / "audit"
LOCALIZATION = ROOT / "foundations" / "content" / "localization.yml"
EXPECTED_KEYS = {
    "checked_rules", "status", "priority", "decision_owner", "label_findings", "context_gaps", "rewrite_slots",
}


def known_rule_ids() -> set[str]:
    ids = {r["id"] for data in contracts_by_id().values() for r in data.get("rules") or [] if isinstance(r, dict)}
    localization = yaml.safe_load(LOCALIZATION.read_text(encoding="utf-8")) or {}
    return ids | {r["id"] for r in localization.get("rules") or [] if isinstance(r, dict) and "id" in r}


def validate_content_types(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    types = contract.get("content_types") or {}
    if not types:
        return ["copy-audit.yml: content_types is empty"]
    schema = contract.get("audit_item_schema") or {}
    if "content_type" not in (schema.get("context") or []):
        errors.append("copy-audit.yml: content_type must be a context field (AUD-005)")
    optional = set(schema.get("optional") or [])
    rules = known_rule_ids()
    for name, spec in types.items():
        where = f"copy-audit.yml: content type `{name}`"
        if not isinstance(spec, dict) or not spec.get("decision_owner") or not spec.get("label"):
            errors.append(f"{where}: needs label and decision_owner")
            continue
        if not isinstance(spec.get("rewrite"), bool):
            errors.append(f"{where}: rewrite must be true or false")
        if extra := sorted(set(spec.get("required_context") or []) - optional):
            errors.append(f"{where}: required_context must be optional item fields; unknown {extra}")
        patterns = spec.get("judged_rules") or []
        if not patterns:
            errors.append(f"{where}: judged_rules is empty")
        for pattern in patterns:
            if not any(judges(rule, {"judged_rules": [pattern]}) for rule in rules):
                errors.append(f"{where}: judged rule `{pattern}` matches no active rule")
        if spec.get("rewrite") and "*" not in patterns:
            errors.append(f"{where}: a content type with rewrite must judge every rule")
    for pattern in (contract.get("review_model") or {}).get("mechanical_rules") or []:
        if not any(judges(rule, {"judged_rules": [pattern]}) for rule in rules):
            errors.append(f"copy-audit.yml: mechanical rule `{pattern}` matches no active rule")
    if not contract.get("source_kinds"):
        errors.append("copy-audit.yml: source_kinds is empty")
    claims = contract.get("claim_routing") or {}
    if claims.get("dimension") not in ((contract.get("priority_model") or {}).get("dimension_rank") or {}):
        errors.append("copy-audit.yml: claim_routing.dimension must be a ranked dimension")
    if not claims.get("decision_owner"):
        errors.append("copy-audit.yml: claim_routing needs a decision_owner")
    return errors


def validate_contract(contract: dict[str, Any], ctx: Context) -> list[str]:
    errors: list[str] = []
    model = contract.get("priority_model") or {}
    ranked = set(model.get("dimension_rank") or {})
    if missing := sorted(set(RULE_DIMENSIONS) - {"presentation"} - ranked):
        errors.append(f"copy-audit.yml: priority_model lacks dimensions {missing}")
    if unknown := sorted(ranked - set(RULE_DIMENSIONS)):
        errors.append(f"copy-audit.yml: priority_model has unknown dimensions {unknown}")
    if bad := sorted(set(model.get("surface_offset") or {}) ^ ctx.visibility):
        errors.append(f"copy-audit.yml: surface_offset must cover exactly the visibility values; differs at {bad}")
    rule = model.get("default_rule_for_labels")
    known_rules = {r["id"] for data in ctx.contracts.values() for r in data.get("rules") or [] if isinstance(r, dict)}
    if rule not in known_rules:
        errors.append(f"copy-audit.yml: default_rule_for_labels `{rule}` is not an active rule")
    if set(contract.get("finding_schema", {}).get("status") or []) != set(FINDING_STATUSES):
        errors.append("copy-audit.yml: finding_schema.status must match the tool statuses")
    return errors + validate_content_types(contract)


def validate_case(case: Any, ctx: Context, contract: dict[str, Any], rules: set[str]) -> tuple[list[str], set[str]]:
    if not isinstance(case, dict) or not isinstance(case.get("id"), str):
        return ["case must be a mapping with an id"], set()
    where = f"case `{case['id']}`"
    item, expected = case.get("item"), case.get("expected")
    if not isinstance(expected, dict):
        return [f"{where}: expected must be a mapping"], set()
    errors = [f"{where}: {e}" for e in validate_item(item, contract)]
    if errors:
        return errors, set()
    if unknown := sorted(set(expected) - EXPECTED_KEYS):
        errors.append(f"{where}: unknown expected keys {unknown}")
    checked = set(expected.get("checked_rules") or [])
    if not checked or checked - rules:
        errors.append(f"{where}: checked_rules must be non-empty AUD rules")

    actual = check_item(item, ctx, contract)
    if actual["status"] != expected.get("status"):
        return errors + [f"{where}: status `{actual['status']}`, expected `{expected.get('status')}`"], checked
    if actual.get("context_gaps", []) != expected.get("context_gaps", []):
        errors.append(f"{where}: context_gaps {actual.get('context_gaps')} != {expected.get('context_gaps')}")
    if "decision_owner" in expected and actual.get("decision_owner") != expected["decision_owner"]:
        errors.append(f"{where}: decision_owner {actual.get('decision_owner')} != {expected['decision_owner']}")
    if actual.get("priority") != expected.get("priority"):
        errors.append(f"{where}: priority {actual.get('priority')} != {expected.get('priority')}")
    got = [
        {k: f[k] for k in ("concept", "label", "kind", "needs_review")}
        for f in actual.get("label_findings") or []
    ]
    if got != (expected.get("label_findings") or []):
        errors.append(f"{where}: label_findings {got} != {expected.get('label_findings')}")
    for f in actual.get("label_findings") or []:
        if not f["approved_labels"]:
            errors.append(f"{where}: `{f['label']}` has no approved terminology label (AUD-002)")
    if actual["status"] == "finding" and not actual.get("rule_ids") and not actual.get("guideline_gap"):
        errors.append(f"{where}: finding needs rule_ids or guideline_gap (AUD-001)")
    brief = actual.get("rewrite_brief")
    if brief is not None:
        errors += [f"{where}: rewrite brief: {e}" for e in validate_brief(brief, ctx, "rewrite", False)]
        slots = brief["states"][0]["slots"]
        if slots != expected.get("rewrite_slots"):
            errors.append(f"{where}: rewrite slots {slots} != {expected.get('rewrite_slots')}")
    elif expected.get("rewrite_slots"):
        errors.append(f"{where}: expected a rewrite brief")
    return errors, checked


def main() -> int:
    contract, ctx = load_contract(), Context.from_repository()
    errors = validate_contract(contract, ctx)
    rules = {r["id"]: r["obligation"] for r in contract.get("rules") or []}
    covered: set[str] = set()
    count = 0
    paths = sorted(CASES_DIR.glob("*-cases.yml"))
    if not paths:
        errors.append(f"{CASES_DIR.relative_to(ROOT)}: no audit cases")
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        ids = [c.get("id") for c in data.get("cases") or [] if isinstance(c, dict)]
        if len(ids) != len(set(ids)):
            errors.append(f"{path.name}: duplicate case ids")
        for case in data.get("cases") or []:
            case_errors, checked = validate_case(case, ctx, contract, set(rules))
            errors += [f"{path.name}: {e}" for e in case_errors]
            covered |= checked
            count += 1
    blocking = {rid for rid, ob in rules.items() if ob in {"must", "must_not"}}
    if missing := sorted(blocking - covered):
        errors.append(f"audit cases do not cover blocking rules: {', '.join(missing)}")
    if errors:
        print("Copy audit validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Copy audit is valid: {count} cases, {len(blocking)} blocking AUD rules covered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
