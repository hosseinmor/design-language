"""Regression tests for the shared content contract rule schema."""

import tempfile
import textwrap
import unittest
from pathlib import Path

import yaml

from tooling import content_rule_index
from tooling.validators import check_content_contracts
from tooling.validators.check_content_contracts import (
    validate_contract,
    validate_retired_owners,
)
from tooling.generate_content_rule_sections import expected_text
from tooling.validators.check_content_patterns import validate_notification_pattern

CONTRACT = textwrap.dedent(
    """\
    schema_version: "0.1"
    id: content.pattern.sample
    title: نمونه
    status: draft
    language: fa-IR
    rules:
      - id: SMP-001
        obligation: must
        dimension: clarity
        key: name_result
        statement: نتیجه را نام ببرید.
      - id: SMP-002
        obligation: must_not
        dimension: tone
        key: no_hype
        statement: هیجان اضافه نکنید.
    evaluation_source: cases.yml
    """
)
DOC = "# نمونه\n\n## قرارداد قطعی\n\n- متن قدیمی\n\n## ساختار\n\nمتن.\n"


class ContentContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        (self.dir / "cases.yml").write_text("cases: []\n", encoding="utf-8")
        self.yml = self.dir / "sample.yml"
        self.md = self.dir / "sample.md"

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, contract=CONTRACT, generate=True):
        self.yml.write_text(contract, encoding="utf-8")
        self.md.write_text(DOC, encoding="utf-8")
        if generate:
            self.md.write_text(expected_text(self.md, self.yml), encoding="utf-8")

    def test_valid_contract_passes(self):
        self.write()
        self.assertEqual(validate_contract(self.yml, {}, {}), [])

    def test_generated_section_keeps_following_sections(self):
        self.write()
        text = self.md.read_text(encoding="utf-8")
        self.assertIn("- `SMP-001` نتیجه را نام ببرید.", text)
        self.assertIn("## ساختار", text)
        self.assertNotIn("متن قدیمی", text)

    def test_stale_markdown_is_rejected(self):
        self.write(generate=False)
        errors = validate_contract(self.yml, {}, {})
        self.assertTrue(any("stale" in error for error in errors))

    def test_unknown_dimension_is_rejected(self):
        self.write(CONTRACT.replace("dimension: tone", "dimension: emoji"))
        errors = validate_contract(self.yml, {}, {})
        self.assertTrue(any("dimension `emoji`" in error for error in errors))

    def test_duplicate_rule_id_across_contracts_is_rejected(self):
        self.write()
        errors = validate_contract(self.yml, {}, {"SMP-001": "other.yml"})
        self.assertTrue(any("duplicate rule id" in error for error in errors))

    def test_mixed_prefixes_are_rejected(self):
        self.write(CONTRACT.replace("SMP-002", "XYZ-002"))
        errors = validate_contract(self.yml, {}, {})
        self.assertTrue(any("one id prefix" in error for error in errors))

    @staticmethod
    def retired_contract(block):
        return CONTRACT.replace("evaluation_source:", block + "evaluation_source:")

    RETIRED = textwrap.dedent(
        """\
        retired_rules:
          - id: SMP-003
            superseded_by: [SMP-001]
            reason: ادغام شد.
        """
    )

    def test_retired_rule_is_rendered_and_valid(self):
        self.write(self.retired_contract(self.RETIRED))
        retired = {}
        self.assertEqual(validate_contract(self.yml, {}, {}, retired), [])
        self.assertEqual(retired, {"SMP-003": ["SMP-001"]})
        self.assertIn("- `SMP-003` → `SMP-001`: ادغام شد.", self.md.read_text(encoding="utf-8"))

    def test_retired_id_cannot_stay_active(self):
        self.write(self.retired_contract(self.RETIRED.replace("SMP-003", "SMP-002")))
        errors = validate_contract(self.yml, {}, {})
        self.assertTrue(any("cannot also be an active rule" in e for e in errors))

    def test_retired_rule_requires_owner_and_reason(self):
        block = "retired_rules:\n  - id: SMP-003\n    superseded_by: []\n"
        self.write(self.retired_contract(block))
        errors = validate_contract(self.yml, {}, {})
        self.assertTrue(any("superseded_by" in e for e in errors))
        self.assertTrue(any("reason" in e for e in errors))

    def test_retired_owner_must_resolve(self):
        errors = validate_retired_owners(
            {"SMP-001": "a.yml"},
            {"SMP-003": ["SMP-009", "missing.doc"], "SMP-001": ["SMP-003"]},
            {"known.doc"},
        )
        self.assertTrue(any("unknown owner rule `SMP-009`" in e for e in errors))
        self.assertTrue(any("unknown owner document `missing.doc`" in e for e in errors))
        self.assertTrue(any("reused" in e for e in errors))
        self.assertTrue(any("itself retired" in e for e in errors))

    def test_eval_citing_retired_rule_is_rejected(self):
        evals = self.dir / "evals"
        evals.mkdir()
        (evals / "cases.yml").write_text(
            "cases:\n  - expected:\n      checked_rules: [SMP-003]\n", encoding="utf-8"
        )
        original = check_content_contracts.EVAL_DIR
        check_content_contracts.EVAL_DIR = evals
        try:
            errors = check_content_contracts.validate_eval_references(
                {"SMP-001": "a.yml"}, {"SMP-003": ["SMP-001"]}
            )
        finally:
            check_content_contracts.EVAL_DIR = original
        self.assertTrue(any("retired rule id `SMP-003`" in e for e in errors))


class InheritedRuleTests(unittest.TestCase):
    def test_component_inherits_pattern_and_voice_rules(self):
        inherited = content_rule_index.inherited_rule_ids("content.component.text-input")
        self.assertIn("INS-014", inherited)
        self.assertIn("ERR-003", inherited)
        self.assertIn("VOICE-007", inherited)
        self.assertNotIn("TXT-001", inherited)

    def test_retired_rules_are_not_inherited(self):
        inherited = content_rule_index.inherited_rule_ids("content.component.notification")
        self.assertIn("NTF-005", inherited)
        self.assertNotIn("NTF-012", inherited)


class NotificationOwnershipTests(unittest.TestCase):
    def test_presentation_model_is_rejected(self):
        path = content_rule_index.CONTENT / "patterns" / "notifications.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["presentation_model"] = {"toast": {"use_when": "x"}}
        data.pop("presentation_owner")
        errors, _ = validate_notification_pattern(data, set())
        self.assertTrue(any("`presentation_model` belongs to" in e for e in errors))
        self.assertTrue(any("`presentation_owner` must be" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
