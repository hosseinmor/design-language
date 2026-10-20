#!/usr/bin/env python3
"""Validate machine-readable product voice, content patterns, and evals."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
VOICE_PATH = ROOT / "foundations" / "content" / "product-voice.yml"
ERROR_PATH = ROOT / "foundations" / "content" / "patterns" / "errors.yml"
EVAL_PATH = ROOT / "ai" / "evals" / "content" / "error-cases.yml"
CONFIRMATION_PATH = ROOT / "foundations" / "content" / "patterns" / "confirmations.yml"
CONFIRMATION_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "confirmation-cases.yml"
)
EMPTY_STATE_PATH = ROOT / "foundations" / "content" / "patterns" / "empty-states.yml"
EMPTY_STATE_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "empty-state-cases.yml"
)
NOTIFICATION_PATH = ROOT / "foundations" / "content" / "patterns" / "notifications.yml"
NOTIFICATION_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "notification-cases.yml"
)
LOADING_PATH = (
    ROOT / "foundations" / "content" / "patterns" / "loading-and-progress.yml"
)
LOADING_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "loading-progress-cases.yml"
)
AI_CONTENT_PATH = (
    ROOT / "foundations" / "content" / "patterns" / "ai-content-and-disclosure.yml"
)
AI_CONTENT_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "ai-content-cases.yml"
)
INSTRUCTION_PATH = (
    ROOT / "foundations" / "content" / "patterns" / "instructions-and-helper-text.yml"
)
INSTRUCTION_EVAL_PATH = (
    ROOT / "ai" / "evals" / "content" / "instruction-helper-cases.yml"
)
PATTERN_PATHS = (
    ERROR_PATH,
    CONFIRMATION_PATH,
    EMPTY_STATE_PATH,
    NOTIFICATION_PATH,
    LOADING_PATH,
    AI_CONTENT_PATH,
    INSTRUCTION_PATH,
)
EVAL_PATHS = (
    EVAL_PATH,
    CONFIRMATION_EVAL_PATH,
    EMPTY_STATE_EVAL_PATH,
    NOTIFICATION_EVAL_PATH,
    LOADING_EVAL_PATH,
    AI_CONTENT_EVAL_PATH,
    INSTRUCTION_EVAL_PATH,
)
# Keep the shared eval directory closed while specialized validators own these files.
NON_PATTERN_EVAL_PATHS = (
    ROOT / "ai" / "evals" / "content" / "localization-cases.yml",
    ROOT / "ai" / "evals" / "content" / "button-content-cases.yml",
    ROOT / "ai" / "evals" / "content" / "text-input-content-cases.yml",
    ROOT / "ai" / "evals" / "content" / "modal-content-cases.yml",
    ROOT / "ai" / "evals" / "content" / "notification-content-cases.yml",
)
RULE_ID_RE = re.compile(r"^(VOICE|ERR|CNF|EST|NTF|LDP|AIC|INS)-[0-9]{3}$")
CASE_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
VALID_OBLIGATIONS = {"must", "must_not", "should"}
TONE_DIMENSIONS = {"clarity", "warmth", "encouragement", "brand_expression"}


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


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.load(
            path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader
        )
    except FileNotFoundError:
        raise SystemExit(f"ERROR missing content source: {path}")
    except yaml.YAMLError as exc:
        raise SystemExit(f"ERROR invalid YAML in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise SystemExit(f"ERROR {path} must contain a YAML mapping")
    return loaded


def validate_registered_inventory() -> list[str]:
    errors: list[str] = []
    expected_patterns = {path.name for path in PATTERN_PATHS}
    actual_patterns = {
        path.name for path in ERROR_PATH.parent.glob("*.yml") if path.is_file()
    }
    expected_human_docs = {path.with_suffix(".md").name for path in PATTERN_PATHS}
    actual_human_docs = {
        path.name for path in ERROR_PATH.parent.glob("*.md") if path.is_file()
    }
    expected_evals = {path.name for path in EVAL_PATHS + NON_PATTERN_EVAL_PATHS}
    actual_evals = {
        path.name for path in EVAL_PATH.parent.glob("*.yml") if path.is_file()
    }

    for label, expected, actual in (
        ("pattern", expected_patterns, actual_patterns),
        ("human-readable pattern", expected_human_docs, actual_human_docs),
        ("eval", expected_evals, actual_evals),
    ):
        missing = sorted(expected - actual)
        unregistered = sorted(actual - expected)
        if missing:
            errors.append(f"missing registered {label} files: {', '.join(missing)}")
        if unregistered:
            errors.append(
                f"unregistered {label} files: {', '.join(unregistered)}"
            )

    return errors


def duplicate_values(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def validate_identity(
    data: dict[str, Any],
    label: str,
    expected_id: str,
    required_fields: tuple[str, ...],
) -> list[str]:
    errors: list[str] = []
    for field in required_fields:
        if not nonempty_string(data.get(field)):
            errors.append(f"{label}: top-level `{field}` must be a non-empty string")
    if data.get("id") != expected_id:
        errors.append(f"{label}: `id` must be `{expected_id}`")
    return errors


def validate_rules(
    rules: Any,
    label: str,
    expected_prefix: str,
    source_ids: set[str] | None = None,
    require_key: bool = False,
) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    if not isinstance(rules, list) or not rules:
        return [f"{label}: `rules` must be a non-empty list"], set()

    rule_ids: list[str] = []
    rule_keys: list[str] = []
    for index, rule in enumerate(rules):
        location = f"{label}.rules[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{location} must be a mapping")
            continue
        rule_id = rule.get("id")
        if not nonempty_string(rule_id) or not RULE_ID_RE.fullmatch(rule_id):
            errors.append(
                f"{location}.id must match VOICE-000, ERR-000, CNF-000, EST-000, NTF-000, LDP-000, AIC-000, or INS-000"
            )
        else:
            rule_ids.append(rule_id)
            location = rule_id
            if not rule_id.startswith(f"{expected_prefix}-"):
                errors.append(
                    f"{location}: rule id must use the `{expected_prefix}-000` family"
                )
        if require_key:
            rule_key = rule.get("key")
            if not nonempty_string(rule_key):
                errors.append(f"{location}: missing non-empty `key`")
            else:
                rule_keys.append(rule_key)
        if rule.get("obligation") not in VALID_OBLIGATIONS:
            errors.append(
                f"{location}: obligation must be one of {sorted(VALID_OBLIGATIONS)}"
            )
        if not nonempty_string(rule.get("statement")):
            errors.append(f"{location}: missing non-empty `statement`")
        if source_ids is not None:
            evidence = rule.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                errors.append(f"{location}: evidence must be a non-empty list")
            else:
                unknown = sorted(set(evidence) - source_ids)
                if unknown:
                    errors.append(
                        f"{location}: unknown evidence source ids: {', '.join(unknown)}"
                    )

    duplicates = duplicate_values(rule_ids)
    if duplicates:
        errors.append(f"{label}: duplicate rule ids: {', '.join(duplicates)}")
    duplicate_keys = duplicate_values(rule_keys)
    if duplicate_keys:
        errors.append(f"{label}: duplicate rule keys: {', '.join(duplicate_keys)}")
    return errors, set(rule_ids)


def validate_voice(data: dict[str, Any]) -> tuple[list[str], set[str], set[str]]:
    errors = validate_identity(
        data,
        "voice",
        "content.foundation.product_voice",
        ("schema_version", "id", "title", "language"),
    )

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("voice: `sources` must be a non-empty list")
        sources = []
    source_ids = {
        item.get("id")
        for item in sources
        if isinstance(item, dict) and nonempty_string(item.get("id"))
    }
    if len(source_ids) != len(sources):
        errors.append("voice: every source requires a unique non-empty id")

    if not isinstance(data.get("source_derived"), dict):
        errors.append("voice: `source_derived` must be a mapping")

    model = data.get("operational_model")
    if not isinstance(model, dict):
        errors.append("voice: `operational_model` must be a mapping")
        model = {}
    dimensions = model.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != TONE_DIMENSIONS:
        errors.append(
            "voice: operational dimensions must be exactly "
            + ", ".join(sorted(TONE_DIMENSIONS))
        )
        dimensions = {}

    allowed_levels: dict[str, set[str]] = {}
    for dimension in TONE_DIMENSIONS:
        definition = dimensions.get(dimension, {})
        levels = definition.get("levels") if isinstance(definition, dict) else None
        if not isinstance(levels, list) or not levels:
            errors.append(f"voice: dimension `{dimension}` requires non-empty levels")
            allowed_levels[dimension] = set()
        else:
            allowed_levels[dimension] = set(levels)

    profiles = model.get("tone_profiles")
    if not isinstance(profiles, dict) or not profiles:
        errors.append("voice: `tone_profiles` must be a non-empty mapping")
        profiles = {}
    for profile_id, profile in profiles.items():
        if not isinstance(profile, dict):
            errors.append(f"voice: tone profile `{profile_id}` must be a mapping")
            continue
        for dimension in TONE_DIMENSIONS:
            value = profile.get(dimension)
            if value not in allowed_levels.get(dimension, set()):
                errors.append(
                    f"voice: tone profile `{profile_id}` has invalid `{dimension}` level"
                )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "voice", "VOICE", source_ids=source_ids
    )
    errors.extend(rule_errors)
    return errors, set(profiles), rule_ids


def validate_error_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "error pattern",
        "content.pattern.error",
        ("schema_version", "id", "title", "language", "goal"),
    )
    if data.get("tone_profile") not in tone_profiles:
        errors.append("error pattern: `tone_profile` must reference a known voice profile")

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "error pattern", "ERR", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(anatomy.get("pattern")):
        errors.append("error pattern: anatomy requires a non-empty `pattern`")
    if not isinstance(data.get("placement"), dict) or not data["placement"]:
        errors.append("error pattern: `placement` must be a non-empty mapping")
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("error pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_confirmation_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "confirmation pattern",
        "content.pattern.confirmation",
        ("schema_version", "id", "title", "language", "goal"),
    )
    for field in ("tone_profile", "destructive_tone_profile"):
        if data.get(field) not in tone_profiles:
            errors.append(
                f"confirmation pattern: `{field}` must reference a known voice profile"
            )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "confirmation pattern", "CNF", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("title_pattern")
    ):
        errors.append(
            "confirmation pattern: anatomy requires a non-empty `title_pattern`"
        )
    if not isinstance(data.get("decision_model"), dict) or not data["decision_model"]:
        errors.append("confirmation pattern: `decision_model` must be a non-empty mapping")
    if not isinstance(data.get("placement"), dict) or not data["placement"]:
        errors.append("confirmation pattern: `placement` must be a non-empty mapping")
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("confirmation pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_empty_state_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "empty-state pattern",
        "content.pattern.empty-states",
        ("schema_version", "id", "title", "language", "goal"),
    )
    if data.get("tone_profile") not in tone_profiles:
        errors.append(
            "empty-state pattern: `tone_profile` must reference a known voice profile"
        )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "empty-state pattern", "EST", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("message_pattern")
    ):
        errors.append(
            "empty-state pattern: anatomy requires a non-empty `message_pattern`"
        )
    if not isinstance(data.get("taxonomy"), dict) or not data["taxonomy"]:
        errors.append("empty-state pattern: `taxonomy` must be a non-empty mapping")
    if (
        not isinstance(data.get("action_selection"), dict)
        or not data["action_selection"]
    ):
        errors.append(
            "empty-state pattern: `action_selection` must be a non-empty mapping"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("empty-state pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_notification_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "notification pattern",
        "content.pattern.notifications",
        ("schema_version", "id", "title", "language", "goal"),
    )

    pattern_profiles = data.get("tone_profiles")
    if not isinstance(pattern_profiles, dict) or not pattern_profiles:
        errors.append("notification pattern: `tone_profiles` must be a non-empty mapping")
    else:
        required_severities = {"info", "success", "warning", "error"}
        if set(pattern_profiles) != required_severities:
            errors.append(
                "notification pattern: tone profiles must map exactly info, success, warning, and error"
            )
        unknown_profiles = sorted(set(pattern_profiles.values()) - tone_profiles)
        if unknown_profiles:
            errors.append(
                "notification pattern: unknown tone profiles: "
                + ", ".join(unknown_profiles)
            )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "notification pattern", "NTF", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    for field in ("severity_model", "presentation_model", "action_model"):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(
                f"notification pattern: `{field}` must be a non-empty mapping"
            )
    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("message_pattern")
    ):
        errors.append(
            "notification pattern: anatomy requires a non-empty `message_pattern`"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("notification pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_loading_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "loading pattern",
        "content.pattern.loading-and-progress",
        ("schema_version", "id", "title", "language", "goal"),
    )
    if data.get("tone_profile") not in tone_profiles:
        errors.append(
            "loading pattern: `tone_profile` must reference a known voice profile"
        )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "loading pattern", "LDP", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    for field in ("taxonomy", "state_model", "action_model", "accessibility"):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(f"loading pattern: `{field}` must be a non-empty mapping")
    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not nonempty_string(
        anatomy.get("indeterminate_pattern")
    ) or not nonempty_string(anatomy.get("determinate_pattern")):
        errors.append(
            "loading pattern: anatomy requires indeterminate and determinate patterns"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("loading pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_ai_content_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "AI content pattern",
        "content.pattern.ai-content-and-disclosure",
        ("schema_version", "id", "title", "language", "goal"),
    )

    pattern_profiles = data.get("tone_profiles")
    if not isinstance(pattern_profiles, dict) or not pattern_profiles:
        errors.append("AI content pattern: `tone_profiles` must be a non-empty mapping")
    else:
        required_profiles = {"feature", "assistant"}
        if set(pattern_profiles) != required_profiles:
            errors.append(
                "AI content pattern: tone profiles must map exactly feature and assistant"
            )
        unknown_profiles = sorted(set(pattern_profiles.values()) - tone_profiles)
        if unknown_profiles:
            errors.append(
                "AI content pattern: unknown tone profiles: "
                + ", ".join(unknown_profiles)
            )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "AI content pattern", "AIC", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    for field in (
        "experience_model",
        "output_model",
        "disclosure_model",
        "action_model",
        "safety_boundaries",
        "state_model",
        "accessibility",
    ):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(
                f"AI content pattern: `{field}` must be a non-empty mapping"
            )
    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not isinstance(
        anatomy.get("entry_point"), dict
    ) or not isinstance(anatomy.get("output"), dict):
        errors.append(
            "AI content pattern: anatomy requires entry-point and output mappings"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("AI content pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_instruction_pattern(
    data: dict[str, Any], tone_profiles: set[str]
) -> tuple[list[str], dict[str, str]]:
    errors = validate_identity(
        data,
        "instruction pattern",
        "content.pattern.instructions-and-helper-text",
        ("schema_version", "id", "title", "language", "goal"),
    )
    if data.get("tone_profile") not in tone_profiles:
        errors.append(
            "instruction pattern: `tone_profile` must reference a known voice profile"
        )

    rule_errors, rule_ids = validate_rules(
        data.get("rules"), "instruction pattern", "INS", require_key=True
    )
    errors.extend(rule_errors)
    obligations = {
        rule["id"]: rule["obligation"]
        for rule in data.get("rules", [])
        if isinstance(rule, dict)
        and rule.get("id") in rule_ids
        and rule.get("obligation") in VALID_OBLIGATIONS
    }

    for field in (
        "content_roles",
        "placement_model",
        "requiredness_model",
        "validation_transition",
        "specialized_guidance",
    ):
        if not isinstance(data.get(field), dict) or not data[field]:
            errors.append(
                f"instruction pattern: `{field}` must be a non-empty mapping"
            )
    anatomy = data.get("anatomy")
    if not isinstance(anatomy, dict) or not isinstance(
        anatomy.get("field"), dict
    ) or not isinstance(anatomy.get("group"), dict):
        errors.append(
            "instruction pattern: anatomy requires field and group mappings"
        )
    if not isinstance(data.get("templates"), dict) or not data["templates"]:
        errors.append("instruction pattern: `templates` must be a non-empty mapping")
    return errors, obligations


def validate_evals(
    data: dict[str, Any],
    expected_eval_id: str,
    pattern_id: str,
    obligations: dict[str, str],
    eval_label: str,
) -> list[str]:
    errors = validate_identity(
        data,
        eval_label,
        expected_eval_id,
        ("schema_version", "id", "language"),
    )
    if data.get("pattern_id") != pattern_id:
        errors.append(f"{eval_label}: `pattern_id` must match the pattern id")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + [f"{eval_label}: `cases` must be a non-empty list"]

    case_ids: list[str] = []
    covered: set[str] = set()
    has_valid = False
    has_invalid = False
    known_rules = set(obligations)

    for index, case in enumerate(cases):
        location = f"{eval_label}.cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location} must be a mapping")
            continue
        case_id = case.get("id")
        if not nonempty_string(case_id) or not CASE_ID_RE.fullmatch(case_id):
            errors.append(f"{location}.id must use snake_case")
        else:
            case_ids.append(case_id)
            location = case_id
        if not isinstance(case.get("context"), dict) or not case["context"]:
            errors.append(f"{location}: context must be a non-empty mapping")
        if "message" in case:
            if not isinstance(case.get("message"), str):
                errors.append(f"{location}: message must be a string")
        elif "content" in case:
            if not isinstance(case.get("content"), dict) or not case["content"]:
                errors.append(f"{location}: content must be a non-empty mapping")
        else:
            errors.append(f"{location}: requires `message` or `content`")

        expected = case.get("expected")
        if not isinstance(expected, dict) or not isinstance(expected.get("valid"), bool):
            errors.append(f"{location}: expected.valid must be a boolean")
            continue
        checked = expected.get("checked_rules")
        violations = expected.get("violations")
        if not isinstance(checked, list) or not checked:
            errors.append(f"{location}: checked_rules must be a non-empty list")
            checked = []
        elif not all(nonempty_string(rule_id) for rule_id in checked):
            errors.append(f"{location}: checked_rules must contain only rule ids")
            checked = [rule_id for rule_id in checked if nonempty_string(rule_id)]
        if not isinstance(violations, list):
            errors.append(f"{location}: violations must be a list")
            violations = []
        elif not all(nonempty_string(rule_id) for rule_id in violations):
            errors.append(f"{location}: violations must contain only rule ids")
            violations = [
                rule_id for rule_id in violations if nonempty_string(rule_id)
            ]
        duplicate_checked = duplicate_values(checked)
        if duplicate_checked:
            errors.append(
                f"{location}: duplicate checked rule ids: {', '.join(duplicate_checked)}"
            )
        duplicate_violations = duplicate_values(violations)
        if duplicate_violations:
            errors.append(
                f"{location}: duplicate violation ids: {', '.join(duplicate_violations)}"
            )
        unknown = sorted((set(checked) | set(violations)) - known_rules)
        if unknown:
            errors.append(f"{location}: unknown rule ids: {', '.join(unknown)}")
        if not set(violations).issubset(set(checked)):
            errors.append(f"{location}: violations must be included in checked_rules")
        if expected["valid"]:
            has_valid = True
            if violations:
                errors.append(f"{location}: valid case cannot declare violations")
        else:
            has_invalid = True
            if not violations:
                errors.append(f"{location}: invalid case requires at least one violation")
        covered.update(checked)

    duplicates = duplicate_values(case_ids)
    if duplicates:
        errors.append(f"{eval_label}: duplicate case ids: {', '.join(duplicates)}")
    if not has_valid or not has_invalid:
        errors.append(f"{eval_label}: include at least one valid and one invalid case")

    blocking_rules = {
        rule_id
        for rule_id, obligation in obligations.items()
        if obligation in {"must", "must_not"}
    }
    missing_coverage = sorted(blocking_rules - covered)
    if missing_coverage:
        errors.append(
            f"{eval_label}: blocking rules without coverage: "
            + ", ".join(missing_coverage)
        )
    return errors


def validate_evaluation_source(
    pattern: dict[str, Any], expected_source: str, label: str
) -> list[str]:
    if pattern.get("evaluation_source") != expected_source:
        return [
            f"{label}: `evaluation_source` must be `{expected_source}`"
        ]
    return []


def main() -> int:
    inventory_errors = validate_registered_inventory()
    voice = load_yaml(VOICE_PATH)
    error_pattern = load_yaml(ERROR_PATH)
    error_evals = load_yaml(EVAL_PATH)
    confirmation_pattern = load_yaml(CONFIRMATION_PATH)
    confirmation_evals = load_yaml(CONFIRMATION_EVAL_PATH)
    empty_state_pattern = load_yaml(EMPTY_STATE_PATH)
    empty_state_evals = load_yaml(EMPTY_STATE_EVAL_PATH)
    notification_pattern = load_yaml(NOTIFICATION_PATH)
    notification_evals = load_yaml(NOTIFICATION_EVAL_PATH)
    loading_pattern = load_yaml(LOADING_PATH)
    loading_evals = load_yaml(LOADING_EVAL_PATH)
    ai_content_pattern = load_yaml(AI_CONTENT_PATH)
    ai_content_evals = load_yaml(AI_CONTENT_EVAL_PATH)
    instruction_pattern = load_yaml(INSTRUCTION_PATH)
    instruction_evals = load_yaml(INSTRUCTION_EVAL_PATH)

    errors, tone_profiles, voice_rules = validate_voice(voice)
    errors = inventory_errors + errors
    pattern_errors, obligations = validate_error_pattern(error_pattern, tone_profiles)
    errors.extend(pattern_errors)
    errors.extend(
        validate_evaluation_source(
            error_pattern, "../../../ai/evals/content/error-cases.yml", "error pattern"
        )
    )
    errors.extend(
        validate_evals(
            error_evals,
            "content.eval.error_cases",
            error_pattern.get("id", ""),
            obligations,
            "error evals",
        )
    )
    notification_errors, notification_obligations = validate_notification_pattern(
        notification_pattern, tone_profiles
    )
    errors.extend(notification_errors)
    errors.extend(
        validate_evaluation_source(
            notification_pattern,
            "../../../ai/evals/content/notification-cases.yml",
            "notification pattern",
        )
    )
    errors.extend(
        validate_evals(
            notification_evals,
            "content.eval.notification_cases",
            notification_pattern.get("id", ""),
            notification_obligations,
            "notification evals",
        )
    )
    loading_errors, loading_obligations = validate_loading_pattern(
        loading_pattern, tone_profiles
    )
    errors.extend(loading_errors)
    errors.extend(
        validate_evaluation_source(
            loading_pattern,
            "../../../ai/evals/content/loading-progress-cases.yml",
            "loading pattern",
        )
    )
    errors.extend(
        validate_evals(
            loading_evals,
            "content.eval.loading_progress_cases",
            loading_pattern.get("id", ""),
            loading_obligations,
            "loading evals",
        )
    )
    ai_content_errors, ai_content_obligations = validate_ai_content_pattern(
        ai_content_pattern, tone_profiles
    )
    errors.extend(ai_content_errors)
    errors.extend(
        validate_evaluation_source(
            ai_content_pattern,
            "../../../ai/evals/content/ai-content-cases.yml",
            "AI content pattern",
        )
    )
    errors.extend(
        validate_evals(
            ai_content_evals,
            "content.eval.ai_content_cases",
            ai_content_pattern.get("id", ""),
            ai_content_obligations,
            "AI content evals",
        )
    )
    instruction_errors, instruction_obligations = validate_instruction_pattern(
        instruction_pattern, tone_profiles
    )
    errors.extend(instruction_errors)
    errors.extend(
        validate_evaluation_source(
            instruction_pattern,
            "../../../ai/evals/content/instruction-helper-cases.yml",
            "instruction pattern",
        )
    )
    errors.extend(
        validate_evals(
            instruction_evals,
            "content.eval.instruction_helper_cases",
            instruction_pattern.get("id", ""),
            instruction_obligations,
            "instruction evals",
        )
    )
    empty_state_errors, empty_state_obligations = validate_empty_state_pattern(
        empty_state_pattern, tone_profiles
    )
    errors.extend(empty_state_errors)
    errors.extend(
        validate_evaluation_source(
            empty_state_pattern,
            "../../../ai/evals/content/empty-state-cases.yml",
            "empty-state pattern",
        )
    )
    errors.extend(
        validate_evals(
            empty_state_evals,
            "content.eval.empty_state_cases",
            empty_state_pattern.get("id", ""),
            empty_state_obligations,
            "empty-state evals",
        )
    )
    confirmation_errors, confirmation_obligations = validate_confirmation_pattern(
        confirmation_pattern, tone_profiles
    )
    errors.extend(confirmation_errors)
    errors.extend(
        validate_evaluation_source(
            confirmation_pattern,
            "../../../ai/evals/content/confirmation-cases.yml",
            "confirmation pattern",
        )
    )
    errors.extend(
        validate_evals(
            confirmation_evals,
            "content.eval.confirmation_cases",
            confirmation_pattern.get("id", ""),
            confirmation_obligations,
            "confirmation evals",
        )
    )

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1

    print(
        "Content patterns are valid: "
        f"{len(tone_profiles)} tone profiles, {len(voice_rules)} voice rules, "
        f"{len(obligations)} error rules, {len(error_evals['cases'])} error cases, "
        f"{len(confirmation_obligations)} confirmation rules, "
        f"{len(confirmation_evals['cases'])} confirmation cases, "
        f"{len(empty_state_obligations)} empty-state rules, "
        f"{len(empty_state_evals['cases'])} empty-state cases, "
        f"{len(notification_obligations)} notification rules, "
        f"{len(notification_evals['cases'])} notification cases, "
        f"{len(loading_obligations)} loading rules, "
        f"{len(loading_evals['cases'])} loading cases, "
        f"{len(ai_content_obligations)} AI content rules, "
        f"{len(ai_content_evals['cases'])} AI content cases, "
        f"{len(instruction_obligations)} instruction rules, "
        f"{len(instruction_evals['cases'])} instruction cases"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
