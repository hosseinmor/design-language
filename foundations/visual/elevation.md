---
id: design-system.foundation.elevation
collection: design-system
type: foundation
title: Elevation
summary: Defines the semantic shadow model for floating UI and active drag states, plus the boundaries for component-owned shadows.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: 2026-09-19
related:
  - design-system.reference.tailwind
---

# Elevation

## Model

Elevation is semantic and intentionally small. The Foundation does not expose a generic `small / medium / large` shadow ladder.

The public Foundation has two recipes:

```text
Shadow / Floating
Shadow / Dragged
```

They express different meanings, not adjacent visual levels.

## Shadow / Floating

Use Floating for temporary surfaces or controls that sit above surrounding page content without relying on a scrim.

Typical uses:
- Dropdown and Menu;
- Popover and Toggletip;
- Date picker calendar;
- Autocomplete and Select panel;
- Coachmark;
- Toast;
- floating controls such as the Support FAB.

The approved Light recipe follows the Primer-style floating separation model:

```css
0 0 0 1px #d1d9e040,
0 6px 12px -3px #25292e0a,
0 6px 18px 0 #25292e1f
```

`Shadow/Floating` is a **composite floating-surface recipe**:

1. the first `0 0 0 1px` layer provides a subtle outline-like boundary so white raised surfaces remain legible on white backgrounds;
2. the second and third layers provide elevation.

The first layer is part of the shared Floating effect, not an explicit component border. Components using `Shadow/Floating` therefore do not add a separate 1px border by default.

Dark keeps the same three-layer geometry and resolves to appearance-aware boundary/shadow colors.

Figma implements Light/Dark resolution inside one Effect Style by binding the three effect colors to hidden implementation variables in the Semantic Appearance collection.

The internal `shadow/floating/border` color chain is active implementation data for the first Floating layer and remains hidden from publishing as a standalone public token.

## Shadow / Dragged

Use Dragged only while an element is actively being dragged or reordered. It deliberately creates a stronger temporary lift than Floating.

Typical uses:
- dragged card;
- dragged Kanban item;
- reorderable list or table row;
- dragged chip or other movable item.

Approved Light recipe:

```css
0 12px 16px 0 rgba(0,0,0,.08),
0 6px 8px 0 rgba(0,0,0,.04),
0 0 6px 0 rgba(0,0,0,.16)
```

Dark keeps the same geometry and increases the corresponding layer opacities to approximately 24%, 12%, and 48%.

Dragged is an interaction state, not a general `Floating / Strong` level.

## No-shadow defaults

The following do not use elevation shadow by default:
- Card;
- Tile;
- Panel;
- Input;
- Button;
- Table;
- Inline Notification.

Use surface color, border, and spacing for their ordinary separation.

Modal/Dialog and modal Drawer surfaces also use no elevation shadow by default when a scrim/backdrop already establishes the layer relationship.

## Component-owned exceptions

Some shadows solve component-specific representation or direction rather than global elevation and should remain component-owned.

### Non-modal Drawer

A non-modal Drawer that overlays content may use a directional edge shadow because separation is required only along the content boundary.

A Drawer that pushes or resizes content should prefer a divider. A modal Drawer with a scrim does not receive a Foundation elevation shadow by default.

### Document or PDF page

A represented document page may use a subtle page shadow to distinguish paper from the viewer canvas. This is representational, not Floating elevation.

### Scroll boundary

Sticky headers, footers, and frozen table columns use border/divider first. Add a directional overflow cue only when the scrolling boundary is otherwise unclear.

## Tailwind boundary

Do not expose Tailwind's generic `shadow-sm/md/lg/xl` scale as the canonical Design System elevation model.

Product tooling may map the two approved recipes to semantic utilities such as:

```text
shadow-floating
shadow-dragged
```

Exact generated artifact and utility implementation remain Frontend-owned.

## Figma migration

The previous `Shadows/Menu` Effect Style was migrated in place to `Shadow/Floating` so existing consumers retain the same Style ID and automatically receive the canonical three-layer recipe. `Shadow/Dragged` is a separate public Effect Style.

The floating boundary color remains an internal implementation variable consumed by `Shadow/Floating`; consumers should use the Effect Style / semantic shadow utility rather than binding that color variable directly.
