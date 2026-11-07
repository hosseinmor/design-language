"""Shared index of content contract rules.

Content contracts reference each other through `depends_on`. An eval case may
check a rule owned by the contract under test or a rule it inherits from a
contract it depends on (voice, pattern or component). Blocking-rule coverage is
still counted per owning contract by the specialized validators.

Retired rule IDs stay reserved forever: they are listed under `retired_rules`
with the rule or document that now owns the decision.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "foundations" / "content"


def contract_paths() -> list[Path]:
    return sorted(
        [CONTENT / "product-voice.yml", CONTENT / "copy-brief.yml", CONTENT / "copy-audit.yml"]
        + list((CONTENT / "patterns").glob("*.yml"))
        + list((CONTENT / "components").glob("*.yml"))
    )


def load(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def active_rule_ids(data: dict[str, Any]) -> set[str]:
    return {
        rule["id"]
        for rule in data.get("rules") or []
        if isinstance(rule, dict) and isinstance(rule.get("id"), str)
    }


def retired_rule_ids(data: dict[str, Any]) -> set[str]:
    return {
        item["id"]
        for item in data.get("retired_rules") or []
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }


@lru_cache(maxsize=1)
def contracts_by_id() -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for path in contract_paths():
        data = load(path)
        if isinstance(data.get("id"), str):
            index[data["id"]] = data
    return index


def _strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for item in value.values() for s in _strings(item)]
    if isinstance(value, list):
        return [s for item in value for s in _strings(item)]
    return []


def inherited_rule_ids(contract_id: str) -> set[str]:
    """Active rule IDs of every content contract named in `depends_on`."""
    index = contracts_by_id()
    data = index.get(contract_id, {})
    inherited: set[str] = set()
    for reference in _strings(data.get("depends_on")):
        if reference != contract_id and reference in index:
            inherited |= active_rule_ids(index[reference])
    return inherited
