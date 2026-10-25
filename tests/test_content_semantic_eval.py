"""Tests for the report-only content semantic evaluator."""

import json
import tempfile
import unittest
from pathlib import Path

from tooling.evals.run_content_semantic_eval import (
    EvalError,
    build_tasks,
    load_cases,
    normalize_responses,
    render_markdown,
    score_responses,
)


FIXTURE = """
schema_version: "0.1"
id: content.eval.sample
component_id: content.component.button
language: fa-IR
cases:
  - id: valid_case
    context:
      action: save
    content:
      label: ذخیره
    expected:
      valid: true
      checked_rules: [BTN-001]
      violations: []
  - id: invalid_case
    context:
      destructive: true
    content:
      label: ادامه
    expected:
      valid: false
      checked_rules: [BTN-001, BTN-004]
      violations: [BTN-001, BTN-004]
"""


class ContentSemanticEvalTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.fixtures_dir = Path(self.tempdir.name)
        (self.fixtures_dir / "sample-cases.yml").write_text(
            FIXTURE, encoding="utf-8"
        )
        self.cases = load_cases(self.fixtures_dir)

    def tearDown(self):
        self.tempdir.cleanup()

    def test_prepare_hides_expected_answers(self):
        tasks = build_tasks(self.cases, "abc123")
        serialized = json.dumps(tasks, ensure_ascii=False)
        self.assertNotIn('"expected"', serialized)
        self.assertNotIn('"expected_valid"', serialized)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["repository_commit"], "abc123")

    def test_scores_classification_and_rule_metrics(self):
        responses = normalize_responses(
            [
                {
                    "case_id": "content.eval.sample::valid_case",
                    "valid": True,
                    "violations": [],
                    "rationale": "No violation.",
                    "corrected_example": None,
                    "unsupported_product_or_runtime_claim": False,
                },
                {
                    "case_id": "content.eval.sample::invalid_case",
                    "valid": False,
                    "violations": ["BTN-001"],
                    "rationale": "The action is ambiguous.",
                    "corrected_example": {"label": "حذف آگهی"},
                    "unsupported_product_or_runtime_claim": False,
                },
            ]
        )
        report = score_responses(
            self.cases,
            responses,
            {
                "repository_commit": "abc123",
                "model": "test",
                "model_version": "1",
                "evaluator_version": "test",
                "prompt_version": "test",
                "decoding_configuration": {},
                "executed_at": "2026-10-24T00:00:00+00:00",
            },
        )
        self.assertEqual(report["metrics"]["case_classification_accuracy"], 1.0)
        self.assertEqual(report["metrics"]["rule_precision"], 1.0)
        self.assertEqual(report["metrics"]["rule_recall"], 0.5)
        self.assertFalse(report["coverage"]["missing_cases"])
        self.assertIn("BTN-004", report["cases"][1]["rule_false_negatives"])
        self.assertIn("Mode: report-only", render_markdown(report))

    def test_invalid_response_requires_corrected_example(self):
        with self.assertRaisesRegex(EvalError, "corrected_example"):
            normalize_responses(
                [
                    {
                        "case_id": "content.eval.sample::invalid_case",
                        "valid": False,
                        "violations": ["BTN-001"],
                        "rationale": "Ambiguous.",
                        "corrected_example": None,
                        "unsupported_product_or_runtime_claim": False,
                    }
                ]
            )

    def test_duplicate_case_ids_fail(self):
        duplicate = FIXTURE.replace(
            "  - id: invalid_case", "  - id: valid_case"
        )
        (self.fixtures_dir / "sample-cases.yml").write_text(
            duplicate, encoding="utf-8"
        )
        with self.assertRaisesRegex(EvalError, "duplicate case id"):
            load_cases(self.fixtures_dir)

    def test_unexpected_response_is_reported(self):
        responses = normalize_responses(
            [
                {
                    "case_id": "unknown::case",
                    "valid": True,
                    "violations": [],
                    "rationale": "Unknown.",
                    "corrected_example": None,
                    "unsupported_product_or_runtime_claim": False,
                }
            ]
        )
        report = score_responses(
            self.cases,
            responses,
            {
                "repository_commit": "abc123",
                "model": "test",
                "model_version": "1",
                "evaluator_version": "test",
                "prompt_version": "test",
                "decoding_configuration": {},
                "executed_at": "2026-10-24T00:00:00+00:00",
            },
        )
        self.assertFalse(report["coverage"]["complete"])
        self.assertEqual(report["coverage"]["unexpected_cases"], ["unknown::case"])


if __name__ == "__main__":
    unittest.main()
