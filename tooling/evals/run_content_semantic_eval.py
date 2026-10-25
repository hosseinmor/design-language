#!/usr/bin/env python3
"""Prepare and score report-only semantic content evaluations."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURES_DIR = ROOT / "ai" / "evals" / "content"
EVALUATOR_VERSION = "content-semantic-evaluator-v1"


class EvalError(ValueError):
    """Raised when fixtures or evaluator responses violate the contract."""


@dataclass(frozen=True)
class EvalCase:
    case_id: str
    suite_id: str
    fixture_path: str
    policy_refs: tuple[str, ...]
    payload: dict[str, Any]
    expected_valid: bool
    expected_violations: tuple[str, ...]


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise EvalError(f"{path}: cannot load YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise EvalError(f"{path}: top level must be a mapping")
    return data


def load_cases(fixtures_dir: Path = DEFAULT_FIXTURES_DIR) -> list[EvalCase]:
    paths = sorted(fixtures_dir.glob("*-cases.yml"))
    if not paths:
        raise EvalError(f"{fixtures_dir}: no *-cases.yml fixtures found")

    loaded: list[EvalCase] = []
    seen: set[str] = set()
    for path in paths:
        data = _load_yaml(path)
        suite_id = data.get("id")
        if not _nonempty_string(suite_id):
            raise EvalError(f"{path}: missing non-empty suite id")

        refs = tuple(
            value
            for key in ("component_id", "pattern_id", "foundation_id")
            if _nonempty_string(value := data.get(key))
        )
        raw_cases = data.get("cases")
        if not isinstance(raw_cases, list) or not raw_cases:
            raise EvalError(f"{path}: cases must be a non-empty list")

        for index, raw_case in enumerate(raw_cases):
            location = f"{path}: cases[{index}]"
            if not isinstance(raw_case, dict):
                raise EvalError(f"{location} must be a mapping")
            local_id = raw_case.get("id")
            if not _nonempty_string(local_id):
                raise EvalError(f"{location}: missing non-empty id")
            case_id = f"{suite_id}::{local_id}"
            if case_id in seen:
                raise EvalError(f"duplicate case id: {case_id}")
            seen.add(case_id)

            expected = raw_case.get("expected")
            if not isinstance(expected, dict):
                raise EvalError(f"{case_id}: expected must be a mapping")
            expected_valid = expected.get("valid")
            if not isinstance(expected_valid, bool):
                raise EvalError(f"{case_id}: expected.valid must be boolean")
            expected_violations = expected.get("violations")
            if not isinstance(expected_violations, list) or not all(
                _nonempty_string(item) for item in expected_violations
            ):
                raise EvalError(
                    f"{case_id}: expected.violations must be a string list"
                )
            if len(expected_violations) != len(set(expected_violations)):
                raise EvalError(f"{case_id}: duplicate expected violations")
            if expected_valid and expected_violations:
                raise EvalError(
                    f"{case_id}: valid case cannot declare violations"
                )
            if not expected_valid and not expected_violations:
                raise EvalError(
                    f"{case_id}: invalid case requires violations"
                )

            payload = {
                key: value
                for key, value in raw_case.items()
                if key not in {"id", "expected"}
            }
            loaded.append(
                EvalCase(
                    case_id=case_id,
                    suite_id=suite_id,
                    fixture_path=str(path.relative_to(ROOT)),
                    policy_refs=refs,
                    payload=payload,
                    expected_valid=expected_valid,
                    expected_violations=tuple(expected_violations),
                )
            )
    return loaded


def build_tasks(
    cases: Iterable[EvalCase], repository_commit: str
) -> list[dict[str, Any]]:
    if not _nonempty_string(repository_commit):
        raise EvalError("repository commit must be non-empty")
    return [
        {
            "case_id": case.case_id,
            "fixture_path": case.fixture_path,
            "repository_commit": repository_commit,
            "evaluator_version": EVALUATOR_VERSION,
            "policy_refs": list(case.policy_refs),
            "input": case.payload,
            "response_contract": {
                "case_id": "string",
                "valid": "boolean",
                "violations": "string[]",
                "rationale": "non-empty string",
                "corrected_example": "required when invalid; null when valid",
                "unsupported_product_or_runtime_claim": "boolean",
            },
        }
        for case in cases
    ]


def write_jsonl(items: Iterable[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in items:
            handle.write(json.dumps(item, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise EvalError(f"{path}: cannot read responses: {exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise EvalError(
                f"{path}:{line_number}: invalid JSON: {exc.msg}"
            ) from exc
        if not isinstance(item, dict):
            raise EvalError(f"{path}:{line_number}: response must be an object")
        items.append(item)
    return items


def normalize_responses(
    raw_responses: Iterable[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    normalized: dict[str, dict[str, Any]] = {}
    for index, response in enumerate(raw_responses):
        location = f"responses[{index}]"
        case_id = response.get("case_id")
        if not _nonempty_string(case_id):
            raise EvalError(f"{location}.case_id must be non-empty")
        if case_id in normalized:
            raise EvalError(f"duplicate response case_id: {case_id}")

        valid = response.get("valid")
        if not isinstance(valid, bool):
            raise EvalError(f"{case_id}: valid must be boolean")
        violations = response.get("violations")
        if not isinstance(violations, list) or not all(
            _nonempty_string(item) for item in violations
        ):
            raise EvalError(f"{case_id}: violations must be a string list")
        if len(violations) != len(set(violations)):
            raise EvalError(f"{case_id}: duplicate predicted violations")
        if valid and violations:
            raise EvalError(f"{case_id}: valid response cannot have violations")
        if not valid and not violations:
            raise EvalError(f"{case_id}: invalid response requires violations")

        rationale = response.get("rationale")
        if not _nonempty_string(rationale):
            raise EvalError(f"{case_id}: rationale must be non-empty")
        corrected = response.get("corrected_example")
        if not valid and corrected in (None, "", {}, []):
            raise EvalError(
                f"{case_id}: corrected_example is required when invalid"
            )
        unsupported = response.get("unsupported_product_or_runtime_claim")
        if not isinstance(unsupported, bool):
            raise EvalError(
                f"{case_id}: unsupported_product_or_runtime_claim must be boolean"
            )

        normalized[case_id] = {
            "valid": valid,
            "violations": sorted(set(violations)),
            "rationale": rationale.strip(),
            "corrected_example": corrected,
            "unsupported_product_or_runtime_claim": unsupported,
        }
    return normalized


def _ratio(numerator: int, denominator: int) -> float | None:
    if denominator == 0:
        return None
    return round(numerator / denominator, 6)


def score_responses(
    cases: Iterable[EvalCase],
    responses: dict[str, dict[str, Any]],
    metadata: dict[str, Any],
) -> dict[str, Any]:
    cases_by_id = {case.case_id: case for case in cases}
    missing = sorted(set(cases_by_id) - set(responses))
    unexpected = sorted(set(responses) - set(cases_by_id))

    details: list[dict[str, Any]] = []
    case_correct = 0
    valid_case_count = 0
    false_positive_valid_cases = 0
    rule_tp = rule_fp = rule_fn = 0
    unsupported_claims = 0

    for case_id in sorted(set(cases_by_id) & set(responses)):
        case = cases_by_id[case_id]
        response = responses[case_id]
        expected = set(case.expected_violations)
        predicted = set(response["violations"])
        valid_match = response["valid"] == case.expected_valid
        if valid_match:
            case_correct += 1
        if case.expected_valid:
            valid_case_count += 1
            if not response["valid"]:
                false_positive_valid_cases += 1

        tp = sorted(expected & predicted)
        fp = sorted(predicted - expected)
        fn = sorted(expected - predicted)
        rule_tp += len(tp)
        rule_fp += len(fp)
        rule_fn += len(fn)
        if response["unsupported_product_or_runtime_claim"]:
            unsupported_claims += 1

        details.append(
            {
                "case_id": case_id,
                "fixture_path": case.fixture_path,
                "expected": {
                    "valid": case.expected_valid,
                    "violations": sorted(expected),
                },
                "actual": response,
                "classification_correct": valid_match,
                "rule_true_positives": tp,
                "rule_false_positives": fp,
                "rule_false_negatives": fn,
            }
        )

    scored_count = len(details)
    return {
        "schema_version": "0.1",
        "mode": "report_only",
        "blocking": False,
        "metadata": metadata,
        "coverage": {
            "fixture_cases": len(cases_by_id),
            "scored_cases": scored_count,
            "missing_cases": missing,
            "unexpected_cases": unexpected,
            "complete": not missing and not unexpected,
        },
        "metrics": {
            "case_classification_accuracy": _ratio(case_correct, scored_count),
            "rule_precision": _ratio(rule_tp, rule_tp + rule_fp),
            "rule_recall": _ratio(rule_tp, rule_tp + rule_fn),
            "false_positive_rate_on_valid_cases": _ratio(
                false_positive_valid_cases, valid_case_count
            ),
            "unsupported_product_or_runtime_claim_rate": _ratio(
                unsupported_claims, scored_count
            ),
            "counts": {
                "case_correct": case_correct,
                "valid_cases": valid_case_count,
                "false_positive_valid_cases": false_positive_valid_cases,
                "rule_true_positives": rule_tp,
                "rule_false_positives": rule_fp,
                "rule_false_negatives": rule_fn,
                "unsupported_claims": unsupported_claims,
            },
        },
        "cases": details,
    }


def render_markdown(report: dict[str, Any]) -> str:
    coverage = report["coverage"]
    metrics = report["metrics"]
    meta = report["metadata"]

    def value(key: str) -> str:
        item = metrics[key]
        return "n/a" if item is None else f"{item:.3f}"

    lines = [
        "# Content semantic evaluation report",
        "",
        "- Mode: report-only (non-blocking)",
        f"- Repository commit: `{meta['repository_commit']}`",
        f"- Model: `{meta['model']}`",
        f"- Model version: `{meta['model_version']}`",
        f"- Evaluator: `{meta['evaluator_version']}`",
        f"- Executed at: `{meta['executed_at']}`",
        f"- Coverage: {coverage['scored_cases']}/{coverage['fixture_cases']}",
        "",
        "## Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
        f"| Case classification accuracy | {value('case_classification_accuracy')} |",
        f"| Rule precision | {value('rule_precision')} |",
        f"| Rule recall | {value('rule_recall')} |",
        f"| False-positive rate on valid cases | {value('false_positive_rate_on_valid_cases')} |",
        f"| Unsupported product/runtime claim rate | {value('unsupported_product_or_runtime_claim_rate')} |",
        "",
    ]
    if coverage["missing_cases"]:
        lines.extend(
            [
                "## Missing cases",
                "",
                *[f"- `{case_id}`" for case_id in coverage["missing_cases"]],
                "",
            ]
        )
    failures = [
        item
        for item in report["cases"]
        if (
            not item["classification_correct"]
            or item["rule_false_positives"]
            or item["rule_false_negatives"]
            or item["actual"]["unsupported_product_or_runtime_claim"]
        )
    ]
    lines.extend(["## Cases needing review", ""])
    if not failures:
        lines.append("- None")
    else:
        for item in failures:
            lines.append(f"### `{item['case_id']}`")
            lines.append("")
            lines.append(f"- Rationale: {item['actual']['rationale']}")
            if item["rule_false_positives"]:
                lines.append(
                    "- Unexpected violations: "
                    + ", ".join(item["rule_false_positives"])
                )
            if item["rule_false_negatives"]:
                lines.append(
                    "- Missed violations: "
                    + ", ".join(item["rule_false_negatives"])
                )
            if item["actual"]["unsupported_product_or_runtime_claim"]:
                lines.append("- Unsupported product/runtime claim: yes")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _metadata_from_args(args: argparse.Namespace) -> dict[str, Any]:
    try:
        decoding = json.loads(args.decoding_config_json)
    except json.JSONDecodeError as exc:
        raise EvalError(
            f"--decoding-config-json is invalid JSON: {exc.msg}"
        ) from exc
    if not isinstance(decoding, dict):
        raise EvalError("--decoding-config-json must be a JSON object")
    executed_at = args.executed_at or datetime.now(timezone.utc).isoformat()
    return {
        "repository_commit": args.repository_commit,
        "model": args.model,
        "model_version": args.model_version,
        "evaluator_version": EVALUATOR_VERSION,
        "prompt_version": EVALUATOR_VERSION,
        "decoding_configuration": decoding,
        "executed_at": executed_at,
    }


def command_validate(args: argparse.Namespace) -> int:
    cases = load_cases(args.fixtures_dir)
    suites = len({case.suite_id for case in cases})
    print(f"Semantic fixtures are valid: {len(cases)} cases in {suites} suites")
    return 0


def command_prepare(args: argparse.Namespace) -> int:
    cases = load_cases(args.fixtures_dir)
    tasks = build_tasks(cases, args.repository_commit)
    write_jsonl(tasks, args.output)
    print(f"Prepared {len(tasks)} report-only tasks at {args.output}")
    return 0


def command_score(args: argparse.Namespace) -> int:
    cases = load_cases(args.fixtures_dir)
    responses = normalize_responses(read_jsonl(args.responses))
    report = score_responses(cases, responses, _metadata_from_args(args))

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if args.report_markdown:
        args.report_markdown.parent.mkdir(parents=True, exist_ok=True)
        args.report_markdown.write_text(
            render_markdown(report), encoding="utf-8"
        )

    print(
        "Semantic evaluation scored in report-only mode: "
        f"{report['coverage']['scored_cases']}/"
        f"{report['coverage']['fixture_cases']} cases"
    )
    if not args.allow_partial and not report["coverage"]["complete"]:
        raise EvalError(
            "response coverage is incomplete; use --allow-partial only for an "
            "explicit pilot"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare and score report-only content semantic evaluations."
    )
    parser.set_defaults(fixtures_dir=DEFAULT_FIXTURES_DIR)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser(
        "validate", help="Validate all fixture schemas."
    )
    validate_parser.add_argument(
        "--fixtures-dir", type=Path, default=DEFAULT_FIXTURES_DIR
    )
    validate_parser.set_defaults(func=command_validate)

    prepare_parser = subparsers.add_parser(
        "prepare", help="Create answer-free JSONL tasks for a model runner."
    )
    prepare_parser.add_argument(
        "--fixtures-dir", type=Path, default=DEFAULT_FIXTURES_DIR
    )
    prepare_parser.add_argument("--repository-commit", required=True)
    prepare_parser.add_argument("--output", type=Path, required=True)
    prepare_parser.set_defaults(func=command_prepare)

    score_parser = subparsers.add_parser(
        "score", help="Score JSONL evaluator responses and write reports."
    )
    score_parser.add_argument(
        "--fixtures-dir", type=Path, default=DEFAULT_FIXTURES_DIR
    )
    score_parser.add_argument("--responses", type=Path, required=True)
    score_parser.add_argument("--report-json", type=Path, required=True)
    score_parser.add_argument("--report-markdown", type=Path)
    score_parser.add_argument("--repository-commit", required=True)
    score_parser.add_argument("--model", required=True)
    score_parser.add_argument("--model-version", required=True)
    score_parser.add_argument(
        "--decoding-config-json", default="{}", help="JSON object"
    )
    score_parser.add_argument("--executed-at")
    score_parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="Allow an explicit pilot to omit some fixtures.",
    )
    score_parser.set_defaults(func=command_score)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except EvalError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
