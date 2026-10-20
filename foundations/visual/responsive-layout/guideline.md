---
id: design-system.foundation.responsive-layout
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout
summary: Canonical guidance for viewport ranges, breakpoint ruler values, page types, layout regions, content containers, responsive strategies, container queries, and responsive testing.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-12
related:
  - design-system.foundation.layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.responsive-layout
  - design-system.reference.tailwind
---

# Responsive Layout

Responsive layout separates six decisions that should not be collapsed into one breakpoint system:

1. **Viewport ranges** — high-level page and navigation structure.
2. **Breakpoint ruler values** — fine-tuning thresholds for specific responsive scenarios.
3. **Page types and layout regions** — how shared regions compose into Full, Split, and Interstitial pages.
4. **Content containers** — how far a content region is allowed to grow.
5. **Responsive strategies** — how regions transform when available space changes.
6. **Container queries** — component or pane adaptation based on its own available width.

The model is intentionally close to Primer's responsive foundation because it supports both content-focused pages and dense multi-region application layouts without tying the Foundation to a specific product.

## Viewport ranges

Viewport ranges are the primary semantic states for page-level responsive behavior.

| Range | Width | Major layout regions | Intended use |
|---|---:|---:|---|
| `narrow` | `< 768px` | 1 | Mobile / compact page structure |
| `regular` | `>= 768px` | Up to 2 | Desktop-friendly patterns may begin |
| `wide` | `>= 1400px` | Up to 3 | Optional third region or wide workspace |

Use viewport ranges for navigation affordance, stacking/separating major page regions, persistent panes, and optional third-region behavior.

Entering `regular` does **not** mean every page must immediately become multi-column. A page may keep a compact composition until its own content constraints fit.

## Breakpoint ruler

Breakpoint tokens are shared numeric ruler values. They are not device categories and do not each define a new page mode.

| Token | Value | Tailwind adapter |
|---|---:|---|
| `xsmall` | `320px` | `xs` |
| `small` | `544px` | `sm` |
| `medium` | `768px` | `md` |
| `large` | `1012px` | `lg` |
| `xlarge` | `1280px` | `xl` |
| `xxlarge` | `1400px` | `2xl` |

Use these values to fine-tune behavior when the three viewport ranges are too coarse. A global breakpoint must not be added for a one-off component; use a local media query or container query instead.

## Breakpoint source contract

Breakpoint values have one canonical Design System source of truth. That source generates Design System responsive CSS, Product framework configuration such as Tailwind `screens`, and any other shared runtime adapter.

Do not manually maintain a second set of breakpoint numbers in Product configuration. The Design System package remains framework-agnostic and does not depend on Tailwind. Exact machine-readable source format, generated module format, import path, and build integration are Frontend-owned.

Figma's `Typography breakpoint` collection is a separate design-time mechanism for Fluid Heading size/line-height and must not be treated as the runtime breakpoint scale.

## Content and pane padding

Padding belongs to the content or pane region itself. Do not add a second outer page-padding wrapper around a normal constrained content container.

| Breakpoint | Content padding | Pane padding |
|---|---:|---:|
| `xsmall` | `16px` | `16px` |
| `small` | `16px` | `16px` |
| `medium` | `16px` | `16px` |
| `large` | `16px` | `16px` |
| `xlarge` | `24px` | `16px` |
| `xxlarge` | `24px` | `16px` |

A container's max-width **includes its own horizontal padding**. Example: an `xlarge` container has a maximum outer width of `1280px`; with `24px` padding on both sides, the maximum visually usable inner width is `1232px`.

## Content containers

| Role | Maximum width | Typical use |
|---|---:|---|
| `interstitial` | `320px` | Sign-in, verification, focused single-task screens |
| `medium` | `768px` | Focused forms and narrow content |
| `large` | `1012px` | Settings, larger forms, constrained application pages |
| `xlarge` | `1280px` | Default centered Full page |
| `full` | `100%` | Operational workspace and split layouts that need all available space |

The numeric max-width includes the region's padding.

## Page types

### Full page

Use for ordinary centered pages. Default to `xlarge = 1280px`. Use `medium` or `large` when the task benefits from a narrower form or reading width.

Use `xlarge` as the default for ordinary centered pages unless the task benefits from a narrower container.

### Split page

Use for navigation, filtering, list-detail, persistent panes, and operational workspaces.

Compose Split pages from logical **Start Pane / Content / End Pane** regions as needed.

Rules:
- Start/End pane width is outside the constrained Content max-width;
- the Content region may be `full`, `medium`, `large`, or `xlarge`;
- if constrained, center Content inside the **remaining main region**, not relative to the full viewport;
- direction is independent from the layout contract; in RTL products, Start Pane appears on the right;
- use independent scrolling only when the pattern requires it and accessibility remains intact.

#### Full operational workspace

Data-heavy tables, boards, management views, and similar operational pages should normally use Split page + `full` Content. There is no page-level max-width for the operational workspace. Use container queries for internal panes/components that become constrained.

#### Constrained task inside a Split page

Keep the same Split-page shell, but constrain the primary task when useful: `medium` for focused forms and `large` for settings or larger task flows. Center constrained Content inside the remaining main region after Start/End panes are accounted for.

#### List-detail

Treat list-detail as a Split page. The `regular` range begins at `768px`, but this does not force list-detail to split at `768px`. Use a fine-tune threshold such as `large = 1012px` or a container query when the minimum list + detail widths actually fit.

### Interstitial page

Use for sign-in, verification, focused loading/transition tasks, and similar single-purpose experiences. Default maximum width: `320px`.

## Layout regions

Page types are compositions of a small shared region vocabulary:

- **Header** — page-level header/chrome when present.
- **Start Pane** — primary edge pane; appears on the right in RTL and left in LTR.
- **Content** — the primary task/content region.
- **End Pane** — secondary edge pane; appears on the left in RTL and right in LTR.
- **Footer** — page-level footer when present.

Use logical Start/End names in Design System and implementation contracts. Avoid encoding physical direction in region names such as `Right pane` or `Left pane`.

A page type does not require every region. For example:
- Full pages normally center Content and may include Header/Footer.
- Split pages add Start Pane and/or End Pane around Content.
- Interstitial pages normally use only focused Content plus minimal surrounding chrome.

## Responsive strategies

When available space shrinks, do not assume every region should simply stack. Choose the transformation that best preserves task continuity and information hierarchy:

1. **Split into views** — for master/detail or list/detail flows, Narrow may navigate between views instead of rendering both at once.
2. **Pane → overlay** — filters and secondary panes may become a drawer, sheet, or bottom sheet when persistent pane width is unavailable.
3. **Stack** — place secondary content below primary content when reading order remains clear and the workflow stays coherent.

Hide or remove a region only when its information/action is genuinely non-essential at that width; responsiveness must not silently make required functionality unreachable.

## Local layout inside regions

Use Flexbox, CSS Grid, or other local layout primitives inside a region when they best fit the composition.

The Responsive Layout Foundation does **not** define a canonical global 4/8/12-column grid, global column count, or global gutter scale. Column count and track definitions are local layout decisions unless a separate repeated cross-product need is explicitly promoted later.

The previous experimental `Grid/Base`, `Grid/MD`, `Grid/LG`, and `Grid/XL` Figma styles remain legacy working artifacts only.

## Container queries

Use a container query when a reusable component or pane should react to its own available width rather than the full viewport. Good candidates include cards, result rows, filter bars, toolbars, summaries, chart panels, and master-detail subregions.

Viewport range and container query may be active at the same time. The page can be in `wide` while a candidate-list pane is still narrow enough to require its compact component composition.

## Reference design and QA widths

### Primary design frames

| Purpose | Width |
|---|---:|
| Compact mobile reference | `390px` |
| Regular-range boundary | `768px` |
| Large fine-tune reference | `1012px` |
| XLarge container reference | `1280px` |
| Primary wide desktop design | `1440px` |

### Responsive QA

Test both sides of meaningful thresholds: `320`, `543`, `544`, `767`, `768`, `1011`, `1012`, `1279`, `1280`, `1399`, `1400`, and `1920px`.

Also test intermediate fluid widths, RTL, text expansion, 200% zoom/reflow, keyboard navigation, and pane open/closed states where applicable.

## Figma contract

Published `Responsive layout` variables:

```text
breakpoint/xsmall      320
breakpoint/small       544
breakpoint/medium      768
breakpoint/large      1012
breakpoint/xlarge     1280
breakpoint/xxlarge    1400

container/interstitial 320
container/medium       768
container/large       1012
container/xlarge      1280

content-padding/default 16
content-padding/wide    24
pane-padding            16
```

The previous experimental `Grid/Base`, `Grid/MD`, `Grid/LG`, and `Grid/XL` styles are not part of the canonical responsive foundation. They remain hidden under `Legacy/Working/*` only to preserve existing bindings during migration.

The Figma page is named **Responsive layout** and documents viewport ranges, page types, canonical Layout regions, responsive strategies, and generic Full/Split/Interstitial examples.

## Related documents

- [`spec.md`](spec.md): atomic rules, decision tables, migration rules, and implementation requirements.
- [`patterns.md`](patterns.md): responsive behavior for common product patterns.
- [`examples/README.md`](examples/README.md): expectations for documenting product examples.
