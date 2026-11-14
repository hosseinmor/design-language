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
        "content_type": "interface",
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

    def test_marketing_finding_has_owner_and_no_rewrite(self):
        value = item(content_type="marketing", observed_text="۵۹٬۷۴۳ آگهی استخدام در ۳۹۱ شهر", concepts=["job_post"])
        for key in ("contract", "state", "slot"):
            del value[key]
        finding = check_item(value, CTX, CONTRACT)
        self.assertEqual((finding["status"], finding["decision_owner"]), ("finding", "marketing"))
        self.assertNotIn("rewrite_brief", finding)

    def test_interface_still_needs_its_slot_context(self):
        value = item()
        del value["slot"]
        self.assertEqual(check_item(value, CTX, CONTRACT)["context_gaps"], ["slot"])

    def test_marketing_ignores_rules_outside_its_type(self):
        value = item(content_type="marketing", observed_text="رزومهٔ خود را کامل کنید.", concepts=[])
        findings = [check_item(value, CTX, CONTRACT)]
        report = summarize(findings, [{"case_id": "sample", "violations": ["NTF-005", "VOICE-004"]}], CONTRACT)
        self.assertEqual(report["findings"][0]["status"], "no_issue")

    def test_unsupported_claim_goes_to_product_manager(self):
        value = item(content_type="marketing", observed_text="هوشمندترین سیستم پیشنهاد شغل", concepts=[])
        findings = [check_item(value, CTX, CONTRACT)]
        response = {"case_id": "sample", "violations": ["VOICE-003"], "unsupported_product_or_runtime_claim": True}
        finding = summarize(findings, [response], CONTRACT)["findings"][0]
        self.assertEqual((finding["status"], finding["decision_owner"], finding["priority"]), ("finding", "product_manager", "P1"))

    def test_interface_claim_also_goes_to_product_manager(self):
        findings = [check_item(item(), CTX, CONTRACT)]
        finding = summarize(findings, [{"case_id": "sample", "violations": ["VOICE-005"]}], CONTRACT)["findings"][0]
        self.assertEqual(finding["decision_owner"], "product_manager")

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

    def test_rewrite_type_must_judge_every_rule(self):
        broken = copy.deepcopy(CONTRACT)
        broken["content_types"]["interface"]["judged_rules"] = ["VOICE-007"]
        self.assertTrue(any("every rule" in e for e in validate_contract(broken, CTX)))

    def test_judged_rule_must_exist(self):
        broken = copy.deepcopy(CONTRACT)
        broken["content_types"]["marketing"]["judged_rules"].append("VOICE-999")
        self.assertTrue(any("VOICE-999" in e for e in validate_contract(broken, CTX)))

    def test_content_type_is_required_context(self):
        broken = copy.deepcopy(CONTRACT)
        broken["audit_item_schema"]["context"].remove("content_type")
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
