"""Regression tests for terminology source authority boundaries."""

import unittest

from tooling.validators.check_content_terminology import validate


def authority_model():
    return {
        "meaning_owner": "product_knowledge",
        "language_owner": "design_language",
        "linked_product_source_role": "product_knowledge_reference",
        "unresolved_product_source": "unresolved",
        "migration_states": [
            "source_linked",
            "needs_product_knowledge_reference",
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

    def test_design_language_cannot_claim_product_meaning(self):
        data = valid_data()
        data["terms"][0]["authority"]["meaning_owner"] = "design_language"
        errors = " ".join(validate(data))
        self.assertIn("authority.meaning_owner", errors)

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


if __name__ == "__main__":
    unittest.main()
