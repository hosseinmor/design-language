"""Regression tests for the shared content contract rule schema."""

import tempfile
import textwrap
import unittest
from pathlib import Path

from tooling.validators.check_content_contracts import validate_contract
from tooling.generate_content_rule_sections import expected_text

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


if __name__ == "__main__":
    unittest.main()
