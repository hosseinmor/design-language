#!/usr/bin/env python3
"""Deterministic structural regression checks for canonical accessibility knowledge.

This gate intentionally validates repository invariants that can be checked reliably
without pretending to replace manual standards, component, flow, keyboard, screen-
reader, or complete-process review. The manual gate remains in
accessibility/testing.md.
"""

from __future__ import annotations

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
ACCESSIBILITY_DIR = ROOT / "accessibility"
OWNER = "Design System team"

EXPECTED_ACCESSIBILITY_DOCS = {
    "color-and-contrast.md": "design-system.accessibility.color-and-contrast",
    "component-accessibility-authoring-contract.md": "design-system.accessibility.component-authoring-contract",
    "conformance-and-policy.md": "design-system.accessibility.conformance-and-policy",
    "content.md": "design-system.accessibility.content",
    "core.md": "design-system.accessibility.core",
    "dynamic-content-and-feedback.md": "design-system.accessibility.dynamic-content-and-feedback",
    "focus-management.md": "design-system.accessibility.focus-management",
    "forms.md": "design-system.accessibility.forms",
    "images-icons-and-media.md": "design-system.accessibility.images-icons-and-media",
    "keyboard-navigation.md": "design-system.accessibility.keyboard-navigation",
    "motion.md": "design-system.accessibility.motion",
    "pointer-touch-and-gestures.md": "design-system.accessibility.pointer-touch-and-gestures",
    "responsive-and-zoom.md": "design-system.accessibility.responsive-and-zoom",
    "router.md": "design-system.accessibility.router",
    "screen-reader-semantics.md": "design-system.accessibility.screen-reader-semantics",
    "structure-and-navigation.md": "design-system.accessibility.structure-and-navigation",
    "tables-and-data-visualization.md": "design-system.accessibility.tables-and-data-visualization",
    "testing.md": "design-system.accessibility.testing",
}

GOVERNANCE_DOCS = [
    ROOT / "governance/ownership.md",
    ROOT / "governance/documentation-maintenance.md",
    ROOT / "governance/change-process.md",
]


def read_markdown(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    _, raw_frontmatter, body = text.split("---", 2)
    data = yaml.safe_load(raw_frontmatter) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: frontmatter must be a mapping")
    return data, body


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    # Canonical operational corpus: exact identity + maintenance metadata.
    # Ownership is resolved by the collection default in governance/ownership.md
    # unless a document explicitly overrides it.
    for filename, expected_id in EXPECTED_ACCESSIBILITY_DOCS.items():
        path = ACCESSIBILITY_DIR / filename
        require(path.exists(), f"missing operational accessibility doc: {path.relative_to(ROOT)}", errors)
        if not path.exists():
            continue

        try:
            meta, _ = read_markdown(path)
        except Exception as exc:  # noqa: BLE001 - report all validation failures together
            errors.append(str(exc))
            continue

        rel = path.relative_to(ROOT)
        require(meta.get("id") == expected_id, f"{rel}: expected id {expected_id!r}, got {meta.get('id')!r}", errors)
        require(meta.get("knowledge_state") == "canonical", f"{rel}: knowledge_state must remain canonical", errors)
        require(meta.get("document_maturity") in {"reviewed", "stable"}, f"{rel}: document_maturity must remain reviewed/stable", errors)
        explicit_owner = meta.get("owner")
        require(
            explicit_owner in (None, "", OWNER),
            f"{rel}: explicit owner must be {OWNER!r} or omitted to inherit the collection owner",
            errors,
        )

    # Governance that makes ownership and change gates operational.
    for path in GOVERNANCE_DOCS:
        require(path.exists(), f"missing governance doc: {path.relative_to(ROOT)}", errors)
        if not path.exists():
            continue
        meta, _ = read_markdown(path)
        rel = path.relative_to(ROOT)
        require(meta.get("knowledge_state") == "canonical", f"{rel}: knowledge_state must be canonical", errors)
        require(meta.get("document_maturity") in {"reviewed", "stable"}, f"{rel}: document_maturity must be reviewed/stable", errors)
        require(meta.get("owner") == OWNER, f"{rel}: owner must be {OWNER!r}", errors)

    # Production retrieval integration must explicitly invoke the accessibility router.
    design_start = (ROOT / "ai/router.md").read_text(encoding="utf-8")
    require(
        "accessibility/router.md" in design_start,
        "ai/router.md must explicitly route web design through accessibility/router.md",
        errors,
    )

    # Stable ownership markers for the WCAG 2.2 gaps closed in Phase 3.
    structure = (ACCESSIBILITY_DIR / "structure-and-navigation.md").read_text(encoding="utf-8")
    pointer = (ACCESSIBILITY_DIR / "pointer-touch-and-gestures.md").read_text(encoding="utf-8")
    testing = (ACCESSIBILITY_DIR / "testing.md").read_text(encoding="utf-8")
    router = (ACCESSIBILITY_DIR / "router.md").read_text(encoding="utf-8")

    for marker in ("3.2.1", "3.2.2", "3.2.6"):
        require(marker in structure, f"structure-and-navigation.md must retain WCAG {marker} ownership", errors)
        require(marker in testing, f"testing.md must retain WCAG {marker} regression coverage", errors)
    require("2.5.4" in pointer, "pointer-touch-and-gestures.md must retain WCAG 2.5.4 Motion Actuation ownership", errors)
    require("2.5.4" in testing, "testing.md must retain WCAG 2.5.4 regression coverage", errors)
    require("device-motion input" in router and "Consistent Help" in router, "accessibility/router.md must retain Motion Actuation and Consistent Help triggers", errors)

    # Keep the repository component name deterministic.
    require("Button, Dialog, Combobox" not in router, "accessibility/router.md must use Modal, not Dialog, as the DS component example", errors)
    require("Button, Modal, Combobox" in router, "accessibility/router.md must retain Modal as the DS component example", errors)

    if errors:
        print("Accessibility knowledge regression gate: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Accessibility knowledge regression gate: PASS")
    print("Manual behavior/standards regression remains required by accessibility/testing.md when triggered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
