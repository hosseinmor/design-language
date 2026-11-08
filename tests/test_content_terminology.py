"""Regression tests for terminology source authority boundaries."""

import unittest

import tempfile
from pathlib import Path

from tooling.validators.check_content_terminology import layout_errors, naming_coverage_errors, validate


def authority_model():
    return {
        "meaning_owners": ["product_knowledge", "design_language"],
        "language_owner": "design_language",
        "design_language_owned_concept_kinds": [
            "communication_concept",
            "feature_family",
            "persona",
        ],
        "linked_product_source_role": "product_knowledge_reference",
        "unresolved_product_source": "unresolved",
        "not_applicable_product_source": "not_applicable",
        "migration_states": [
            "source_linked",
            "needs_product_knowledge_reference",
            "not_applicable",
        ],
    }


def linked_term():
    return {
        "id": "job_post",
        "concept_kind": "entity",
        "authority": {
            "meaning_owner": "product_knowledge",
            "language_owner": "design_language",
            "product_source": "product_source",
            "migration_state": "source_linked",
        },
        "production_alignment": {"state": "unverified"},
        "definition": {"source": "A referenced product definition."},
        "preferred": {"default": "آگهی شغلی"},
        "visibility": ["public"],
        "status": "stable",
        "evidence": ["product_source"],
    }


def valid_data():
    return {
        "schema_version": "0.3",
        "id": "content.foundation.terminology",
        "product": "jobvision",
        "language": "fa-IR",
        "authority_model": authority_model(),
        "sources": [
            {
                "id": "product_source",
                "role": "product_knowledge_reference",
            }
        ],
        "terms": [linked_term()],
        "decision_queue": [],
        "decision_log": [],
    }


class TerminologyAuthorityValidationTest(unittest.TestCase):
    def test_linked_product_source_is_valid(self):
        self.assertEqual(validate(valid_data()), [])

    def test_term_without_authority_fails(self):
        data = valid_data()
        del data["terms"][0]["authority"]
        errors = " ".join(validate(data))
        self.assertIn("authority must be a mapping", errors)

    def test_product_entity_cannot_claim_design_language_meaning(self):
        data = valid_data()
        authority = data["terms"][0]["authority"]
        authority["meaning_owner"] = "design_language"
        authority["product_source"] = "not_applicable"
        authority["migration_state"] = "not_applicable"
        errors = " ".join(validate(data))
        self.assertIn("cannot use `design_language`", errors)

    def test_language_owned_communication_concept_is_valid(self):
        data = valid_data()
        term = data["terms"][0]
        term["concept_kind"] = "communication_concept"
        term["authority"] = {
            "meaning_owner": "design_language",
            "language_owner": "design_language",
            "product_source": "not_applicable",
            "migration_state": "not_applicable",
        }
        term["evidence"] = []
        self.assertEqual(validate(data), [])

    def test_linked_source_requires_product_knowledge_role(self):
        data = valid_data()
        data["sources"][0]["role"] = "runtime_product_evidence"
        errors = " ".join(validate(data))
        self.assertIn("product_knowledge_reference", errors)

    def test_linked_source_must_be_evidence(self):
        data = valid_data()
        data["terms"][0]["evidence"] = []
        errors = " ".join(validate(data))
        self.assertIn("must also appear in evidence", errors)

    def test_unresolved_product_reference_is_explicit_and_valid(self):
        data = valid_data()
        term = data["terms"][0]
        term["id"] = "recruitment"
        term["authority"]["product_source"] = "unresolved"
        term["authority"]["migration_state"] = (
            "needs_product_knowledge_reference"
        )
        term["evidence"] = []
        self.assertEqual(validate(data), [])

    def test_unresolved_state_cannot_name_a_source(self):
        data = valid_data()
        term = data["terms"][0]
        term["authority"]["migration_state"] = (
            "needs_product_knowledge_reference"
        )
        errors = " ".join(validate(data))
        self.assertIn("must be `unresolved`", errors)


    def test_new_entry_cannot_wait_for_product_knowledge(self):
        data = valid_data()
        term = data["terms"][0]
        term["authority"]["product_source"] = "unresolved"
        term["authority"]["migration_state"] = "needs_product_knowledge_reference"
        term["evidence"] = []
        self.assertIn("cannot wait for a Product Knowledge reference", " ".join(validate(data)))


class ProductionAlignmentTest(unittest.TestCase):
    def test_alignment_is_required(self):
        data = valid_data()
        del data["terms"][0]["production_alignment"]
        self.assertIn("production_alignment.state", " ".join(validate(data)))

    def test_differs_needs_production_label_and_evidence(self):
        data = valid_data()
        data["terms"][0]["production_alignment"] = {"state": "differs"}
        errors = " ".join(validate(data))
        self.assertIn("requires `production_label`", errors)
        self.assertIn("requires a known `evidence` source", errors)

    def test_differs_with_label_and_source_is_valid(self):
        data = valid_data()
        data["terms"][0]["production_alignment"] = {
            "state": "differs",
            "production_label": "آگهی استخدام",
            "evidence": "product_source",
        }
        self.assertEqual(validate(data), [])

    def test_aligned_entry_keeps_no_production_details(self):
        data = valid_data()
        data["terms"][0]["production_alignment"] = {"state": "aligned", "production_label": "x"}
        self.assertIn("only differs alignment", " ".join(validate(data)))


class LayoutTest(unittest.TestCase):
    def shared(self):
        return {
            "id": "content.foundation.terminology",
            "schema_version": "0.7",
            "language": "fa-IR",
            "products": {"jobvision": "jobvision.yml"},
        }

    def product(self):
        return {
            "id": "content.foundation.terminology.jobvision",
            "product": "jobvision",
            "extends": "content.foundation.terminology",
            "schema_version": "0.7",
            "language": "fa-IR",
        }

    def test_valid_layout(self):
        self.assertEqual(layout_errors(self.shared(), {"jobvision": self.product()}), [])

    def test_shared_base_cannot_hold_terms(self):
        shared = self.shared()
        shared["terms"] = []
        self.assertIn("`terms` belongs to a product file", " ".join(layout_errors(shared, {})))

    def test_product_file_cannot_redefine_policy(self):
        product = self.product()
        product["policy"] = {}
        errors = " ".join(layout_errors(self.shared(), {"jobvision": product}))
        self.assertIn("`policy` belongs to shared.yml", errors)

    def test_product_file_must_name_its_product(self):
        product = self.product()
        product["product"] = "cando"
        errors = " ".join(layout_errors(self.shared(), {"jobvision": product}))
        self.assertIn("`product` must be `jobvision`", errors)


class TerminologyLanguageSchemaTest(unittest.TestCase):
    def test_design_language_forbidden_label_cannot_be_chosen(self):
        data = valid_data()
        data["terms"][0]["forbidden"] = [
            {"label": "آگهی شغلی", "scope": "concept", "source": "design_language"}
        ]
        errors = " ".join(validate(data))
        self.assertIn("both forbidden and a chosen label", errors)

    def test_snapshot_override_is_reported_not_failed(self):
        data = valid_data()
        data["terms"][0]["forbidden"] = [
            {
                "label": "آگهی شغلی",
                "scope": "entity_label",
                "source": "product_knowledge_snapshot",
            }
        ]
        overrides = []
        self.assertEqual(validate(data, overrides), [])
        self.assertEqual(len(overrides), 1)

    def test_forbidden_requires_known_scope(self):
        data = valid_data()
        data["terms"][0]["forbidden"] = [
            {"label": "وکنسی", "scope": "synonym", "source": "design_language"}
        ]
        self.assertIn("scope must be one of", " ".join(validate(data)))

    def test_unknown_term_key_fails(self):
        data = valid_data()
        data["terms"][0]["forbidden_as_synonym"] = ["وکنسی"]
        self.assertIn("unknown term keys", " ".join(validate(data)))

    def test_legacy_label_cannot_be_a_chosen_label(self):
        data = valid_data()
        data["terms"][0]["legacy_labels"] = [{"label": "آگهی شغلی"}]
        self.assertIn("still a chosen label", " ".join(validate(data)))

    def test_relation_target_must_be_known_or_registered(self):
        data = valid_data()
        data["terms"][0]["relations"] = {"distinct_from": ["job_category"]}
        self.assertIn("neither a term", " ".join(validate(data)))
        data["unregistered_concepts"] = ["job_category"]
        self.assertEqual(validate(data), [])

    def test_needs_decision_term_must_be_queued(self):
        data = valid_data()
        data["terms"][0]["status"] = "needs_decision"
        self.assertIn("must be referenced by decision_queue", " ".join(validate(data)))
        data["decision_queue"] = [
            {
                "id": "DEC-001",
                "term_ids": ["job_post"],
                "question": "q",
                "recommendation": "r",
                "impact": "low",
            }
        ]
        self.assertEqual(validate(data), [])



class NamingCoverageTests(unittest.TestCase):
    def test_repository_naming_cases_cover_blocking_rules(self):
        self.assertEqual(naming_coverage_errors(), [])

    def test_uncovered_blocking_rule_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            contract = Path(tmp) / "naming.yml"
            cases = Path(tmp) / "cases.yml"
            contract.write_text(
                "rules:\n  - {id: NAM-001, obligation: must}\n  - {id: NAM-002, obligation: should}\n",
                encoding="utf-8",
            )
            cases.write_text("cases: []\n", encoding="utf-8")
            errors = naming_coverage_errors(contract, cases)
        self.assertEqual(errors, ["naming cases do not cover blocking rules: NAM-001"])


if __name__ == "__main__":
    unittest.main()
