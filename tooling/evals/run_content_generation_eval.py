#!/usr/bin/env python3
"""Prepare and score report-only copy generation evaluations.

Each fixture case is a copy brief plus measurable expectations. `prepare`
writes answer-free tasks (brief, policy references and output contract) for a
reviewed model adapter. `score` checks generator outputs deterministically:
outcome, filled and empty slots, open questions, draft dependencies, required
and forbidden labels, and declared rules. Rule-level quality of the produced
copy is judged separately with the semantic evaluator. Mismatches never fail
the command; malformed fixtures or responses do.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tooling.evals.run_content_semantic_eval import (  # noqa: E402
    EvalError,
    read_jsonl,
    write_jsonl,
)
from tooling.validators.check_copy_briefs import (  # noqa: E402
    GENERATION_DIR,
    Context,
    validate_fixture,
)

GENERATOR_VERSION = "content-copy-generation-v1"
BRIEF_CONTRACT_ID = "content.foundation.copy_brief"


def load_cases(fixtures_dir: Path = GENERATION_DIR) -> list[dict[str, Any]]:
    paths = sorted(fixtures_dir.glob("*-cases.yml"))
    if not paths:
        raise EvalError(f"{fixtures_dir}: no *-cases.yml fixtures found")
    ctx = Context.from_repository()
    cases: list[dict[str, Any]] = []
    for path in paths:
        errors, _ = validate_fixture(path, ctx)
        if errors:
            raise EvalError("; ".join(errors))
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for case in data["cases"]:
            cases.append({**case, "case_id": f"{data['id']}::{case['id']}"})
    return cases


def build_tasks(cases: list[dict[str, Any]], repository_commit: str) -> list[dict[str, Any]]:
    if not repository_commit.strip():
        raise EvalError("repository commit must be non-empty")
    return [
        {
            "case_id": case["case_id"],
            "repository_commit": repository_commit,
            "generator_version": GENERATOR_VERSION,
            "policy_refs": [BRIEF_CONTRACT_ID, case["brief"]["contract"]],
            "input": {"brief": case["brief"]},
            "response_contract": {
                "case_id": "string",
                "brief_id": "string",
                "outcome": "copy | blocked",
                "copy": "state -> slot -> text; required when outcome is copy",
                "checked_rules": "string[]",
                "open_questions": "[{fact, question}]",
                "draft_dependencies": "[{fact, slots}]",
                "blocked_reason": "required when outcome is blocked",
            },
        }
        for case in cases
    ]


def normalize(response: dict[str, Any]) -> dict[str, Any]:
    case_id = response.get("case_id")
    if not isinstance(case_id, str) or not case_id:
        raise EvalError("response case_id must be non-empty")
    outcome = response.get("outcome")
    if outcome not in {"copy", "blocked"}:
        raise EvalError(f"{case_id}: outcome must be copy or blocked")
    copy = response.get("copy") or {}
    if not isinstance(copy, dict) or not all(
        isinstance(slots, dict) and all(isinstance(t, str) for t in slots.values())
        for slots in copy.values()
    ):
        raise EvalError(f"{case_id}: copy must map state -> slot -> text")
    if outcome == "copy" and not copy:
        raise EvalError(f"{case_id}: copy is required when outcome is copy")
    if outcome == "blocked" and not str(response.get("blocked_reason") or "").strip():
        raise EvalError(f"{case_id}: blocked_reason is required when outcome is blocked")
    checked = response.get("checked_rules")
    if not isinstance(checked, list) or not all(isinstance(r, str) for r in checked):
        raise EvalError(f"{case_id}: checked_rules must be a string list")
    lists = {}
    for key in ("open_questions", "draft_dependencies"):
        items = response.get(key) or []
        if not isinstance(items, list) or not all(
            isinstance(i, dict) and isinstance(i.get("fact"), str) for i in items
        ):
            raise EvalError(f"{case_id}: {key} must be a list of objects with `fact`")
        lists[key] = {i["fact"] for i in items}
    return {
        "case_id": case_id,
        "outcome": outcome,
        "copy": copy,
        "checked_rules": set(checked),
        **lists,
    }


def check_case(case: dict[str, Any], response: dict[str, Any]) -> list[str]:
    expected = case["expected"]
    failures: list[str] = []
    if response["outcome"] != expected["outcome"]:
        return [f"outcome `{response['outcome']}`, expected `{expected['outcome']}`"]
    if missing := sorted(set(expected["checked_rules"]) - response["checked_rules"]):
        failures.append(f"checked_rules missing {missing}")
    copy = response["copy"]
    for state, slots in (expected.get("required_slots") or {}).items():
        for slot in slots:
            if not str(copy.get(state, {}).get(slot, "")).strip():
                failures.append(f"required slot `{state}.{slot}` is empty")
    for state, slots in (expected.get("empty_slots") or {}).items():
        for slot in slots:
            if str(copy.get(state, {}).get(slot, "")).strip():
                failures.append(f"slot `{state}.{slot}` should stay empty for an unknown fact")
    for key in ("required_questions", "draft_dependencies"):
        response_key = "open_questions" if key == "required_questions" else key
        if missing := sorted(set(expected.get(key) or []) - response[response_key]):
            failures.append(f"{response_key} missing facts {missing}")
    text = "\n".join(t for slots in copy.values() for t in slots.values())
    for item in expected.get("must_use_labels") or []:
        if item["label"] not in text:
            failures.append(f"required label `{item['label']}` is absent")
    for item in expected.get("forbidden_labels") or []:
        if item["label"] in text:
            failures.append(f"forbidden label `{item['label']}` is used")
    return failures


def score(cases: list[dict[str, Any]], responses: dict[str, dict[str, Any]], metadata: dict[str, Any]) -> dict[str, Any]:
    known = {case["case_id"] for case in cases}
    if extra := sorted(set(responses) - known):
        raise EvalError(f"responses for unknown cases: {extra}")
    results = []
    for case in cases:
        response = responses.get(case["case_id"])
        if response is None:
            continue
        failures = check_case(case, response)
        results.append({"case_id": case["case_id"], "passed": not failures, "failures": failures})
    passed = sum(1 for r in results if r["passed"])
    return {
        "mode": "report-only",
        "metadata": metadata,
        "coverage": {
            "fixture_cases": len(cases),
            "scored_cases": len(results),
            "complete": len(results) == len(cases),
        },
        "summary": {"passed": passed, "failed": len(results) - passed},
        "results": results,
    }


def render_markdown(report: dict[str, Any]) -> str:
    meta, summary = report["metadata"], report["summary"]
    lines = [
        "# Copy generation evaluation (report-only)",
        "",
        f"- Repository commit: `{meta['repository_commit']}`",
        f"- Model: `{meta['model']}` `{meta['model_version']}`",
        f"- Generator version: `{meta['generator_version']}`",
        f"- Executed at: {meta['executed_at']}",
        f"- Scored: {report['coverage']['scored_cases']}/{report['coverage']['fixture_cases']}",
        f"- Passed: {summary['passed']}, failed: {summary['failed']}",
        "",
    ]
    for result in report["results"]:
        if not result["passed"]:
            lines.append(f"## `{result['case_id']}`")
            lines.extend(f"- {failure}" for failure in result["failures"])
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def command_validate(args: argparse.Namespace) -> int:
    cases = load_cases(args.fixtures_dir)
    print(f"Generation fixtures are valid: {len(cases)} cases")
    return 0


def command_prepare(args: argparse.Namespace) -> int:
    tasks = build_tasks(load_cases(args.fixtures_dir), args.repository_commit)
    write_jsonl(tasks, args.output)
    print(f"Prepared {len(tasks)} report-only generation tasks at {args.output}")
    return 0


def command_score(args: argparse.Namespace) -> int:
    cases = load_cases(args.fixtures_dir)
    responses: dict[str, dict[str, Any]] = {}
    for raw in read_jsonl(args.responses):
        response = normalize(raw)
        if response["case_id"] in responses:
            raise EvalError(f"duplicate response case_id: {response['case_id']}")
        responses[response["case_id"]] = response
    metadata = {
        "repository_commit": args.repository_commit,
        "model": args.model,
        "model_version": args.model_version,
        "generator_version": GENERATOR_VERSION,
        "executed_at": args.executed_at or datetime.now(timezone.utc).isoformat(),
    }
    report = score(cases, responses, metadata)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if args.report_markdown:
        args.report_markdown.write_text(render_markdown(report), encoding="utf-8")
    print(
        "Generation evaluation scored in report-only mode: "
        f"{report['summary']['passed']}/{report['coverage']['scored_cases']} passed"
    )
    if not args.allow_partial and not report["coverage"]["complete"]:
        raise EvalError("response coverage is incomplete; use --allow-partial only for a pilot")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func in (("validate", command_validate), ("prepare", command_prepare), ("score", command_score)):
        p = sub.add_parser(name)
        p.add_argument("--fixtures-dir", type=Path, default=GENERATION_DIR)
        p.set_defaults(func=func)
        if name == "prepare":
            p.add_argument("--repository-commit", required=True)
            p.add_argument("--output", type=Path, required=True)
        if name == "score":
            p.add_argument("--responses", type=Path, required=True)
            p.add_argument("--report-json", type=Path, required=True)
            p.add_argument("--report-markdown", type=Path)
            p.add_argument("--repository-commit", required=True)
            p.add_argument("--model", required=True)
            p.add_argument("--model-version", required=True)
            p.add_argument("--executed-at")
            p.add_argument("--allow-partial", action="store_true")
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
