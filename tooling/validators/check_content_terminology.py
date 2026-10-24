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
VALID_MEANING_OWNERS = {"product_knowledge", "design_language"}
DESIGN_LANGUAGE_OWNED_CONCEPT_KINDS = {
    "communication_concept",
    "feature_family",
    "persona",
}
VALID_AUTHORITY_MIGRATION_STATES = {
    "source_linked",
    "needs_product_knowledge_reference",
    "not_applicable",
}
VALID_PRODUCTS = {"jobvision", "cando"}
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
    source_roles: dict[str, str] = {}
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
            role = source.get("role")
            if not nonempty_string(role):
                errors.append(f"{location}.role must be a non-empty string")
            else:
                source_roles[source_id] = role
    duplicate_sources = sorted(
        source_id
        for source_id, count in Counter(source_ids).items()
        if source_id and count > 1
    )
    if duplicate_sources:
        errors.append(f"duplicate source ids: {', '.join(duplicate_sources)}")
    known_sources = set(source_ids)

    authority_model = data.get("authority_model")
    if not isinstance(authority_model, dict):
        errors.append("top-level `authority_model` must be a mapping")
        authority_model = {}
    expected_authority_values = {
        "language_owner": "design_language",
        "linked_product_source_role": "product_knowledge_reference",
        "unresolved_product_source": "unresolved",
        "not_applicable_product_source": "not_applicable",
    }
    for field, expected in expected_authority_values.items():
        if authority_model.get(field) != expected:
            errors.append(
                f"authority_model.{field} must be `{expected}`"
            )
    meaning_owners = authority_model.get("meaning_owners")
    if not isinstance(meaning_owners, list) or set(meaning_owners) != (
        VALID_MEANING_OWNERS
    ):
        errors.append(
            "authority_model.meaning_owners must contain exactly "
            + ", ".join(sorted(VALID_MEANING_OWNERS))
        )
    design_language_kinds = authority_model.get(
        "design_language_owned_concept_kinds"
    )
    if not isinstance(design_language_kinds, list) or set(
        design_language_kinds
    ) != DESIGN_LANGUAGE_OWNED_CONCEPT_KINDS:
        errors.append(
            "authority_model.design_language_owned_concept_kinds must contain exactly "
            + ", ".join(sorted(DESIGN_LANGUAGE_OWNED_CONCEPT_KINDS))
        )
    migration_states = authority_model.get("migration_states")
    if not isinstance(migration_states, list) or set(migration_states) != (
        VALID_AUTHORITY_MIGRATION_STATES
    ):
        errors.append(
            "authority_model.migration_states must contain exactly "
            + ", ".join(sorted(VALID_AUTHORITY_MIGRATION_STATES))
        )

    product_variant_model = data.get("product_variant_model")
    if not isinstance(product_variant_model, dict):
        errors.append("top-level `product_variant_model` must be a mapping")
        product_variant_model = {}
    products = product_variant_model.get("products")
    if not isinstance(products, list) or set(products) != VALID_PRODUCTS:
        errors.append(
            "product_variant_model.products must contain exactly "
            + ", ".join(sorted(VALID_PRODUCTS))
        )
    if product_variant_model.get("unresolved_source") != "unresolved":
        errors.append(
            "product_variant_model.unresolved_source must be `unresolved`"
        )

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

        concept_kind = term.get("concept_kind")
        if not nonempty_string(concept_kind):
            errors.append(f"{location}: missing non-empty `concept_kind`")

        authority = term.get("authority")
        if not isinstance(authority, dict):
            errors.append(f"{location}: authority must be a mapping")
            authority = {}
        meaning_owner = authority.get("meaning_owner")
        if meaning_owner not in VALID_MEANING_OWNERS:
            errors.append(
                f"{location}: authority.meaning_owner must be one of "
                f"{sorted(VALID_MEANING_OWNERS)}"
            )
        if (
            meaning_owner == "design_language"
            and concept_kind not in DESIGN_LANGUAGE_OWNED_CONCEPT_KINDS
        ):
            errors.append(
                f"{location}: concept_kind `{concept_kind}` cannot use "
                "`design_language` as meaning owner"
            )
        if authority.get("language_owner") != "design_language":
            errors.append(
                f"{location}: authority.language_owner must be `design_language`"
            )
        migration_state = authority.get("migration_state")
        if migration_state not in VALID_AUTHORITY_MIGRATION_STATES:
            errors.append(
                f"{location}: authority.migration_state must be one of "
                f"{sorted(VALID_AUTHORITY_MIGRATION_STATES)}"
            )
        product_source = authority.get("product_source")
        if meaning_owner == "product_knowledge":
            if migration_state == "source_linked":
                if product_source not in known_sources:
                    errors.append(
                        f"{location}: linked product_source must reference a known source"
                    )
                elif source_roles.get(product_source) != (
                    "product_knowledge_reference"
                ):
                    errors.append(
                        f"{location}: linked product_source `{product_source}` must use "
                        "`product_knowledge_reference` role"
                    )
            elif migration_state == "needs_product_knowledge_reference":
                if product_source != "unresolved":
                    errors.append(
                        f"{location}: unresolved product_source must be `unresolved`"
                    )
            else:
                errors.append(
                    f"{location}: product-owned meaning cannot use "
                    "`not_applicable` migration state"
                )
        elif meaning_owner == "design_language":
            if (
                migration_state != "not_applicable"
                or product_source != "not_applicable"
            ):
                errors.append(
                    f"{location}: Design Language-owned meaning must use "
                    "`not_applicable` product source and migration state"
                )

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
            if (
                migration_state == "source_linked"
                and product_source not in evidence
            ):
                errors.append(
                    f"{location}: linked product_source must also appear in evidence"
                )

        product_variants = term.get("product_variants")
        if product_variants is not None:
            if not isinstance(product_variants, dict) or not product_variants:
                errors.append(
                    f"{location}: product_variants must be a non-empty mapping"
                )
            else:
                invalid_products = sorted(set(product_variants) - VALID_PRODUCTS)
                if invalid_products:
                    errors.append(
                        f"{location}: unknown product variants: "
                        + ", ".join(invalid_products)
                    )
                for product, variant in product_variants.items():
                    variant_location = f"{location}.product_variants.{product}"
                    if not isinstance(variant, dict):
                        errors.append(f"{variant_location} must be a mapping")
                        continue
                    preferred_variant = variant.get("preferred")
                    if not isinstance(preferred_variant, dict) or not any(
                        nonempty_string(value)
                        for value in preferred_variant.values()
                    ):
                        errors.append(
                            f"{variant_location}.preferred must contain a label"
                        )
                    variant_source = variant.get("product_source")
                    if variant_source == "unresolved":
                        continue
                    if variant_source not in known_sources:
                        errors.append(
                            f"{variant_location}.product_source must reference "
                            "a known source or `unresolved`"
                        )
                    elif source_roles.get(variant_source) != (
                        "product_knowledge_reference"
                    ):
                        errors.append(
                            f"{variant_location}.product_source must use "
                            "`product_knowledge_reference` role"
                        )
                    elif variant_source not in evidence:
                        errors.append(
                            f"{variant_location}.product_source must also "
                            "appear in evidence"
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
    authority_states = Counter(
        term["authority"]["migration_state"] for term in terms
    )
    print(
        "Content terminology is valid: "
        f"{len(terms)} terms, {len(data['decision_queue'])} open decisions, "
        f"{len(data['decision_log'])} resolved decisions, "
        + ", ".join(f"{key}={value}" for key, value in sorted(statuses.items()))
        + "; authority: "
        + ", ".join(
            f"{key}={value}" for key, value in sorted(authority_states.items())
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
