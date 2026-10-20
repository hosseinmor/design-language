---
id: design-system.foundation.color
collection: design-system
type: foundation
title: Color
summary: Operational entry point for JV Color semantics, installable Theme architecture, Appearance behavior, accessibility, and source routing.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.architecture
  - design-system.token.semantic-tokens
  - design-system.token.component-tokens
  - design-system.token.product-overrides
  - design-system.accessibility.color-and-contrast
  - design-system.reference.source-of-truth
last_reviewed: '2026-09-14'
---

# Color

Color communicates structure, hierarchy, interaction, Product identity, system feedback, and a small number of reviewed product meanings. Choose it by semantic role rather than by hue.

This document is the compact entry point. It defines durable rules and routes exact questions to the owning source instead of duplicating the full token catalog or Figma value table.

## Color model

The target runtime model separates the shared Color contract from Theme-specific values:

```text
Shared Design System
→ owns Semantic role names + meaning

Installed Theme
→ owns Theme-local Primitives
→ owns Light/Dark values for the shared Semantic roles

Product UI / Components
→ consume the shared Semantic roles
```

The normal path is therefore:

```text
Theme-local Primitive → Semantic → Product UI / Component
```

- **Primitive** is Theme-local implementation detail in the target runtime architecture.
- **Semantic** is the stable shared UI Color API.
- **Brand** remains semantic meaning but is no longer a required alias layer.
- **Component** Color tokens remain exceptional; most components consume Semantic Color directly.

Product UI must not bind directly to Theme-local Primitives.

Categorical Tag is the current approved Component Color-token exception. Its `tag/{color}/*` values are shared across Products, vary only by Light/Dark Appearance, and are not available as Product-facing tokens.

## Theme and Appearance

The application selects an installable Theme package; Theme is not Product identity itself.

Current intended mapping:

```text
JobVision application → JobVision Theme
Cando application     → Cando Theme
```

Each Theme package contains both Appearance mappings:

```text
Theme
├── Light
└── Dark
```

Appearance may change at runtime without switching Theme package.

Semantic token names remain stable across Themes and Appearances. Do not encode Product, Theme, Light, or Dark into public Semantic names.

The current Figma Variables model is:

```text
01 Primitives            → Value
02 Product               → JobVision | Cando
03 Semantic              → Value
03 Semantic Values       → Light | Dark
  ├── jobvision/*
  └── cando/*
04 Component Tokens      → Light | Dark
```

`03 Semantic` remains the stable public Color API. `02 Product` is the Figma Product-mode selector and routes Semantic values to the selected Product branch in `03 Semantic Values`; `03 Semantic Values` independently selects Light/Dark. `04 Component Tokens` remains Product-independent and component-only.

## Semantic boundaries

| Need | Use |
|---|---|
| Page, container, depth, or neutral interaction | `surface/*` |
| Text or icon | `fg/*` |
| Divider, outline, or boundary | `line/*` |
| Product identity or approved key conversion moment | Brand semantics |
| General chromatic interaction or affordance | Accent |
| AI-assisted or AI-generated capability | Magic |
| Destructive intent or irreversible action | Danger |
| Information, success, warning, or error feedback | Support |
| Navigation link | `link/*` |
| Keyboard focus indication | Focus roles |

Brand is not a synonym for primary, selected, focused, or important. Accent is not system feedback. Danger and Error may share Red primitives while remaining different meanings: Danger is destructive intent; Error is validation or system failure.

Selection is primarily a component state expressed through component anatomy. Do not create a parallel global Selected Color matrix. Use existing Surface, Foreground, Line, and Accent roles; only the reviewed persistent neutral selected-container surfaces are shared semantics.

Transparent interaction states and overlay are represented by resolved Semantic Color values themselves. A published alpha-palette API is not part of the current Color contract.

## Primitive palette rules

Primitive families are named by hue, not by Product or semantic ownership. The same hue ramp may feed several independent meanings.

For example, a Theme-local Blue ramp may feed Brand semantics, Accent, Link, Info, and a categorical Tag without those roles becoming interchangeable.

Do not add a hue family only to make the palette visually complete. Add or split one when a real Semantic or Component use case requires a distinct tonal range, or when contrast and appearance validation show that the current palette cannot serve the required roles.

Primitive step numbers represent tonal order; they are not semantic labels. Equivalent roles across different hues do not need the same numeric step.

## Accessibility

WCAG 2.2 AA is the web baseline. Validate **actual Semantic pairings and component states**, not isolated Primitive swatches.

- Normal text should meet the applicable text contrast requirement in its real background/state pairing.
- Essential non-text boundaries and focus indicators should meet their applicable contrast requirement.
- Disabled appearance is not a reason to make required explanatory content unreadable.
- Color must not be the only signal for state, validation, status, or meaning when another perceivable cue is required.
- Focus remains a dedicated Semantic role even when it shares a Primitive with Accent. The current default mapping uses the approved Accent Blue primitive for each Appearance; components still consume `focus/default`, and the actual Focus pairing must be validated across supported Theme × Appearance contexts.

For exact acceptance rules and edge cases, use [`../../accessibility/color-and-contrast.md`](../../accessibility/color-and-contrast.md).

## Where exact truth lives

- Token graph and layer responsibilities → [`../../design-system/tokens/architecture.md`](../../design-system/tokens/architecture.md)
- Semantic role meanings and boundaries → [`../../design-system/tokens/semantic-tokens.md`](../../design-system/tokens/semantic-tokens.md)
- Exact current aliases and visual values → current Figma variables; use [`../../design-system/tokens/color-token-aliases.md`](../../design-system/tokens/color-token-aliases.md) for the documented mapping contract
- Product ↔ Theme selection and Brand semantic resolution → [`../../design-system/tokens/product-overrides.md`](../../design-system/tokens/product-overrides.md)
- Component-owned Color exceptions such as Tag → [`../../design-system/tokens/component-tokens.md`](../../design-system/tokens/component-tokens.md)
- Accessibility and contrast requirements → [`../../accessibility/color-and-contrast.md`](../../accessibility/color-and-contrast.md)
- Source conflicts and ownership → [`../../integrations/source-of-truth.md`](../../integrations/source-of-truth.md)

Figma owns current editable visual values and aliases. Design System Knowledge owns semantic meaning and usage. Code/Storybook owns the runtime API and implemented behavior when available. A mismatch between them is a maintenance gap; do not invent a compromise.

## AI retrieval rule

For a Color question, start here and load only the next source needed:

```text
Color foundation
→ semantic meaning question?      semantic-tokens.md
→ architecture/layering question? architecture.md
→ exact current value/alias?       Figma, then color-token-aliases.md
→ Product variation?               product-overrides.md
→ Tag/component exception?         component-tokens.md
→ contrast/accessibility?          accessibility/color-and-contrast.md
```

Do not preload or reproduce the full token catalog when a semantic rule is sufficient. Do not infer unresolved runtime Theme, CSS variable, Tailwind, or SSR behavior from the Figma model.
