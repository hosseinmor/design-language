---
id: design-system.token.typography.catalog
collection: design-system
type: token
title: Typography Token Catalog
summary: Approved semantic typography recipes, responsive heading styles, weights, and product-aware font mapping.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.foundation.typography
---

# Typography Token Catalog

These are the reviewed design-side recipe definitions. Figma owns editable Text Styles; code owns actual runtime implementation.

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
