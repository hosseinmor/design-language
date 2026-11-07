#!/usr/bin/env python3
"""Validate the shared rule schema across all content contracts.

Contract-specific models (taxonomies, anatomy, tone profiles) stay in the
specialized validators. This validator owns what every contract shares:
rule identity, obligation, dimension vocabulary, global uniqueness, eval
references and the generated Markdown rule sections.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tooling"))

from generate_content_rule_sections import (  # noqa: E402
    contract_paths,
    expected_text,
)

EVAL_DIR = ROOT / "ai" / "evals" / "content"
RULE_ID_RE = re.compile(r"^([A-Z]{2,5})-[0-9]{3}$")
KEY_RE = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_OBLIGATIONS = {"must", "must_not", "should"}

# Closed vocabulary. Keep in sync with foundations/content/README.md.
RULE_DIMENSIONS = {
    "classification": "Identify the situation, text role or component before writing.",
    "product_truth": "Claims match verified product behavior and real system state.",
    "clarity": "The message names what happened, to what, and what it means.",
    "structure": "Content is distributed correctly across anatomy roles without repetition.",
    "action": "Action labels, available actions, safe exit and recovery.",
    "terminology": "Canonical labels for the audience and surface.",
    "tone": "Voice, register and brand expression.",
    "localization": "Numbers, dates, variables, units and bidirectional text.",
    "accessibility": "Programmatic meaning, names, relationships and announcements.",
    "disclosure": "AI involvement, provenance, limits and status of generated output.",
    "presentation": "Visual severity, hierarchy or display choice; marks a Design System boundary.",
    "interaction": "Interactive behavior such as data preservation and input handling.",
}
RULES_WITHOUT_KEY = {"product-voice.yml"}
REQUIRED_FIELDS = ("schema_version", "id", "title", "status", "language")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def validate_contract(
    path: Path, prefixes: dict[str, str], all_ids: dict[str, str]
) -> list[str]:
    errors: list[str] = []
    label = rel(path)
    data = load(path)

    for field in REQUIRED_FIELDS:
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"{label}: missing non-empty `{field}`")

    source = data.get("evaluation_source")
    if path.name != "product-voice.yml":
        if not isinstance(source, str) or not (path.parent / source).resolve().is_file():
            errors.append(f"{label}: `evaluation_source` must point to an existing file")

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        return errors + [f"{label}: `rules` must be a non-empty list"]

    own_prefixes: set[str] = set()
    keys: list[str] = []
    for index, rule in enumerate(rules):
        where = f"{label}: rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{where} must be a mapping")
            continue
        rule_id = rule.get("id")
        match = RULE_ID_RE.fullmatch(rule_id) if isinstance(rule_id, str) else None
        if not match:
            errors.append(f"{where}: id must match ABC-000")
        else:
            where = f"{label}: {rule_id}"
            own_prefixes.add(match.group(1))
            if rule_id in all_ids:
                errors.append(f"{where}: duplicate rule id (also in {all_ids[rule_id]})")
            all_ids[rule_id] = label
        if rule.get("obligation") not in VALID_OBLIGATIONS:
            errors.append(f"{where}: obligation must be one of {sorted(VALID_OBLIGATIONS)}")
        if rule.get("dimension") not in RULE_DIMENSIONS:
            errors.append(
                f"{where}: dimension `{rule.get('dimension')}` must be one of "
                f"{sorted(RULE_DIMENSIONS)}"
            )
        if not isinstance(rule.get("statement"), str) or not rule["statement"].strip():
            errors.append(f"{where}: missing non-empty `statement`")
        if path.name not in RULES_WITHOUT_KEY:
            key = rule.get("key")
            if not isinstance(key, str) or not KEY_RE.fullmatch(key):
                errors.append(f"{where}: `key` must use snake_case")
            else:
                keys.append(key)

    if len(own_prefixes) > 1:
        errors.append(f"{label}: rules must share one id prefix, found {sorted(own_prefixes)}")
    for prefix in own_prefixes:
        if prefix in prefixes and prefixes[prefix] != label:
            errors.append(f"{label}: prefix `{prefix}` is already used by {prefixes[prefix]}")
        prefixes[prefix] = label
    for key, count in Counter(keys).items():
        if count > 1:
            errors.append(f"{label}: duplicate rule key `{key}`")

    md_path = path.with_suffix(".md")
    try:
        if md_path.read_text(encoding="utf-8") != expected_text(md_path, path):
            errors.append(
                f"{rel(md_path)}: generated rule section is stale; run "
                "`python tooling/generate_content_rule_sections.py generate`"
            )
    except (OSError, ValueError) as error:
        errors.append(f"{rel(md_path)}: {error}")
    return errors


def referenced_rule_ids(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"checked_rules", "violations"} and isinstance(item, list):
                found.update(x for x in item if isinstance(x, str))
            else:
                found |= referenced_rule_ids(item)
    elif isinstance(value, list):
        for item in value:
            found |= referenced_rule_ids(item)
    return found


def validate_eval_references(all_ids: dict[str, str]) -> list[str]:
    errors: list[str] = []
    known_prefixes = {RULE_ID_RE.fullmatch(i).group(1) for i in all_ids}
    for path in sorted(EVAL_DIR.glob("*.yml")):
        for rule_id in sorted(referenced_rule_ids(load(path))):
            match = RULE_ID_RE.fullmatch(rule_id)
            if match and match.group(1) in known_prefixes and rule_id not in all_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown rule id `{rule_id}`")
    return errors


def duplicate_statements() -> list[str]:
    seen: dict[str, list[str]] = defaultdict(list)
    for path in contract_paths():
        for rule in load(path).get("rules") or []:
            if isinstance(rule, dict) and isinstance(rule.get("statement"), str):
                seen[" ".join(rule["statement"].split())].append(str(rule.get("id")))
    return [", ".join(ids) for ids in seen.values() if len(ids) > 1]


def main() -> int:
    errors: list[str] = []
    prefixes: dict[str, str] = {}
    all_ids: dict[str, str] = {}
    for path in contract_paths():
        errors.extend(validate_contract(path, prefixes, all_ids))
    errors.extend(validate_eval_references(all_ids))

    if errors:
        print("Content contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    dimensions = Counter()
    for path in contract_paths():
        dimensions.update(r.get("dimension") for r in load(path).get("rules") or [])
    duplicates = duplicate_statements()
    if duplicates:
        print("Note: identical rule statements in more than one contract (ownership review):")
        for item in duplicates:
            print(f"  - {item}")
    summary = ", ".join(f"{k}={v}" for k, v in sorted(dimensions.items()))
    print(
        f"Content contracts are valid: {len(contract_paths())} contracts, "
        f"{len(all_ids)} rules; {summary}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
