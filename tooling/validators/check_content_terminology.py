#!/usr/bin/env python3
"""Validate the machine-readable shared content terminology source."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
TERMS_PATH = ROOT / "foundations" / "content" / "terminology" / "terms.yml"
ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
DECISION_ID_RE = re.compile(r"^DEC-[0-9]{3}$")
VALID_STATUSES = {"stable", "draft", "needs_decision"}
VALID_VISIBILITY = {
    "public",
    "internal",
    "admin",
    "code_only",
    "documentation",
    "unknown",
}


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def load_terms() -> dict[str, Any]:
    try:
        loaded = yaml.load(
            TERMS_PATH.read_text(encoding="utf-8"), Loader=UniqueKeyLoader
        )
    except FileNotFoundError:
        raise SystemExit(f"ERROR missing terminology source: {TERMS_PATH}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR invalid YAML in {TERMS_PATH}: {exc}") from exc

    if not isinstance(loaded, dict):
        raise SystemExit("ERROR terminology source must be a YAML mapping")
    return loaded


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in ("schema_version", "id", "language"):
        if not nonempty_string(data.get(field)):
            errors.append(f"top-level `{field}` must be a non-empty string")
    if data.get("id") != "content.foundation.terminology":
        errors.append("top-level `id` must be `content.foundation.terminology`")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("top-level `sources` must be a non-empty list")
        sources = []
    source_ids: list[str] = []
    for index, source in enumerate(sources):
        location = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{location} must be a mapping")
            continue
        source_id = source.get("id")
        if not nonempty_string(source_id) or not ID_RE.fullmatch(source_id):
            errors.append(f"{location}.id must use snake_case")
        else:
            source_ids.append(source_id)
    duplicate_sources = sorted(
        source_id
        for source_id, count in Counter(source_ids).items()
        if source_id and count > 1
    )
    if duplicate_sources:
        errors.append(f"duplicate source ids: {', '.join(duplicate_sources)}")
    known_sources = set(source_ids)

    terms = data.get("terms")
    if not isinstance(terms, list) or not terms:
        errors.append("top-level `terms` must be a non-empty list")
        terms = []

    term_ids: list[str] = []
    for index, term in enumerate(terms):
        location = f"terms[{index}]"
        if not isinstance(term, dict):
            errors.append(f"{location} must be a mapping")
            continue

        term_id = term.get("id")
        if not nonempty_string(term_id) or not ID_RE.fullmatch(term_id):
            errors.append(f"{location}.id must use snake_case")
        else:
            term_ids.append(term_id)
            location = term_id

        if not nonempty_string(term.get("concept_kind")):
            errors.append(f"{location}: missing non-empty `concept_kind`")

        status = term.get("status")
        if status not in VALID_STATUSES:
            errors.append(
                f"{location}: status must be one of {sorted(VALID_STATUSES)}"
            )

        definition = term.get("definition")
        if not isinstance(definition, dict) or not any(
            nonempty_string(value) for value in definition.values()
        ):
            errors.append(f"{location}: definition must contain source or product content")

        visibility = term.get("visibility")
        if not isinstance(visibility, list) or not visibility:
            errors.append(f"{location}: visibility must be a non-empty list")
        elif not all(nonempty_string(value) for value in visibility):
            errors.append(f"{location}: visibility must contain only strings")
        elif invalid := sorted(set(visibility) - VALID_VISIBILITY):
            errors.append(f"{location}: invalid visibility values: {', '.join(invalid)}")

        evidence = term.get("evidence", [])
        if not isinstance(evidence, list):
            errors.append(f"{location}: evidence must be a list")
        elif not all(nonempty_string(source_id) for source_id in evidence):
            errors.append(f"{location}: evidence must contain only source ids")
        else:
            unknown = sorted(set(evidence) - known_sources)
            if unknown:
                errors.append(
                    f"{location}: unknown evidence source ids: {', '.join(unknown)}"
                )

        if status == "stable":
            preferred = term.get("preferred")
            if not isinstance(preferred, dict) or not any(
                nonempty_string(value) for value in preferred.values()
            ):
                errors.append(f"{location}: stable term requires a preferred label")

    duplicate_terms = sorted(
        term_id
        for term_id, count in Counter(term_ids).items()
        if count > 1
    )
    if duplicate_terms:
        errors.append(f"duplicate term ids: {', '.join(duplicate_terms)}")
    known_terms = set(term_ids)

    decisions = data.get("decision_queue")
    if not isinstance(decisions, list):
        errors.append("top-level `decision_queue` must be a list")
        decisions = []

    decision_ids: list[str] = []
    for index, decision in enumerate(decisions):
        location = f"decision_queue[{index}]"
        if not isinstance(decision, dict):
            errors.append(f"{location} must be a mapping")
            continue

        decision_id = decision.get("id")
        if not nonempty_string(decision_id) or not DECISION_ID_RE.fullmatch(decision_id):
            errors.append(f"{location}.id must match DEC-000")
        else:
            decision_ids.append(decision_id)
            location = decision_id

        referenced_terms = decision.get("term_ids")
        if not isinstance(referenced_terms, list) or not referenced_terms:
            errors.append(f"{location}: term_ids must be a non-empty list")
        elif not all(nonempty_string(term_id) for term_id in referenced_terms):
            errors.append(f"{location}: term_ids must contain only term ids")
        else:
            unknown = sorted(set(referenced_terms) - known_terms)
            if unknown:
                errors.append(f"{location}: unknown term ids: {', '.join(unknown)}")

        for field in ("question", "recommendation", "impact"):
            if not nonempty_string(decision.get(field)):
                errors.append(f"{location}: missing non-empty `{field}`")

    duplicate_decisions = sorted(
        decision_id
        for decision_id, count in Counter(decision_ids).items()
        if count > 1
    )
    if duplicate_decisions:
        errors.append(f"duplicate decision ids: {', '.join(duplicate_decisions)}")

    decision_log = data.get("decision_log")
    if not isinstance(decision_log, list):
        errors.append("top-level `decision_log` must be a list")
        decision_log = []

    resolved_ids: list[str] = []
    for index, decision in enumerate(decision_log):
        location = f"decision_log[{index}]"
        if not isinstance(decision, dict):
            errors.append(f"{location} must be a mapping")
            continue

        decision_id = decision.get("id")
        if not nonempty_string(decision_id) or not DECISION_ID_RE.fullmatch(decision_id):
            errors.append(f"{location}.id must match DEC-000")
        else:
            resolved_ids.append(decision_id)
            location = decision_id

        referenced_terms = decision.get("term_ids")
        if not isinstance(referenced_terms, list) or not referenced_terms:
            errors.append(f"{location}: term_ids must be a non-empty list")
        elif not all(nonempty_string(term_id) for term_id in referenced_terms):
            errors.append(f"{location}: term_ids must contain only term ids")
        else:
            unknown = sorted(set(referenced_terms) - known_terms)
            if unknown:
                errors.append(f"{location}: unknown term ids: {', '.join(unknown)}")

        if not nonempty_string(str(decision.get("decided_on", ""))):
            errors.append(f"{location}: missing `decided_on`")
        for field in ("outcome", "rationale"):
            if not nonempty_string(decision.get(field)):
                errors.append(f"{location}: missing non-empty `{field}`")

    duplicate_resolved = sorted(
        decision_id
        for decision_id, count in Counter(resolved_ids).items()
        if count > 1
    )
    if duplicate_resolved:
        errors.append(f"duplicate resolved decision ids: {', '.join(duplicate_resolved)}")

    overlap = sorted(set(decision_ids) & set(resolved_ids))
    if overlap:
        errors.append(
            "decision ids cannot be both open and resolved: " + ", ".join(overlap)
        )

    return errors


def main() -> int:
    data = load_terms()
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    terms = data["terms"]
    statuses = Counter(term["status"] for term in terms)
    print(
        "Content terminology is valid: "
        f"{len(terms)} terms, {len(data['decision_queue'])} open decisions, "
        f"{len(data['decision_log'])} resolved decisions, "
        + ", ".join(f"{key}={value}" for key, value in sorted(statuses.items()))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
