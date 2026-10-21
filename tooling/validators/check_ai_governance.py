#!/usr/bin/env python3
"""Validate AI router row coverage and shared Design Language stewardship.

The manifest generator owns schema, related IDs and freshness. This script
checks every initial route row, file references in the verification column,
and the existence of a steward independently from Manifest maturity status.
"""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTER = ROOT / "ai" / "router.md"
MANIFEST = ROOT / "registry" / "manifest.generated.json"
ROUTER_HEADER = ["Question", "Start here", "Verify exact facts in"]
INLINE_START = re.compile(r"\s*" + chr(96) + r"([^" + chr(96) + r"]+)" + chr(96) + r"\s*\Z")
VERIFICATION_FILE = re.compile(
    r"(?<![\w.-])(?:[\w.-]+/)+[\w.-]+\.md(?:#[\w-]+)?"
)
ALTERNATIVES = re.compile(r"\{([^{}]+)\}")


def expand_locations(raw: str) -> list[str]:
    match = ALTERNATIVES.search(raw)
    if match is None:
        return [raw]
    options = [option.strip() for option in match.group(1).split(",")]
    if any(not option for option in options):
        raise ValueError(f"Malformed route alternatives: {raw}")
    return list(itertools.chain.from_iterable(
        expand_locations(raw[:match.start()] + option + raw[match.end():])
        for option in options
    ))


def check_path(root: Path, raw: str) -> str | None:
    location = raw.split("#", 1)[0]
    target = (root / location).resolve()
    if not target.is_relative_to(root.resolve()):
        return f"Route escapes repository: {raw}"
    if not target.exists():
        return f"Missing AI router destination: {raw}"
    return None


def validate_router(markdown: str, root: Path) -> list[str]:
    errors: list[str] = []
    table_found = False
    in_table = False
    row_count = 0
    for line_number, line in enumerate(markdown.splitlines(), start=1):
        if not in_table:
            if line.startswith("|") and [c.strip() for c in line.strip().strip("|").split("|")] == ROUTER_HEADER:
                table_found = True
                in_table = True
            continue
        if not line.startswith("|"):
            break

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        if len(cells) != 3:
            errors.append(f"Router row at line {line_number} must have exactly 3 columns.")
            continue
        question, start, verify = cells
        row_count += 1
        if not question:
            errors.append(f"Router row at line {line_number} lacks a question.")
        if not verify:
            errors.append(f"Router row at line {line_number} lacks verification guidance.")

        match = INLINE_START.fullmatch(start)
        if not match:
            errors.append(
                f"Router row at line {line_number} lacks one backtick-quoted 'Start here' path."
            )
        else:
            try:
                destinations = expand_locations(match.group(1))
            except ValueError as exc:
                errors.append(str(exc))
                destinations = []
            for destination in destinations:
                error = check_path(root, destination)
                if error:
                    errors.append(f"Line {line_number}: {error}")

        # Match backtick-quoted, Markdown-linked and unquoted file references.
        # Provider names such as Code/Storybook remain natural language.
        for destination in VERIFICATION_FILE.findall(verify):
            error = check_path(root, destination)
            if error:
                errors.append(f"Line {line_number}: {error}")

    if not table_found:
        errors.append("AI router is missing the three-column routing table.")
    elif not row_count:
        errors.append("AI router must contain at least one non-header route.")
    return errors


def validate_owners(manifest: dict) -> list[str]:
    errors: list[str] = []
    documents = manifest.get("documents", [])
    if not documents:
        return ["Registry Manifest has no indexed documents."]
    for doc in documents:
        kind = doc.get("kind", "")
        is_shared = kind.startswith(("design-system-", "design-language-"))
        is_accessibility = doc.get("path", "").startswith("accessibility/")
        if (is_shared or is_accessibility) and not doc.get("owner"):
            errors.append(
                f"Shared document lacks effective steward: {doc.get('id', '<unknown>')}"
            )
    return errors


def main() -> int:
    errors = validate_router(ROUTER.read_text(encoding="utf-8"), ROOT)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors.extend(validate_owners(manifest))
    if errors:
        for error in errors:
            print("ERROR " + error)
        print(f"{len(errors)} AI/Governance validation error(s).")
        return 1
    shared = sum(
        doc.get("kind", "").startswith(("design-system-", "design-language-"))
        or doc.get("path", "").startswith("accessibility/")
        for doc in manifest["documents"]
    )
    print(f"Validated router coverage and {shared} shared document stewards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
