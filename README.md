# JV Design Language

This repository is the canonical decision layer for the shared JobVision and
Cando design language. It contains durable visual, content, interaction,
accessibility, component, pattern, and product-expression rules.

It does not replace the live sources that own exact implementation facts:

- Figma owns editable visual construction and published design assets.
- Karbon code and Storybook own runtime APIs, rendered behavior, examples, and tests.
- Product Knowledge owns product concepts, business rules, permissions, states, and flows.
- The Product Development Harness owns end-to-end delivery orchestration.

Start with [the design-language overview](overview/design-language.md), then
load only the component, pattern, foundation, or accessibility rule needed for
the task. See [Sources of Truth](integrations/source-of-truth.md) when sources
disagree.

## Structure

```text
overview/             Purpose, scope, and architecture
foundations/          Visual, content, and interaction foundations
accessibility/        Shared accessibility baseline and specialized guidance
design-system/        Tokens, components, patterns, and UI templates
product-expression/   Approved brand and experience variations
playbooks/            How to evolve or apply this language
integrations/         Figma, Karbon, code, and source-boundary contracts
assets/               Canonical icons, illustrations, and previews when added
governance/           Ownership, change, release, and documentation rules
registry/             Aliases and generated retrieval indexes
ai/                   AI routing, retrieval policy, and semantic evals
schemas/              Machine-readable contracts
tooling/              Repository validation and adapter tooling
tests/                Repository-level quality checks
```

## Validation

```bash
python tooling/generate_manifest.py generate
python tooling/generate_manifest.py check
python tooling/validate_links.py
python tooling/validators/check_accessibility_knowledge.py
python tooling/validators/check_content_terminology.py
python tooling/validators/check_content_localization.py
python tooling/validators/check_content_components.py
python tooling/validators/check_content_patterns.py
```

The generated files in `registry/` are derived artifacts. Do not edit them by
hand.
