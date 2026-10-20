---
id: design-system.foundation.responsive-layout-spec
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout Specification
summary: Atomic rules and decision tables for viewport ranges, breakpoint ruler values, page types, layout regions, containers, responsive strategies, and responsive implementation.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.foundation.responsive-layout
  - design-system.pattern.responsive-layout
  - design-system.reference.tailwind
---

# Responsive Layout Specification

## Viewport ranges

| Range | Query intent | Major layout regions |
|---|---|---:|
| `narrow` | width below `768px` | 1 |
| `regular` | width at or above `768px` | Up to 2 |
| `wide` | width at or above `1400px` | Up to 3 |

Viewport ranges are the preferred semantic API for high-level page structure.

## Breakpoint ruler

| Token | Value | Tailwind adapter |
|---|---:|---|
| `xsmall` | `320px` | `xs` |
| `small` | `544px` | `sm` |
| `medium` | `768px` | `md` |
| `large` | `1012px` | `lg` |
| `xlarge` | `1280px` | `xl` |
| `xxlarge` | `1400px` | `2xl` |

Breakpoint values are ruler values for fine-tuning. They must not be interpreted as six separate page modes.

Generated runtime artifacts must originate from one canonical Design System source. Tailwind, CSS custom media, or other framework outputs must not re-author these numbers independently.

## Container and padding tokens

| Token | Value |
|---|---:|
| `container/interstitial` | `320px` |
| `container/medium` | `768px` |
| `container/large` | `1012px` |
| `container/xlarge` | `1280px` |
| `container/full` | `100%` |
| `content-padding/default` | `16px` |
| `content-padding/wide` | `24px` |
| `pane-padding` | `16px` |

Content padding is `16px` through `large`, then `24px` at `xlarge` and `xxlarge`. Pane padding remains `16px`.

A numeric container max-width includes its horizontal padding.

## Rules

### RSP-001 — Use viewport ranges for page structure

- **Rule:** Prefer `narrow / regular / wide` for high-level page and navigation adaptations.
- **Requirement:** Do not create a new page mode at every breakpoint ruler value.
- **Example:** Entering `regular` at `768px` permits desktop-friendly patterns but does not force a list-detail split.

### RSP-002 — Breakpoints are ruler values, not devices

- **Rule:** `xsmall / small / medium / large / xlarge / xxlarge` are shared numeric thresholds.
- **Incorrect:** `large = desktop device`.
- **Correct:** `large = 1012px`, usable as a fine-tune threshold when needed.
- **Requirement:** Device labels may appear only as non-normative examples.

### RSP-003 — Fine-tune locally before adding global semantics

- **Rule:** Use the shared breakpoint ruler or a local query for responsive cases not expressed by viewport ranges.
- **Requirement:** Do not add a global breakpoint for one page or component.
- **Fallback:** Prefer a container query when the dependency is the parent region's width.

### RSP-004 — Use container queries for reusable components and panes

- **Rule:** A reusable component should respond to its own container width when viewport width is not a reliable proxy.
- **Includes:** cards, toolbars, result rows, filter bars, candidate panes, chart panels, and master-detail subregions.

### RSP-005 — Keep container width independent from viewport range

- **Rule:** Viewport range determines page structure; container role determines content growth.
- **Requirement:** Do not create a new breakpoint only to impose a max-width.

### RSP-006 — Container max-width includes padding

- **Rule:** Horizontal content padding belongs to the content region itself.
- **Requirement:** Numeric container max-width includes that padding.
- **Incorrect:** `1280px` max-width wrapper plus an additional outer `24px` page padding layer for the same region.
- **Correct:** `1280px` content region whose internal padding is `24px` per side.

### RSP-007 — Use semantic page types

- **Full page:** centered constrained Content; default `xlarge = 1280px`.
- **Split page:** Start Pane and/or End Pane plus Content; Content may be `full / medium / large / xlarge`.
- **Interstitial page:** focused single-task Content; default `320px`.

### RSP-008 — Use logical layout-region names

- **Canonical regions:** `Header / Start Pane / Content / End Pane / Footer`.
- **Rule:** Start/End describe logical page edges, not physical left/right.
- **RTL:** Start Pane is on the right and End Pane is on the left.
- **LTR:** Start Pane is on the left and End Pane is on the right.
- **Requirement:** Do not encode direction into canonical region names such as `Right pane` or `Left pane`.

### RSP-009 — Split-page panes are outside Content max-width

- **Rule:** Start/End pane width does not consume the numeric max-width token of Content.
- **Requirement:** If Content is constrained, center it in the remaining main region, not the full viewport.

### RSP-010 — Operational workspaces use Full Content

- **Rule:** Data tables, boards, management views, and similar operational pages normally use Split page + `full` Content.
- **Requirement:** Do not impose a page-level max-width on a dense operational workspace.
- **Requirement:** Use container queries for constrained internal panes/components.

### RSP-011 — Constrain focused tasks when useful

- **Rule:** Forms, settings, and other focused tasks may keep the Split-page shell while constraining Content.
- **Preferred roles:** `medium = 768px` for focused forms; `large = 1012px` for larger settings/application pages.

### RSP-012 — Ordinary Full pages default to XLarge

- **Rule:** New ordinary centered Full pages should default to `xlarge = 1280px` unless the content benefits from another role.

### RSP-013 — List-detail uses Split-page behavior

- **Rule:** List-detail does not automatically split at the start of `regular`.
- **Preferred mechanism:** Use a fine-tune threshold such as `large = 1012px` or a container query when list + detail minimum widths fit.

### RSP-014 — Remain fluid between thresholds

- **Rule:** Layouts must work throughout every interval, not only at reference widths.
- **Requirement:** No unintended overflow, overlap, inaccessible actions, or accidental horizontal page scrolling.

### RSP-015 — Name variants by behavior

- **Incorrect:** `Card / Tablet`, `Modal / Desktop`.
- **Correct:** `Card / Vertical`, `Card / Horizontal`, `Modal / Dialog`, `Modal / Full-screen`.

### RSP-016 — Do not infer input capability from width

- **Rule:** Width must not be used to assume touch, mouse, hover, or keyboard support.
- **Requirement:** Essential actions must not depend on hover.
- **Requirement:** Pointer/hover refinements use capability media features.

### RSP-017 — Keep RTL independent from responsive thresholds

- **Rule:** Threshold values are direction-independent.
- **Preferred CSS:** logical properties such as `padding-inline`, `margin-inline`, `inset-inline-start`, and `border-inline-end`.

### RSP-018 — Stable UI typography by default

- **Rule:** Body, Label, Button, and ordinary UI text do not receive a new type size at each breakpoint.
- **Requirement:** Use the Typography Foundation; Fluid Heading owns its approved design-time responsive mapping separately.

### RSP-019 — Test boundaries and ranges

Minimum responsive QA widths:

`320`, `543`, `544`, `767`, `768`, `1011`, `1012`, `1279`, `1280`, `1399`, `1400`, and `1920px`.

Also test intermediate widths, content expansion, RTL, 200% zoom/reflow, keyboard navigation, and side pane open/closed states.

### RSP-020 — Choose a responsive transformation explicitly

- **Split into views:** use when master/detail or list/detail should become navigable separate views in Narrow.
- **Pane → overlay:** use when a persistent filter/secondary pane should become a drawer, sheet, or bottom sheet.
- **Stack:** use when vertical order preserves comprehension and task continuity.
- **Requirement:** Do not default every multi-region page to stacking.
- **Requirement:** Required actions/information must remain reachable after the transformation.

### RSP-021 — Keep column grids local

- **Rule:** Flexbox and CSS Grid remain normal local layout tools inside Header, Content, Start Pane, End Pane, and Footer regions.
- **Requirement:** Do not treat 4/8/12 columns, global gutters, or Figma Grid styles as canonical Responsive Layout tokens.
- **Legacy:** `Grid/Base`, `Grid/MD`, `Grid/LG`, and `Grid/XL` are retained only as hidden `Legacy/Working/*` bindings during migration.
- **Promotion rule:** Add a shared grid contract only if a repeated cross-product requirement cannot be expressed cleanly through page types, regions, containers, spacing, and local layout primitives.

## Page-type decision table

| Situation | Preferred page/layout |
|---|---|
| Ordinary centered page | Full / XLarge |
| Focused form | Full or Split / Medium |
| Settings or larger constrained task | Full or Split / Large |
| Data table / board / operational workspace | Split / Full |
| List-detail | Split; fine-tune split threshold |
| Sign-in / verification / one-task screen | Interstitial |
| Reusable pane/component becomes cramped | Container query |
| List-detail cannot fit both regions | Split into views |
| Filter/secondary pane cannot remain persistent | Pane → overlay |
| Secondary content can follow primary content naturally | Stack |

## Tailwind mapping

Tailwind may map the shared ruler to custom screens:

| DS token | Tailwind key | Value |
|---|---|---:|
| `xsmall` | `xs` | `320px` |
| `small` | `sm` | `544px` |
| `medium` | `md` | `768px` |
| `large` | `lg` | `1012px` |
| `xlarge` | `xl` | `1280px` |
| `xxlarge` | `2xl` | `1400px` |

Tailwind screen keys are an implementation adapter over the breakpoint ruler. They do not replace `narrow / regular / wide` as page-layout semantics.

Exact custom media/variant implementation for viewport ranges and container queries remains Frontend-owned.

## Reference frames

| Purpose | Width |
|---|---:|
| Compact mobile reference | `390px` |
| Regular boundary | `768px` |
| Large fine-tune reference | `1012px` |
| XLarge container reference | `1280px` |
| Primary wide desktop design | `1440px` |

## Migration from current/legacy thresholds

Migration is behavior-led.

| Existing threshold/convention | Shared target direction |
|---|---|
| Bootstrap `576px` | Usually `small = 544px` or a local threshold |
| `768px` | `medium = 768px` |
| Bootstrap `1200px` | Usually `xlarge = 1280px` |
| `1400px` | `xxlarge = 1400px` / Wide range |

Do not change a threshold until navigation, tables, forms, panes, dialogs, content wrapping, and zoom/reflow have been checked across the affected width interval.

## Prohibited patterns

- Do not define page structure with six independent breakpoint modes.
- Do not name global breakpoints after devices.
- Do not add a global breakpoint for one component.
- Do not maintain a second hard-coded breakpoint scale in Product Tailwind configuration.
- Do not add outer page padding around a constrained content container that already owns its horizontal padding.
- Do not include Start/End pane width inside the Content max-width token.
- Do not encode physical direction into canonical layout-region names.
- Do not establish a global 4/8/12-column grid or global gutter contract without a new repeated cross-product requirement.
- Do not default every multi-region responsive transformation to stacking.
- Do not constrain dense operational workspaces with a global page max-width.
- Do not stretch reading/form content indefinitely on wide screens.
- Do not assume desktop width means hover or mouse.
- Do not design only at 390px and 1440px without checking boundary and intermediate behavior.
