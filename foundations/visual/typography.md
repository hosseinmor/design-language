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

The core recipe owns:
- font size;
- line height;
- weight;
- Product-aware font family.

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

## Product-aware font family

The semantic recipes are shared between JobVision and Cando.

```text
JobVision → Vazirmatn
Cando     → IRANYekanX
```

Figma binds the Typography Text Styles' fontFamily to `02 Product / typography/font-family` (JobVision / Cando), so switching Product changes font identity without duplicating the semantic scale. The former `02 Brand / brand/Brand font` reference is obsolete and must not be used for new components.

Typography does not depend on Appearance. Exact Cando font style/weight compatibility remains subject to visual validation when IRANYekanX is available in the implementation environment.

## Weight roles

```text
Label   → 500 Medium
Body    → 400 Regular
Heading → 700 Bold
```

Do not create parallel typography families for Link, Error, Selected, Disabled, or other state/color meanings. Combine the typography role with the appropriate Semantic foreground or component state.

## Canonical fixed styles

### Label

| Figma style | Size / line height | Weight |
|---|---:|---:|
| `Label / XS` | 12 / 16px | 500 |
| `Label / SM` | 14 / 20px | 500 |
| `Label / MD` | 16 / 24px | 500 |

Use Label for short UI labels, metadata, captions, and control-supporting text. Do not use it as general body copy.

### Body Compact

| Figma style | Size / line height | Weight |
|---|---:|---:|
| `Body / Compact / XS` | 12 / 16px | 400 |
| `Body / Compact / SM` | 14 / 20px | 400 |
| `Body / Compact / MD` | 16 / 24px | 400 |

Use Compact when vertical density matters and the content is short, component-level copy. Wrapping to one or two lines does not by itself require switching to regular Body. Do not use Compact for paragraph-like or reading-oriented content.

### Body

| Figma style | Size / line height | Weight |
|---|---:|---:|
| `Body / XS` | 12 / 20px | 400 |
| `Body / SM` | 14 / 24px | 400 |
| `Body / MD` | 16 / 28px | 400 |

`Body / SM` is the default readable Product body style. Prefer Body for paragraph-like, reading-oriented content, or copy expected to run beyond a short one-to-two-line UI message. Choose Body versus Compact by content role and expected reading length, not by incidental wrapping caused by container width.

### Heading Compact

| Figma style | Size / line height | Weight |
|---|---:|---:|
| `Heading / Compact / XS` | 12 / 16px | 700 |
| `Heading / Compact / SM` | 14 / 18px | 700 |
| `Heading / Compact / MD` | 16 / 22px | 700 |

Use Compact Heading for short, dense component titles where vertical space matters.

### Heading

| Figma style | Size / line height | Weight |
|---|---:|---:|
| `Heading / XS` | 12 / 18px | 700 |
| `Heading / SM` | 14 / 20px | 700 |
| `Heading / MD` | 16 / 24px | 700 |
| `Heading / LG` | 18 / 28px | 700 |
| `Heading / XL` | 20 / 28px | 700 |
| `Heading / 2XL` | 24 / 32px | 700 |
| `Heading / 3XL` | 32 / 40px | 700 |
| `Heading / 4XL` | 42 / 52px | 700 |

Regular Heading is the default hierarchy family and may wrap. Do not use Compact merely because a heading is visually small.

## Fluid Heading

Fluid Heading is reserved for large responsive page/layout headings. The recipe owns its responsive size and line-height behavior; Product code should not manually recreate the breakpoint mapping.

| Figma style | SM | LG | Weight |
|---|---:|---:|---:|
| `Heading / Fluid / XL` | 18 / 28px | 20 / 28px | 700 |
| `Heading / Fluid / 2XL` | 20 / 28px | 24 / 32px | 700 |
| `Heading / Fluid / 3XL` | 24 / 32px | 32 / 40px | 700 |
| `Heading / Fluid / 4XL` | 32 / 40px | 42 / 52px | 700 |

The Fluid tier reaches the same-named fixed Heading tier at the large mode and generally steps down at the small mode.

Figma's `Breakpoint = SM | LG` modes are design-time typography modes. They are not the full runtime Responsive Layout breakpoint scale.

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

## Live references

- Figma Typography page: current Text Styles and usage rules are the editable visual source.
- Runtime adapter syntax and generated artifact: pending Frontend implementation review.
