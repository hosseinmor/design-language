"""Negative regression tests for AI routing and shared stewardship."""

import tempfile
import unittest
from pathlib import Path

from tooling.generate_manifest import infer_owner
from tooling.validators.check_ai_governance import (
    expand_locations, validate_owners, validate_router,
)

TICK = chr(96)


class RouterValidationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "ai").mkdir()
        (self.root / "governance").mkdir()
        (self.root / "governance" / "ownership.md").write_text("Valid")

    def tearDown(self):
        self.temp.cleanup()

    def router(self, start=None, verify=None):
        if start is None:
            start = TICK + "ai/" + TICK
        if verify is None:
            verify = TICK + "governance/ownership.md" + TICK
        return (
            "# AI router\n\n"
            "| Question | Start here | Verify exact facts in |\n"
            "|---|---|---|\n"
            f"| Governance | {start} | {verify} |\n"
        )

    def validate(self, content):
        return validate_router(content, self.root)

    def test_valid_route(self):
        self.assertEqual(self.validate(self.router()), [])

    def test_missing_start_path(self):
        errors = self.validate(self.router(start=TICK + "missing/" + TICK))
        self.assertIn("Missing AI router destination", " ".join(errors))

    def test_unquoted_start_path(self):
        errors = self.validate(self.router(start="ai/"))
        self.assertIn("backtick-quoted", " ".join(errors))

    def test_empty_start_path(self):
        self.assertIn("Start here", " ".join(self.validate(self.router(start=""))))

    def test_missing_verify_file_inside_backticks(self):
        errors = self.validate(self.router(verify=TICK + "governance/missing.md" + TICK))
        self.assertIn("governance/missing.md", " ".join(errors))

    def test_missing_unquoted_verify_file(self):
        self.assertIn("governance/missing.md",
                      " ".join(self.validate(self.router(verify="See governance/missing.md"))))

    def test_missing_markdown_link_verify_file(self):
        errors = self.validate(self.router(verify="[Policy](governance/missing.md)"))
        self.assertIn("governance/missing.md", " ".join(errors))

    def test_empty_verify_column(self):
        self.assertIn("lacks verification guidance",
                      " ".join(self.validate(self.router(verify=""))))

    def test_extra_table_column(self):
        bad = self.router().replace("| Governance |", "| Governance | extra |")
        self.assertIn("exactly 3 columns", " ".join(self.validate(bad)))

    def test_missing_table(self):
        self.assertIn("missing the three-column routing table",
                      " ".join(self.validate("# No router table")))

    def test_brace_alternatives_expand(self):
        self.assertEqual(
            expand_locations("design-system/tokens/{color,spacing}/"),
            ["design-system/tokens/color/", "design-system/tokens/spacing/"],
        )

    def test_path_escape(self):
        self.assertIn(
            "escapes repository",
            " ".join(self.validate(self.router(start=TICK + "../" + TICK))),
        )


class OwnershipValidationTest(unittest.TestCase):
    def test_missing_shared_draft_steward_fails(self):
        data = {"documents": [{
            "id": "draft-a", "kind": "design-system-component",
            "path": "design-system/components/a.md", "status": "draft",
            "owner": None,
        }]}
        self.assertIn("draft-a", " ".join(validate_owners(data)))

    def test_missing_shared_reviewed_steward_fails(self):
        data = {"documents": [{
            "id": "router", "kind": "design-language-ai-routing",
            "path": "ai/router.md", "status": "reviewed", "owner": None,
        }]}
        self.assertIn("router", " ".join(validate_owners(data)))

    def test_other_collection_may_have_no_default(self):
        data = {"documents": [{
            "id": "content", "kind": "content-content-pattern",
            "path": "foundations/content/patterns/example.md",
            "owner": None,
        }]}
        self.assertEqual(validate_owners(data), [])

    def test_explicit_owner_precedence(self):
        self.assertEqual(
            infer_owner("design-system/components/a.md", {
                "collection": "design-system", "document_maturity": "draft",
                "owner": "Component maintainers",
            }),
            "Component maintainers",
        )

    def test_shared_scaffold_inherits_maintainer_not_approval(self):
        self.assertEqual(
            infer_owner("design-system/components/a.md", {
                "collection": "design-system", "document_maturity": "scaffold",
            }),
            "Design System team",
        )

    def test_other_collection_keeps_independent_ownership(self):
        self.assertIsNone(
            infer_owner("foundations/content/a.md", {
                "collection": "content", "document_maturity": "reviewed",
            }),
        )

    def test_accessibility_always_has_collection_steward(self):
        self.assertEqual(
            infer_owner("accessibility/router.md", {
                "collection": "content", "document_maturity": "draft",
            }),
            "Design System team",
        )


if __name__ == "__main__":
    unittest.main()
