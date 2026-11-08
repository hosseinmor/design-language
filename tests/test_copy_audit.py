"""Regression tests for the copy audit checker and validator."""

import copy
import unittest

from tooling.audit.run_copy_audit import (
    EvalError,
    check_item,
    load_contract,
    priority,
    summarize,
    validate_item,
)
from tooling.validators.check_copy_audit import validate_case, validate_contract
from tooling.validators.check_copy_briefs import Context

CTX = Context.from_repository()
CONTRACT = load_contract()
RULES = {r["id"] for r in CONTRACT["rules"]}


def item(**overrides):
    value = {
        "id": "sample",
        "observed_text": "۳ اپلای جدید دارید.",
        "location": "inv-1",
        "captured_on": "2026-11-01",
        "product": "jobvision",
        "audience": ["employer_actor"],
        "surface": "public",
        "contract": "content.pattern.notifications",
        "state": "info",
        "slot": "message",
        "concepts": ["job_application"],
    }
    value.update(overrides)
    return value


class CheckerTests(unittest.TestCase):
    def test_forbidden_label_becomes_finding(self):
        finding = check_item(item(), CTX, CONTRACT)
        self.assertEqual(finding["status"], "finding")
        self.assertEqual(finding["rule_ids"], ["VOICE-007"])
        self.assertEqual(finding["label_findings"][0]["approved_labels"][0], "درخواست شغلی")

    def test_approved_label_masks_forbidden_short_form(self):
        finding = check_item(item(observed_text="درخواست شغلی ارسال شد."), CTX, CONTRACT)
        self.assertEqual(finding["status"], "no_issue")

    def test_short_approved_label_does_not_hide_forbidden_phrase(self):
        value = item(
            observed_text="۵۹٬۷۴۳ آگهی استخدام در ۳۹۱ شهر",
            audience=["jobseeker"],
            concepts=["job_post"],
        )
        finding = check_item(value, CTX, CONTRACT)
        self.assertEqual(finding["status"], "finding")
        self.assertEqual(finding["label_findings"][0]["label"], "آگهی استخدام")

    def test_missing_context_is_not_judged(self):
        value = item()
        del value["contract"]
        finding = check_item(value, CTX, CONTRACT)
        self.assertEqual((finding["status"], finding["context_gaps"]), ("needs_context", ["contract"]))

    def test_url_location_is_rejected(self):
        self.assertTrue(validate_item(item(location="https://example.com/page"), CONTRACT))

    def test_priority_uses_lowest_rank_and_surface(self):
        model = CONTRACT["priority_model"]
        self.assertEqual(priority(["tone", "product_truth"], "public", model), "P1")
        self.assertEqual(priority(["tone"], "admin", model), "P4")

    def test_semantic_violation_raises_priority(self):
        findings = [check_item(item(), CTX, CONTRACT)]
        report = summarize(findings, [{"case_id": "sample", "violations": ["NTF-005"]}], CONTRACT)
        self.assertEqual(report["findings"][0]["priority"], "P1")
        self.assertIn("NTF-005", report["findings"][0]["rule_ids"])

    def test_finding_without_rule_or_gap_is_rejected(self):
        broken = {"item_id": "x", "location": "inv", "status": "finding", "rule_ids": []}
        with self.assertRaises(EvalError):
            summarize([broken], [], CONTRACT)


class ValidatorTests(unittest.TestCase):
    def test_contract_is_valid(self):
        self.assertEqual(validate_contract(CONTRACT, CTX), [])

    def test_contract_must_rank_every_dimension(self):
        broken = copy.deepcopy(CONTRACT)
        del broken["priority_model"]["dimension_rank"]["tone"]
        self.assertTrue(validate_contract(broken, CTX))

    def test_case_mismatch_is_reported(self):
        case = {
            "id": "c",
            "item": item(),
            "expected": {"checked_rules": ["AUD-001"], "status": "no_issue"},
        }
        errors, _ = validate_case(case, CTX, CONTRACT, RULES)
        self.assertTrue(any("status" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
