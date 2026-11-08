"""Regression tests for copy briefs and the report-only generation evaluator."""

import copy
import unittest

from tooling.evals.run_content_generation_eval import EvalError, check_case, normalize
from tooling.validators.check_copy_briefs import Context, anatomy_roles, validate_brief, validate_case

CTX = Context.from_repository()


def brief(**overrides):
    value = {
        "id": "delete_job_post",
        "product": "jobvision",
        "audience": ["employer_actor"],
        "surface": "public",
        "contract": "content.pattern.confirmation",
        "states": [{"id": "destructive", "slots": ["title", "primary_action", "safe_exit"]}],
        "concepts": ["job_post"],
        "product_facts": [
            {"id": "permanent", "statement": "حذف دائمی است.", "status": "verified", "source": "pk_jobvision_jobpost_overview"}
        ],
    }
    value.update(overrides)
    return value


def case(**expected_overrides):
    expected = {
        "outcome": "copy",
        "checked_rules": ["BRF-001", "CNF-005"],
        "required_slots": {"destructive": ["title", "primary_action"]},
        "must_use_labels": [{"concept": "job_post", "label": "آگهی"}],
        "forbidden_labels": [{"concept": "job_post", "label": "وکنسی"}],
    }
    expected.update(expected_overrides)
    return {"id": "sample", "brief": brief(), "expected": expected}


class BriefTests(unittest.TestCase):
    def errors(self, value, fixture=False):
        return validate_brief(value, CTX, "brief", allow_fixture_source=fixture)

    def test_valid_brief(self):
        self.assertEqual(self.errors(brief()), [])

    def test_slot_outside_anatomy_is_rejected(self):
        value = brief(states=[{"id": "s", "slots": ["title", "primary_action", "safe_exit", "headline"]}])
        self.assertTrue(any("not anatomy roles" in e for e in self.errors(value)))

    def test_missing_required_role_is_rejected(self):
        value = brief(states=[{"id": "s", "slots": ["title", "primary_action"]}])
        self.assertTrue(any("required anatomy roles" in e for e in self.errors(value)))

    def test_product_without_terminology_cannot_borrow_terms(self):
        value = brief(product="cando", audience=["operator"], product_facts=[])
        errors = self.errors(value)
        self.assertTrue(any("has no terminology layer" in e for e in errors))
        pk = {"kind": "product_knowledge", "product": "cando", "page": "p", "label": "x"}
        self.assertEqual(self.errors(brief(product="cando", audience=["operator"], concepts=[pk], product_facts=[])), [])

    def test_sources_are_scoped_to_the_brief_product(self):
        value = brief(product="cando", audience=["operator"], concepts=[])
        self.assertTrue(any("not a registered terminology source" in e for e in self.errors(value)))

    def test_audience_must_be_a_role_term(self):
        self.assertTrue(any("audience" in e for e in self.errors(brief(audience=["job_post"]))))

    def test_verified_fact_cannot_exceed_draft_source(self):
        fact = {"id": "f", "statement": "x", "status": "verified", "source": "source_glossary"}
        self.assertTrue(any("exceeds source" in e for e in self.errors(brief(product_facts=[fact]))))

    def test_unknown_fact_needs_question_and_no_source(self):
        fact = {"id": "f", "statement": "x", "status": "unknown", "source": "source_glossary"}
        errors = self.errors(brief(product_facts=[fact]))
        self.assertTrue(any("must not cite a source" in e for e in errors))
        self.assertTrue(any("requires a question" in e for e in errors))

    def test_fixture_source_only_in_fixtures(self):
        fact = {"id": "f", "statement": "x", "status": "draft", "source": "eval_fixture"}
        self.assertTrue(self.errors(brief(product_facts=[fact])))
        self.assertEqual(self.errors(brief(product_facts=[fact]), fixture=True), [])

    def test_product_knowledge_page_source(self):
        page = {"kind": "product_knowledge", "product": "jobvision", "page": "jobpost-overview", "state": "draft"}
        verified = {"id": "f", "statement": "x", "status": "verified", "source": page}
        self.assertTrue(any("exceeds source maturity" in e for e in self.errors(brief(product_facts=[verified]))))
        draft = {**verified, "status": "draft"}
        self.assertEqual(self.errors(brief(product_facts=[draft])), [])

    def test_product_knowledge_of_other_product_is_rejected(self):
        page = {"kind": "product_knowledge", "product": "cando", "page": "p", "state": "verified"}
        fact = {"id": "f", "statement": "x", "status": "verified", "source": page}
        self.assertTrue(any("cannot support" in e for e in self.errors(brief(product_facts=[fact]))))

    def test_prd_source_needs_accepted_decision_for_verified(self):
        prd = {"kind": "prd", "ref": "JV-1405081200", "decision": "proposed"}
        fact = {"id": "f", "statement": "x", "status": "verified", "source": prd}
        self.assertTrue(any("exceeds source maturity" in e for e in self.errors(brief(product_facts=[fact]))))
        accepted = {**fact, "source": {**prd, "decision": "accepted"}}
        self.assertEqual(self.errors(brief(product_facts=[accepted])), [])

    def test_unknown_source_kind_is_rejected(self):
        fact = {"id": "f", "statement": "x", "status": "draft", "source": {"kind": "slack"}}
        self.assertTrue(any("unknown source kind" in e for e in self.errors(brief(product_facts=[fact]))))

    def test_product_knowledge_concept_must_match_product(self):
        concept = {"kind": "product_knowledge", "product": "cando", "page": "p", "label": "x"}
        self.assertTrue(any("cannot label" in e for e in self.errors(brief(concepts=[concept]))))

    def test_new_concept_needs_prd_source_and_no_entry(self):
        existing = {"kind": "new_concept", "id": "job_post", "source": {"kind": "prd", "ref": "r", "decision": "accepted"}}
        self.assertTrue(any("already has a terminology entry" in e for e in self.errors(brief(concepts=[existing]))))
        no_prd = {"kind": "new_concept", "id": "video_call", "source": "source_glossary"}
        self.assertTrue(any("must be a prd reference" in e for e in self.errors(brief(concepts=[no_prd]))))

    def test_anatomy_roles_flatten_nested_lists(self):
        roles, required = anatomy_roles({"required": ["a"], "output": {"conditional": ["b"]}})
        self.assertEqual((roles, required), ({"a", "b"}, {"a"}))


class CaseTests(unittest.TestCase):
    def errors(self, value):
        return validate_case(value, CTX, "case")[0]

    def test_valid_case(self):
        self.assertEqual(self.errors(case()), [])

    def test_product_without_layer_must_block(self):
        value = case()
        value["brief"]["product"] = "cando"
        self.assertTrue(any("contradicts product layer" in e for e in self.errors(value)))

    def test_questions_must_match_unknown_facts(self):
        value = case()
        value["brief"]["product_facts"].append(
            {"id": "cost", "statement": "x", "status": "unknown", "question": "?"}
        )
        self.assertTrue(any("required_questions" in e for e in self.errors(value)))

    def test_labels_must_come_from_terminology(self):
        value = case(forbidden_labels=[{"concept": "job_post", "label": "پست"}])
        self.assertTrue(any("not a terminology forbidden label" in e for e in self.errors(value)))

    def test_new_concept_must_be_a_draft_dependency(self):
        value = case()
        value["brief"]["concepts"].append(
            {"kind": "new_concept", "id": "video_call", "source": {"kind": "prd", "ref": "r", "decision": "accepted"}}
        )
        self.assertTrue(any("draft_dependencies" in e for e in self.errors(value)))

    def test_checked_rules_must_belong_to_contract(self):
        self.assertTrue(any("checked_rules" in e for e in self.errors(case(checked_rules=["ERR-001"]))))


class ScoringTests(unittest.TestCase):
    def response(self, **overrides):
        value = {
            "case_id": "sample",
            "brief_id": "delete_job_post",
            "outcome": "copy",
            "copy": {"destructive": {"title": "آگهی را حذف می‌کنید؟", "primary_action": "حذف آگهی"}},
            "checked_rules": ["BRF-001", "CNF-005"],
        }
        value.update(overrides)
        return normalize(value)

    def test_good_response_passes(self):
        self.assertEqual(check_case(case(), self.response()), [])

    def test_forbidden_label_is_reported(self):
        bad = self.response(copy={"destructive": {"title": "وکنسی را حذف می‌کنید؟", "primary_action": "حذف آگهی"}})
        self.assertTrue(any("forbidden label" in f for f in check_case(case(), bad)))

    def test_filled_empty_slot_and_missing_question_are_reported(self):
        expected = case(empty_slots={"destructive": ["safe_exit"]}, required_questions=["cost"])
        value = copy.deepcopy(self.response())
        value["copy"]["destructive"]["safe_exit"] = "انصراف"
        failures = check_case(expected, value)
        self.assertTrue(any("should stay empty" in f for f in failures))
        self.assertTrue(any("open_questions missing" in f for f in failures))

    def test_blocked_response_needs_reason(self):
        with self.assertRaises(EvalError):
            normalize({"case_id": "x", "outcome": "blocked", "checked_rules": []})


if __name__ == "__main__":
    unittest.main()
