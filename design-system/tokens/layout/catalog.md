---
id: design-system.token.layout.catalog
collection: design-system
type: token
title: Layout Token Catalog
summary: Reviewed responsive breakpoint, content-container and region-padding token identifiers and values; distinguishes published Figma variables from conceptual layout roles.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.foundation.layout
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.reference.tailwind
---

# Layout Token Catalog

This is the **one Markdown owner of approved numeric responsive-layout token declarations**. The live editable source is the Figma **Responsive layout** variables; code and Tailwind own generated runtime adapters. Inspect Figma for current live values before asserting implementation parity.

## Breakpoint ruler

| Token | Value | Intended Tailwind adapter |
|---|---:|---|
| `breakpoint/xsmall` | 320px | `xs` |
| `breakpoint/small` | 544px | `sm` |
| `breakpoint/medium` | 768px | `md` |
| `breakpoint/large` | 1012px | `lg` |
| `breakpoint/xlarge` | 1280px | `xl` |
| `breakpoint/xxlarge` | 1400px | `2xl` |

The six ruler values are **not six viewport modes**. The [Responsive Layout Guideline](../../../foundations/visual/responsive-layout/guideline.md) defines semantic `narrow / regular / wide` layout ranges and when to fine-tune locally. Tailwind keys are intended adapter names, not evidence of a shipped package.

## Content container values

| Token | Value | Source status |
|---|---:|---|
| `container/interstitial` | 320px | Published Figma variable |
| `container/medium` | 768px | Published Figma variable |
| `container/large` | 1012px | Published Figma variable |
| `container/xlarge` | 1280px | Published Figma variable |
| `container/full` | 100% | Conceptual layout role; not part of the listed published numeric Figma variables |

Container maximum widths include the Content region's own horizontal padding. `full` means unconstrained within the available main region, not a separate numeric Figma token that must be published.

## Content and pane padding

| Token | Value | Intended use |
|---|---:|---|
| `content-padding/default` | 16px | Content through the `large` breakpoint |
| `content-padding/wide` | 24px | Content from `xlarge` onward |
| `pane-padding` | 16px | Start/End panes across breakpoint ranges |

All three padding values are published Figma variables. These Layout-specific tokens express the use of values from the shared Spacing scale; they are **not** an alternative global spacing scale.

## Contract boundaries

- The [Layout Foundation](../../../foundations/visual/layout.md) owns layout design principles and future density/alignment conventions.
- The [Responsive Layout Guideline](../../../foundations/visual/responsive-layout/guideline.md) owns human-facing page/range/region decisions.
- The [Atomic Specification](../../../foundations/visual/responsive-layout/spec.md) owns numbered requirements (`RSP-*`) and testing/implementation constraints.
- [Responsive Layout Patterns](../../../foundations/visual/responsive-layout/patterns.md) owns **draft** adaptation guidance for compositions.
- Do not independently edit or hard-code these values in Tailwind, other Design Language documents, or Product UI. The actual source/generation pipeline remains Frontend-owned; the values documented here are reviewed design contracts, not proof of a built code package.
