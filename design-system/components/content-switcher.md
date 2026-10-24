---
id: design-system.component.content-switcher
collection: design-system
type: component
title: Content Switcher
summary: Content Switcher switches immediately between closely related views of the same content using one current choice.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-10-24'
related:
  - design-system.component.tabs
  - design-system.component.toggle-button
  - design-system.reference.component-mapping
---

# Content Switcher

## Purpose

Content Switcher is a compact single-select control for switching immediately between closely related views or representations of the same underlying content.

Use it when the user is changing how the same content is viewed, not where they are in the product and not whether a setting is on or off.

Do not use it:

- as primary or secondary navigation;
- for distinct information sections that should use Tabs;
- for a binary on/off preference that should use Toggle;
- as a generic form-field replacement for Radio or Select when choosing a data value;
- when more than five choices are needed.

## Canonical Figma Model

Canonical file: `[DS] Job Vision NEXT`

### Content Switcher

- Component set: `Content Switcher`
- Figma node ID: `23083:1746`
- Figma component key: `2d44a4df734823788a122e9a9c73fec3bd6e4ff2`
- Variant property: `Size = Small / Medium / Large`
- Content property: native `Items` SLOT
- Default: `Medium`
- Exactly three parent variants; no internal Size/Content variable modes
- Default authoring content: 3 equal-width items with exactly one `Selected`
- Recommended item count: 2–5
- Item count is composition, not a variant axis.

### _Content Switcher Item

- Internal component set: `_Content Switcher Item`
- Figma node ID: `23038:127212`
- Figma component key: `17b39a5fe6a7b1fbd1679202f90e2ca2a45aba35`
- Variant properties:
  - `State = Default / Hover / Active / Focus / Disabled / Selected`
  - `Content = Text / Icon`
- Content properties: `Label`, `Icon` instance swap
- Item instances fill the parent Slot vertically; Size is controlled by the parent without variable modes.
- Horizontal Item padding is fixed at `16px`.
- `Selected` is a terminal visual state in Figma; there are no `Selected + Hover/Active/Disabled` Cartesian variants.

## Composition

Use the parent `Content Switcher` component rather than assembling Item instances manually.

The `Items` Slot:

- contains 2–5 items;
- keeps every item equal width;
- stays on one line;
- never wraps;
- may be customized for count, labels/icons, and Item State;
- Item height fills the Slot, so parent Size changes remain automatic after Slot customization.

Exactly one item is `State=Selected`.

Do not create a zero-selected or multi-selected Content Switcher.

## Content Modes

Each Item has `Content = Text / Icon`.

Keep one Content value consistently across all Items in a Content Switcher.

Do not mix Text and Icon items within one control.

Do not use Icon + Text as a shared Content Switcher mode.

### Text

Use short, parallel labels that describe the alternate views.

Labels are single-line. If the available width cannot support clear labels, do not wrap them inside the control.

### Icon

Use Icon-only only when each icon is unambiguous in context.

- Icon size: `16px`
- The Item exposes the shared Icon instance swap.
- Shared source Icons retain the purple guard color in the Icon library.
- Content Switcher Item explicitly overrides Icon color by State:
  - Default → `fg/secondary`
  - Hover / Active / Focus / Selected → `fg/primary`
  - Disabled → `fg/disabled`
- Icon swap is verified to preserve the contextual foreground override.

If icons are not self-explanatory, use Text or switch to Menu/Select in constrained layouts.

## Size and Geometry

Total Content Switcher height aligns with the shared control scale:

| Size | Total height | Inner Item height | Horizontal Item padding |
|---|---:|---:|---:|
| Small | 32px | 28px | 16px |
| Medium | 40px | 36px | 16px |
| Large | 48px | 44px | 16px |

There is no XS size. Small is the compact floor.

The outer Track owns a 2px inset on all sides; the inset is included inside the total 32/40/48 height rather than added to it.

Geometry:

- Track radius: `8px` component-local value; do not bind the deprecated `8px Group` token.
- Item radius: canonical `6px · Medium` radius token
- Item gap: `2px`
- No divider between items
- No persistent Item border

Typography uses `Label/SM` (`14/20`, Medium), matching the shared Button control typography for Small/Medium/Large. This keeps the control aligned with adjacent Buttons/Inputs of the same Size.

## Visual Treatment

### Track

Track uses `surface/inset`.

`surface/inset` is the recessed structural surface behind the local `surface/default` Selected Item.

### Unselected states

```text
Default  → transparent + fg/secondary
Hover    → surface/transparent-hover + fg/primary
Active   → surface/transparent-active + fg/primary
Focus    → transparent + fg/primary + shared focus-visible ring
Disabled → transparent + fg/disabled
```

### Selected

```text
Selected surface → surface/default
Selected content → fg/primary
```

Selected is intentionally lightweight and does not introduce a separate Selected interaction matrix.

## Focus

The Figma Focus state represents keyboard `focus-visible`, not every programmatic or pointer focus event.

Visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) contract. It remains distinct from the selected segment treatment and must not change segment dimensions.

## Responsive Behavior

Do not wrap Content Switcher items.

When available width becomes too narrow, Icon-only may be used only when all icons remain unambiguous. Otherwise switch to an appropriate Menu/Select pattern rather than compressing labels past clarity.

Do not infer a fixed viewport breakpoint from the Figma examples.

## RTL

Do not create an RTL variant.

Compose Slot items in logical/visual reading order for the product direction. Persian/Arabic labels use RTL text direction.

No Position axis is required.

## Accessibility Contract

Content Switcher represents one current choice among alternate views of the same content.

The owning runtime must provide:

- one group-level accessible relationship for the choices;
- exactly one current/selected choice;
- keyboard access without requiring users to tab through every item independently when the chosen runtime pattern supports roving focus;
- arrow-key movement between choices where appropriate for the chosen runtime semantics;
- a visible focus indicator only for focus-visible;
- an accessible name for every Icon-only item.

The exact DOM element, ARIA role, event API, and framework implementation are deliberately unverified until the owning runtime Design System source is registered.

Do not infer runtime roles or prop names from Figma property names.

## Runtime Boundary

The owning JV Design System runtime repository/package is not registered in Design System Knowledge.

The verified Storybook source is also not registered.

Therefore the exact runtime component/API, DOM/ARIA implementation, keyboard implementation details, props/inputs/outputs, Storybook identifier, Figma-to-code prop mapping, and Code Connect mapping remain unverified.

## QA Checklist

Verify:

- Parent API contains only `Size / Items`.
- Item API contains `State / Content / Label / Icon`.
- Parent Size is `Small / Medium / Large`; no XS.
- Total heights are `32 / 40 / 48`.
- A customized Slot still follows parent Size changes through vertical Fill sizing.
- Text and Icon are Item Content variants; keep the same Content across all Items.
- Icon + Text is not authored as a shared mode.
- Exactly one Item is Selected.
- Selected has no redundant Hover/Active/Disabled variants.
- 2, 3, 4, and 5 Item compositions remain equal-width and single-line.
- Track remains distinguishable on default and neutral-muted surfaces.
- No deprecated Radius variables are bound in the canonical component masters.
- No internal Content Switcher Size/Content variable collections remain.
- Icon colors match Item State, including after Icon swap.
- Focus uses the shared focus-visible treatment.
- Disabled content uses `fg/disabled`.
- RTL composition remains correct.
- narrow examples do not wrap.

## Related Documents

- `tabs.md`
- `toggle-button.md`
- `../../accessibility/focus-management.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../../integrations/component-mapping.md`
