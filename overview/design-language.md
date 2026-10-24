---
id: design-system.design-language
collection: design-system
type: design-language
title: JV Design Language
summary: Compact design-language entry point for human and AI design work; routes exact specifications to the canonical live sources.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.overview
  - design-system.structure
  - design-system.reference.source-of-truth
---

# JV Design Language

Use this file as the compact design-language entry point for JobVision and Cando UI work. It describes durable design intent; it is **not** a catalog of every token, component, accessibility rule, or implementation API.

## Design character

- Prefer clarity, task completion, and predictable behavior over decoration.
- Preserve useful information density in professional desktop workflows; do not make interfaces spacious only to appear modern.
- Use hierarchy through typography, spacing, surfaces, and action priority before adding decorative emphasis.
- Prefer an existing Design System component or pattern over a one-off control when it represents the same behavior.
- Choose components by semantic behavior, not visual resemblance.

## Shared system, product identity

JobVision and Cando share component semantics, interaction rules, and most Design System foundations.

Product identity may change Brand values and approved product variations without changing the meaning of shared Semantic roles. Brand is product identity; it is not a generic synonym for interaction, selection, focus, feedback, or every primary action.

## Foundations

- Use Semantic tokens in product UI; do not consume raw Primitive values unless an approved exception explicitly owns that mapping.
- Typography is chosen by content role before visual size.
- Dense product UI may use compact typography and spacing when readability, target-size, keyboard, and accessibility requirements still pass.
- Structural elevation and surface meaning are separate decisions; do not use stronger color merely to simulate depth.

## Interaction

- Make state changes explicit and predictable.
- Focus, selected, current, expanded, disabled, read-only, loading, error, and destructive intent are different states and must not be collapsed into one visual treatment.
- Do not hide required functionality behind hover-only interaction.
- Use motion to explain change, not as the only way to understand change.

## Persian and RTL

- Treat Persian/RTL as a primary product context, not a mirrored afterthought.
- Preserve meaningful reading and focus order in mixed Persian/English content.
- Directional behavior belongs to the component or pattern contract; do not blindly mirror every icon or keyboard behavior.

## Accessibility

WCAG 2.2 AA is the web baseline defined by the Accessibility corpus. Product Designers should use approved components and patterns rather than re-solving internal ARIA or keyboard mechanics. When a component/pattern contract is incomplete, route to the relevant specialized Accessibility guidance instead of guessing.

## Where exact truth lives

Do not duplicate live specifications in this file.

- **Design Language** → why, when, semantic meaning, decision rules, composition constraints, known gaps.
- **Figma** → editable visual construction, component properties, variables, layout specifications.
- **Code / Storybook when available** → runtime API, defaults, rendered states, implementation behavior, executable examples and tests.
- **Product Knowledge** → product-specific business rules, permissions, states, and workflows.
- **Temporary migration/history** → migration or change artifacts, not normal runtime design guidance.

See `../integrations/source-of-truth.md` for conflict handling.

## AI retrieval rule

Start here for design intent, then load only what the task needs:

```text
overview/design-language.md
→ relevant Component or Pattern
→ unresolved Foundation / Experience / Accessibility rule only when needed
→ query Figma / Code / Storybook for exact live specification
```

Do not preload the entire Design System.
