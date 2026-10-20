---
id: design-system.foundation.typography
collection: design-system
type: foundation
title: Typography
summary: Defines the shared Label, Body, and Heading recipes, Product-aware font identity, compact and fluid variants, and the boundary with local Tailwind typography.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.reference.tailwind
---

# Typography

## Model

Typography uses a small set of semantic composite recipes so Product teams choose recurring text by role rather than repeatedly choosing raw font size, line height, and weight.

The shared typography recipe has an approved size, line-height, weight and Product-aware font family. The exact recipe catalog lives in [Typography Tokens](../../design-system/tokens/typography/catalog.md).

Foreground color is separate and comes from Semantic Color.

Shared core families are:

```text
Label
Body
Body / Compact
Heading
Heading / Compact
Heading / Fluid
```

Paragraph and Display are intentionally not part of the core Product recipe set. Landing pages, marketing surfaces, lead paragraphs, display text, and other one-off expressive compositions may use native Tailwind typography utilities.





## DS recipe versus Tailwind utility

Use a Design System typography recipe for recurring Product typography.

Use native Tailwind `text-*`, `font-*`, and `leading-*` utilities for local/exceptional typography and expressive landing/marketing composition.

Do not override `font-size`, `line-height`, or `font-weight` with Tailwind utilities on an element that already consumes a DS typography recipe. Utilities for unrelated properties such as text alignment are fine.

The exact runtime API for consuming a DS recipe—CSS class, Angular directive/component, or another generated adapter—is Frontend-owned and remains to be finalized. Figma therefore does not encode a `type-` implementation prefix in Text Style names.

## Accessibility

- Do not use automatic line height in shared recipes.
- Keep each recipe's size and line height together.
- Validate compact styles with real Persian text.
- Do not truncate headings or essential text merely to preserve a fixed height.
- Validate mixed Persian/English content, zoom, text-spacing overrides, wrapping, and responsive reflow.

General text resize, reflow, contrast, language, and content requirements belong to the Accessibility corpus.

## Token source

Use [Typography Token Catalog](../../design-system/tokens/typography/catalog.md) for the complete approved style list and numeric definitions. This foundation owns usage, accessibility and composition guidance, not a second copy of the scale.

## Live references

- Figma Typography page: current Text Styles and usage rules are the editable visual source.
- Runtime adapter syntax and generated artifact: pending Frontend implementation review.
