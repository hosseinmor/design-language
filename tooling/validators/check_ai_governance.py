#!/usr/bin/env python3
"""Check AI router destinations and effective reviewed-document stewardship.

Structural integrity of the Manifest and related IDs belongs to generate_manifest.py.
This validator checks the operational router locations and reviewed owner lookup.
"""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTER = ROOT / "ai" / "router.md"
MANIFEST = ROOT / "registry" / "manifest.generated.json"
INLINE = re.compile(chr(96) + "([^" + chr(96) + "]+)" + chr(96))
ALTERNATIVES = re.compile(r"\{([^{}]+)\}")


def expand_locations(raw: str) -> list[str]:
    match = ALTERNATIVES.search(raw)
    if match is None:
        return [raw]
    options = [s.strip() for s in match.group(1).split(",")]
    if any(not s for s in options):
        raise ValueError(f"Malformed route alternatives: {raw}")
    return list(itertools.chain.from_iterable(
        expand_locations(raw[:match.start()] + option + raw[match.end():])
        for option in options
    ))


def router_locations(markdown: str) -> list[str]:
    result: list[str] = []
    for line in markdown.splitlines():
        if not line.startswith("|"):
            continue
        cells = line.split("|")
        if len(cells) < 4:
            continue
        # The second column contains the authoritative initial discovery route.
        result.extend(INLINE.findall(cells[2]))
    return result


def main() -> int:
    errors: list[str] = []
    routes = router_locations(ROUTER.read_text(encoding="utf-8"))
    if not routes:
        errors.append("ai/router.md contains no machine-checkable route locations.")

    expanded: list[str] = []
    for raw in routes:
        try:
            expanded.extend(expand_locations(raw))
        except ValueError as exc:
            errors.append(str(exc))
    for location in expanded:
        target = (ROOT / location).resolve()
        if not target.is_relative_to(ROOT.resolve()):
            errors.append(f"Route escapes repository: {location}")
        elif not target.exists():
            errors.append(f"Missing AI router destination: {location}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = manifest.get("documents", [])
    if not entries:
        errors.append("Registry Manifest has no indexed documents.")
    ownerless = [doc["id"] for doc in entries
                 if doc.get("status") == "reviewed" and not doc.get("owner")]
    for doc_id in ownerless:
        errors.append(f"Reviewed document has no effective owner: {doc_id}")
    # Drafts are intentionally not promoted or force-assigned reviewers here.

    if errors:
        for error in errors:
            print("ERROR " + error)
        print(f"{len(errors)} AI/Governance validation error(s).")
        return 1
    print(f"Validated {len(routes)} router patterns, {len(expanded)} destinations, "
          f"and effective ownership of {sum(d.get('status') == 'reviewed' for d in entries)} reviewed documents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
