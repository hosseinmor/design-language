---
id: design-system.component.tabs
collection: design-system
type: component
title: Tabs
summary: Tabs switch between peer content panels within the same context using one current tab.
knowledge_state: verified
document_maturity: reviewed
last_reviewed: '2026-10-14'
related:
  - design-system.component.content-switcher
  - design-system.reference.component-mapping
  - design-system.accessibility.keyboard-navigation
---

# Tabs

## Purpose

Tabs organize peer sections of related information within one product context. Activating a Tab reveals its associated panel while the other peer panels are hidden.

Use Tabs when the user is moving between **content sections at the same contextual level**.

A Tab may participate in deep linking or update the URL. URL change alone does not turn Tabs into Navigation. The deciding question is whether the user remains in the same contextual container and switches its peer panel, or moves to a different destination in the product information architecture.

## When to Use

Use Tabs when:

- several peer content panels belong to the same context;
- exactly one peer panel is current at a time;
- keeping the peer sections visible as choices improves orientation;
- changing the current Tab replaces the associated panel rather than filtering the same panel.

Examples include details / activity / settings sections of one entity, or peer subviews inside one product area.

## When Not to Use

Do not use Tabs when:

- the user is moving to another product destination or information-architecture branch; use Navigation;
- the user is switching the representation or mode of the **same content** such as List / Grid or Day / Week / Month; use Content Switcher / Segmented Control;
- the user is applying predicates to the same collection; use Filter controls;
- the controls reflect scroll position within one continuous page; use an in-page navigation / scrollspy pattern;
- the choices are form values; use Choice Group, Radio, Checkbox, Select, or another appropriate selection control.

## Boundary: Tabs vs Content Switcher

Tabs and Content Switcher are both single-current-choice controls, but they answer different questions.

| Pattern | User is changing |
|---|---|
| Tabs | Which peer content section is visible? |
| Content Switcher / Segmented Control | How is the same content represented or viewed? |

JobVision's canonical Content Switcher owns the connected segmented / pill-like mode-switching treatment.

For this reason, canonical Tabs v1 intentionally supports **Line only**. The legacy Chip and Contained Tab appearances are not part of the public contract. A future pill-style Tab appearance requires a validated product use case that is semantically Tabs and cannot be served by Content Switcher.

## Anatomy

### Tabs

The public Tabs component contains:

1. an `Items` native Slot;
2. a shared subtle bottom line;
3. two or more `_Tab Item` instances.

The item count is composition, not a variant axis.

### _Tab Item

A Tab Item supports three content modes:

1. `Text`;
2. `Text + Icon`;
3. `Icon only`.

All modes share the same selection indicator and interaction states.

Text and Text + Icon use zero inline padding so the first and last labels can align flush with surrounding content. Icon-only stays a fixed `40×40px` hit target.

The `Label` property remains required in every mode. In Icon-only mode it is not visually rendered, but it is the canonical authoring source for the runtime accessible name.

## Figma Property Model

### Tabs / Default

Tabs is a standalone public component rather than a Component Set with appearance, size, count, or alignment axes.

| Property | Type | Notes |
|---|---|---|
| `Items` | native Slot | variable Tab Item composition |

The default authoring composition contains four Tab Items with exactly one Selected.

### _Tab Item

| Property | Values / type | Notes |
|---|---|---|
| `Content` | `Text / Text + Icon / Icon only` | presentation mode |
| `State` | `Default / Hover / Active / Focus / Selected / Selected Focus / Disabled` | compact visual state model |
| `Label` | Text | visible in Text modes; accessible-name source in Icon-only |
| `Icon` | Instance swap | shared icon-library source |

Variant count: **21 = 3 Content × 7 State**.

There is deliberately no Appearance, Size, Alignment, Selected Boolean, Skeleton, Direction, or item-count axis.

## Selection Model

Exactly one Tab in an active tablist is Selected.

Selection is represented directly by `State=Selected`; do not add a redundant `Selected=True/False` axis.

Because the current Tab remains keyboard-focusable, `Selected Focus` is an explicit authored state. This avoids multiplying every interaction state by a separate Selected Boolean while still representing the accessibility-critical selected + focus combination.

Selected does not need Hover or Active Cartesian variants in Figma.

## Size and Spacing

Canonical v1 uses one density:

- Tab height: **40px**
- Text / Text + Icon inline padding: **0px**
- Label: **Label/SM** — Vazirmatn **14/20 Medium (500)**
- Icon: **18px**
- Text + Icon internal gap: **8px**
- Icon-only item: **40×40px**
- inter-item gap owned by Tabs: **24px**

The selected label keeps the same Label/SM weight as every other state; selection must not create layout shift.

Tab Items hug their content by default.

Equal-width Tabs may be composed by a consuming layout when the product has a clear reason to distribute peer sections evenly, but equal width is not a Tabs variant axis.

## Visual Treatment

### Shared tablist line

Tabs owns a 1px bottom line using `line/default`.

### Default

- transparent surface;
- Label / Icon: `fg/secondary`; both must use the same semantic foreground token.

### Hover

- no background;
- Label / Icon: `fg/primary`; both must use the same semantic foreground token.

### Active

- no background;
- Label / Icon: `fg/primary`;
- 2px neutral bottom indicator: `line/emphasis`.

### Focus

- base content uses `fg/primary`;
- shared focus-visible treatment:
  - 2px visible `focus/default` outer ring;
  - 1px visual gap using the normal surface;
  - no geometry change.

### Selected

- Label / Icon: `fg/primary`;
- 2px bottom indicator: `line/accent`;
- no font-weight change.

### Selected Focus

Preserve the Selected indicator and add the shared focus-visible ring.

### Disabled

- Label / Icon: `fg/disabled`; both must use the same semantic foreground token;
- no Hover / Active treatment.

## Content Modes

A single tablist should use one content mode consistently.

### Text

Default mode. Use concise, parallel labels.

### Text + Icon

Use when the icon materially improves recognition of every peer Tab. Do not add icons decoratively to only some Tabs in the same tablist.

### Icon only

Supported for compact contexts where every icon is familiar and unambiguous.

- Icon-only items remain `40×40px`.
- Every Icon-only Tab requires a programmatic accessible name; use the Tab Item `Label` authoring property as the source.
- Use the shared icon library; do not redraw icons inside Tabs.
- The consuming Tab Item must override the shared icon source color so the Icon exactly matches the Label semantic foreground in every state.
- If the icons are not immediately understandable in context, use Text instead.

Do not mix Text, Text + Icon, and Icon-only items within the same tablist.

## Counter / Badge

Legacy Tabs contained an optional Tag-based counter.

That implementation is not canonical because numeric count is not categorical Tag content.

Canonical Tabs v1 does not hard-wire a counter until the shared Badge/count primitive and repeated Tabs use case are validated. Do not reuse Tag merely to preserve the legacy appearance.

## Overflow and Long Labels

Tabs stay on one line.

- Never wrap a tablist into multiple rows.
- Tab labels remain single-line and should be concise.
- Prefer content-width / Hug items.
- When the tablist exceeds available width, the runtime should preserve one line using horizontal scrolling or another accessible overflow mechanism.
- Canonical Figma does not expose Previous / Next overflow buttons.
- Exact scroll controls, scroll snapping, measurement, and overflow algorithm remain runtime-owned and unverified.
- Do not introduce a hard item-count maximum solely from Figma.

If the set of peer sections becomes difficult to scan even with overflow, reconsider the information architecture rather than adding more Tab variants.

## Nested Tabs

A second Tabs level may be used only when a true peer-panel relationship exists inside the selected parent panel and the hierarchy remains obvious.

More than two visible Tabs levels should trigger an information-architecture review rather than another visual hierarchy variant.

Nested Tabs reuse the canonical Line component; canonical v1 does not add Primary / Secondary visual axes.

## Responsive Behavior

- Keep Tabs single-line.
- Preserve the 40px control height.
- Let item widths hug their labels.
- Use horizontal overflow rather than wrapping.
- Do not switch to Content Switcher solely because the viewport became narrow; the semantic role must stay correct.
- If the content model no longer fits a tablist on small screens, the product may choose an alternate navigation pattern, but that is a responsive product-pattern decision rather than a hidden Tabs variant.

## Accessibility Contract

Tabs follow the WAI-ARIA Tabs pattern.

The owning runtime must provide the semantic relationship among:

- `tablist`;
- each `tab`;
- each associated `tabpanel`.

Exactly one peer panel is current in the normal single-select Tabs pattern.

Keyboard contract:

- `Tab` / `Shift+Tab` enters or leaves the composite; focus enters on the active Tab;
- horizontal Arrow keys move focus among Tabs according to the resolved runtime direction / platform behavior;
- `Home` moves to the first Tab and `End` to the last when those keys are supported by the owning implementation;
- in manual activation, `Enter` or `Space` activates the focused Tab;
- automatic activation is appropriate only when panel switching has no perceptible latency;
- keyboard focus remains visibly distinct from Selected state.

The active Tab must expose its selected state programmatically, and each Tab / Tabpanel relationship must be programmatically determinable.

The exact DOM elements, framework props, routing integration, roving-tabindex implementation, and automatic-vs-manual activation policy remain unverified until the owning runtime source is registered.

## RTL

RTL/LTR is not a Figma variant axis.

- Compose Tabs in logical reading order for the product language.
- Persian/Arabic labels use RTL text direction.
- The selected indicator stays on the logical Tab Item itself and does not require mirroring.
- Runtime Arrow-key behavior must be verified in the owning implementation rather than inferred from Figma layer order.

## Loading

Skeleton is not a Tab interaction state.

If the tabbed region is loading, use the shared Skeleton/loading pattern at the appropriate content or composition level rather than multiplying the Tab Item state matrix.

## Migration from Legacy Tabs

The previous Figma model contained:

- `Type = Line / Contained / Chip`;
- `Size = Small / Medium / Large / Expressive`;
- `Alignment = Auto-width / Grid aware`;
- `State = Enabled / Hover / Focus / Selected / Disabled / Skeleton`;
- redundant `Selected = False / True`;
- Icon-only mode;
- fixed hidden item-count compositions;
- Previous / Next overflow-button variants.

These are retained only as legacy migration references in Figma.

Canonical replacements:

- Line only;
- one 40px size;
- Hug items by default;
- compact `Content × State` internal Tab Item;
- native Items Slot for variable count;
- no Skeleton interaction state;
- no overflow-arrow API;
- `Text / Text + Icon / Icon only` content modes;
- zero inline padding for text modes with 24px parent-owned inter-item gap;
- no Tag-based counter.

## Figma Reference

Canonical file: `[DS] Job Vision NEXT`

File key: `rROD8ctH9UfPGAMrRrOzHe`

### Tabs

- Component: `Tabs / Default`
- Figma node ID: `23486:300`
- Component key: `d79023ff7c2575d09ea714814c8d7e75fbac1662`
- Content property: `Items` native Slot
- Default height: `40px`

### _Tab Item

- Internal Component Set: `_Tab Item`
- Figma node ID: `23486:299`
- Component key: `883007580c6e232e8ca2ba70a64c90ed80b73067`
- Variant properties: `Content / State`
- Content: `Text / Text + Icon / Icon only`
- States: `Default / Hover / Active / Focus / Selected / Selected Focus / Disabled`
- Content properties: `Label / Icon`
- Variant count: `21`

### Documentation

- Frame: `Tabs / Documentation`
- Node ID: `23488:286`

### Legacy identities

- `Legacy / Tabs` — node `3890:50605`
- `Legacy / _Tabs Item` — node `5658:278361`
- `Legacy / Tabs Overflow Button` — node `5662:278514`
- `Legacy / Tabs Skeleton Item` — node `5657:278356`

Do not use Legacy components for new design.

## TBD / Future Exploration

The following are deliberately **not part of the current developer contract** and must not be inferred as supported variants:

### Vertical Tabs

TBD. Explore only after a real product use case is validated. The future review must cover:

- whether the pattern is still semantically Tabs rather than local navigation;
- vertical keyboard behavior;
- selected-indicator placement;
- width, truncation, and overflow;
- RTL geometry.

### Pill-style Tabs

TBD. Explore only if a real use case is semantically Tabs and needs stronger visual differentiation — for example a validated second-level Tabs case — and cannot be served cleanly by Content Switcher / Segmented Control.

Until then:

- Level 1 Tabs use the canonical Line appearance.
- Level 2 Tabs, when genuinely needed, reuse the same Line appearance and rely on placement/context for hierarchy.
- Do not introduce a Pill appearance solely to distinguish hierarchy.

## Runtime / Storybook Boundary

Owning runtime Design System repository/package: **Unregistered**

Runtime component/API: **Unverified**

Storybook: **Unregistered**

Figma property → runtime prop mapping: **Unverified**

Do not infer exact DOM structure, event names, route behavior, activation mode, overflow implementation, or prop names from Figma.

## QA Checklist

Verify:

- public Tabs exposes only the Items Slot;
- internal Tab Item exposes only Content / State / Label / Icon;
- exactly one item is Selected in normal usage;
- Selected Focus preserves both current indicator and focus-visible treatment;
- every state remains 40px high;
- changing Label content changes width without changing height;
- selected text keeps Label/SM and does not shift layout;
- Text and Text + Icon items use 0px inline padding and hug content;
- Tabs owns a 24px inter-item gap;
- Icon-only items stay 40×40px;
- each tablist uses one Content mode consistently;
- no tablist wraps;
- long-label and narrow-overflow examples remain single-line;
- Icon-only Tabs retain a Label value for the accessible-name source;
- Hover has no background; Active uses a 2px `line/emphasis` indicator; Selected uses a 2px `line/accent` indicator;
- Disabled content uses `fg/disabled`;
- RTL authoring remains visually correct;
- legacy Contained / Chip / Size / Grid-aware / Skeleton / overflow-arrow APIs do not appear in canonical components.

## Benchmark Evidence

Canonical v1 is aligned to the stable cross-system pattern:

- WAI-ARIA APG defines Tabs as one visible panel selected from a tablist and establishes composite keyboard behavior.
- Carbon Tabs uses transparent unselected line tabs with secondary content color and an interactive selected bottom indicator.
- Spectrum Tabs treats the selection indicator as part of the Tabs anatomy for related sections in one context.
- Primer separates linked tab navigation from in-place tab panels while preserving the broader underline-tab visual family.

External systems are evidence, not runtime sources for JV.

## Related Documents

- `content-switcher.md`
- `../../foundations/interaction/selection.md`
- `../tokens/semantic-tokens.md`
- `../../accessibility/keyboard-navigation.md`
- `../../accessibility/focus-management.md`
- `../../integrations/component-mapping.md`
