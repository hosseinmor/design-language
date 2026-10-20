#!/usr/bin/env python3
"""Validate relative file links in Markdown without accessing the network."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "codex:")
SKIP_PARTS = {".git"}


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    )


def main() -> int:
    errors: list[str] = []
    checked = 0
    for document in markdown_files():
        text = document.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            if not raw_target or raw_target.startswith(SKIP_PREFIXES):
                continue
            target_without_anchor = unquote(raw_target.split("#", 1)[0])
            if not target_without_anchor:
                continue
            checked += 1
            target = (document.parent / target_without_anchor).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"{document.relative_to(ROOT)}: link escapes repository: {raw_target}"
                )
                continue
            if not target.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: missing link target: {raw_target}"
                )
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"\n{len(errors)} broken link(s)")
        return 1
    print(f"Validated {checked} relative Markdown links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
