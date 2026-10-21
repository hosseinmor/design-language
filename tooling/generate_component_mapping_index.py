#!/usr/bin/env python3
"""Generate or check an AI-friendly line-ranged component mapping index."""
from __future__ import annotations
import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "integrations" / "component-mapping.md"
INDEX = ROOT / "integrations" / "component-mapping-index.md"
BEGIN = "<!-- BEGIN GENERATED COMPONENT MAPPING SECTIONS -->"
END = "<!-- END GENERATED COMPONENT MAPPING SECTIONS -->"
HEADING = re.compile(r"^### (.+)$")
SECTION_BOUNDARY = re.compile(r"^#{2,3} ")

def mapping_sections(source: str) -> list[tuple[str, int, int]]:
    """Return (exact heading, first line, last line), 1-based, inclusive."""
    lines = source.splitlines()
    starts = [(i, m.group(1)) for i, line in enumerate(lines) if (m := HEADING.fullmatch(line))]
    if not starts:
        raise ValueError("No level-three mapping headings found.")
    names = [name for _, name in starts]
    if len(set(names)) != len(names):
        raise ValueError("Duplicate level-three mapping headings.")
    sections = []
    for start_index, name in starts:
        stop = start_index + 1
        while stop < len(lines) and not SECTION_BOUNDARY.match(lines[stop]):
            stop += 1
        while stop > start_index + 1 and not lines[stop - 1].strip():
            stop -= 1
        sections.append((name, start_index + 1, stop))
    return sections

def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace(chr(96), "\\" + chr(96))

def generated_table(source: str) -> str:
    rows = [
        "| Component / evidence section | Source lines (inclusive) | Exact heading |",
        "|---|---:|---|",
    ]
    for name, first, last in mapping_sections(source):
        escaped = escape_cell(name)
        rows.append(f"| {escaped} | {first}–{last} | ### {escaped} |")
    return "\n".join(rows)

def expected_index(existing: str, source: str) -> str:
    if existing.count(BEGIN) != 1 or existing.count(END) != 1:
        raise ValueError("Index requires exactly one pair of generated-section markers.")
    before, remainder = existing.split(BEGIN, 1)
    _, after = remainder.split(END, 1)
    return f"{before}{BEGIN}\n{generated_table(source)}\n{END}{after}"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("generate", "check"))
    args = parser.parse_args()
    try:
        source = MAPPING.read_text(encoding="utf-8")
        current = INDEX.read_text(encoding="utf-8")
        expected = expected_index(current, source)
    except (OSError, ValueError) as exc:
        print(f"ERROR component mapping index: {exc}", file=sys.stderr)
        return 1
    if args.action == "generate":
        if current != expected:
            INDEX.write_text(expected, encoding="utf-8")
        print("Component mapping index generated.")
        return 0
    if current != expected:
        print("ERROR component mapping index is stale. Run: python tooling/generate_component_mapping_index.py generate", file=sys.stderr)
        for line in list(difflib.unified_diff(current.splitlines(keepends=True), expected.splitlines(keepends=True)))[:60]:
            sys.stderr.write(line)
        return 1
    print(f"Validated {len(mapping_sections(source))} component mapping headings and inclusive line ranges.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
