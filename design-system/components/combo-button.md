---
id: design-system.component.combo-button
collection: design-system
type: component
title: Combo Button
summary: Combo Button keeps one dominant action directly available and exposes closely related alternative actions from a separate menu trigger.
knowledge_state: verified
document_maturity: draft
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: 2026-10-17
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22932-134187
source_node: 22932:134187
related:
  - button
  - design-system.component.icon-button
  - design-system.component.menu-button
  - design-system.accessibility.core
---

# Combo Button

## Purpose

Combo Button combines:

1. one directly executable **Primary Action**;
2. one separate **Menu Trigger** exposing closely related alternatives.

Use it when one action is sufficiently dominant/common that hiding it inside a menu would add unnecessary friction, but related alternatives still need compact access.

The dominant action must **not** be repeated inside the menu.

Use Menu Button instead when the available actions are peers and none should remain directly executable while closed.

## Component boundary

Combo Button owns:

- composition of the two connected interactive segments;
- shared outer geometry;
- disclosure/open state of the Menu Trigger;
- replaceable Menu content Slot;
- trigger-to-menu anchoring.

The nested Button owns Primary Action behavior/state/loading.

The nested Icon Button owns Menu Trigger interaction styling, accessible-name requirement, and Focus treatment.

The nested Menu owns menu-item behavior and keyboard navigation.

Combo Button is not a generic Button Group. The two controls have fixed roles: one primary action and one menu disclosure.

## Canonical Figma source

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Combo Button / Default`
- Node ID: `22932:134187`
- Component key: `c6f34b8a4294241844d10349881d8264b1c072eb`
- Matrix: `3 Style × 4 Size × 2 Open = 24 variants`
- Primary Action foundation: canonical `Button / Default`
- Menu Trigger foundation: canonical `Icon Button / Default`
- Menu composition: native `Menu content` SLOT

### Figma presentation — verified 2026-10-17

[Combo Button / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=22935-2651) follows the [Figma Component Presentation Guideline](../../integrations/figma-component-presentation.md): one 1600px documentation frame with **the original 24-variant public Component Set** (same node ID/key) in **01 · Component set**. The source's canvas-only layout is now compact: three Style columns and paired Closed/Open rows for each Size, without creating variants or changing their APIs. **02 · Playground** has 13 genuine source-linked Combo Button instances covering dominant action, three styles, Persian/RTL related alternatives, four sizes, Action/Trigger Focus, Action Loading and whole-control Disabled. **03 · Anatomy & composition** documents the shared Wrapper, semantic Divider, canonical Button/Icon Button instances and native Menu Slot; the shared Button masters remain on their own pages. **04 · Usage & handoff** records usage and runtime caveats. The obsolete oversized scaffold and an unrelated loose QA instance were removed; the original documentation frame ID remains unchanged. This is Figma source/presentation verification, not executable runtime QA.

### Figma properties

| Property | Type | Values / behavior |
|---|---|---|
| `Style` | Variant | `Primary / Secondary / Tertiary` |
| `Size` | Variant | `Extra Small / Small / Medium / Large` |
| `Open` | Variant | `False / True` |
| `Menu content` | Native Slot | Replaceable shared Menu content |
| `Primary Action / Button` | Exposed nested instance | Button content/state/loading authoring |
| `Menu Trigger / Icon Button` | Internal nested instance | Fixed Menu Trigger; not exposed for direct authoring |

Default Figma state is `Primary / Medium / Open=False`.

Interaction states are intentionally not multiplied into the outer variant matrix; the two segments are separate interactive targets and own their own states.

## Anatomy

RTL-authored Figma source:

```text
Combo Button / Default (Style × Size × Open)
├─ Unified shell / Wrapper (horizontal Auto Layout, 0px gap, radius 6)
│  ├─ Menu Trigger / Icon Button (canonical instance; logical End)
│  ├─ Divider / semantic {Style} (non-interactive 1px Rectangle)
│  └─ Primary Action / Button (exposed canonical instance; logical Start)
└─ Menu content (native Slot, absolute/out of layout)
```

The **Wrapper** owns the unified shape and Tertiary outer border. The two nested Button instances retain their canonical source links and independent activation, Focus, Disabled and Primary Action Loading. The Divider is an **internal Rectangle**, not a new public component or an interactive target.

### Shared geometry

- Control heights stay `28 / 32 / 40 / 48px` (Extra Small / Small / Medium / Large).
- Wrapper is horizontal Auto Layout, **0px item gap**, radius `6px`, with 6px outer Button corners and **0px touching corners**.
- Divider has **1px visible width**, but is **absolute-positioned inside the Wrapper**: it consumes **0px of Auto Layout width**. Its left edge sits at `Menu Trigger width − 1px`, overlaying the Trigger's last pixel, so the two canonical Button surfaces touch with no exposed background at the top or bottom of the Divider.
- Divider height = control height minus `16px`, i.e. `12 / 16 / 24 / 32px`, centered vertically (`y=8px`).
- The Wrapper is **Hug width**, with total width equal to `Menu Trigger width + Primary Action width`; the Divider contributes **0px**. Default widths are `98 / 118 / 134 / 150px` by Size.
- Menu Slot stays a direct child of the public Combo variant, out of the Wrapper's Auto Layout, anchored **2px** below the control. Open never changes control width or height.

### Divider and border tokens

| Style | Divider fill token | Outer Wrapper border |
|---|---|---|
| Primary | `line/inverse` | None |
| Secondary | `line/emphasis` | None |
| Tertiary | `line/default` | 1px `line/default` |

All Divider fills are bound to semantic variables; the old primitive `palette/bw/white` join stroke is gone. Both nested Button instances have their joining strokes removed, preventing a double boundary. The **Tertiary Wrapper stroke is outside-aligned in Figma** so its Auto Layout does not inset children or change control-frame height; the visible border extends beyond that layout box.

Do not set Divider width to `0px` (that makes it invisible), add a second instance-owned seam, reserve an extra 1px gap for the Divider, or clip the nested Button focus rings. Keep Divider's **rendered width 1px** and its **layout participation zero**.

### Validated Figma migration — 2026-10-17

An isolated Wrapper + Divider prototype passed **24/24** `Style × Size × Open` cases plus independent Action Focus, Trigger Focus, Action Loading and whole-control Disabled checks. The original **24 canonical variants** were then migrated without replacing their node IDs, component-set key, nested Button/Icon Button instance IDs, exposed Primary Action, or native Menu Slot property. Post-migration QA passed all 24 variants, all 13 source-linked Playground instances, RTL menu content, 2px anchoring and source-matrix collision checks. The temporary experiment and stray loose instance were removed.

**Seam fix (2026-10-17):** after visual review revealed a background-colored 1px slit above and below the short Divider, all 24 canonical variants were updated in place to use an absolute Divider overlay and Hug-width Wrapper. Post-fix structural QA passed **24/24**, and all **13** live Playground instances retained independent Action/Trigger Focus, Action Loading and Disabled overrides. Primary, Secondary and Tertiary closed states were visually reviewed without the slit. Original component IDs, tokens and Menu Slot properties were preserved.

These are Figma source/visual-state checks, **not** executed Angular, Storybook, keyboard or screen-reader tests.

## Style contract

JV v1 supports:

- **Primary** — default; strongest operational treatment.
- **Secondary** — medium-emphasis split action when Primary would overstate hierarchy.
- **Tertiary** — control-like/utility treatment in dense operational interfaces.

JV v1 deliberately excludes:

- Brand;
- Ghost;
- all Danger styles.

Brand is reserved for approved product-defining/conversion moments and should not be generalized to a split operational control.

Danger split controls create ambiguity about whether only the default action or all alternatives are destructive; use a clearer dedicated destructive action/menu pattern instead.

Ghost provides insufficient structural definition for a connected two-target control in the current visual model.

### Benchmark note

External systems are not uniform about split/combo emphasis:

- Carbon currently restricts Combo Button to Primary.
- Fluent 2 defines Split Button by behavior: a dominant visible action plus additional actions in a menu.
- Material UI demonstrates Split Button as a ButtonGroup composition and its ButtonGroup supports standard button variants.
- Atlassian's SplitButton history has supported more than one appearance.

JV keeps Primary/Secondary/Tertiary because its canonical Button hierarchy needs lower-emphasis operational split actions in dense products such as ATS, while still keeping the set constrained and semantically explicit.

References:
- https://carbondesignsystem.com/components/menu-buttons/usage/
- https://fluent2.microsoft.design/components/web/react/core/button/usage
- https://mui.com/material-ui/react-button-group/
- https://atlassian.design/components/button/split-button

## Sizes

| Size | Height | Menu Trigger | Current default Menu size |
|---|---:|---:|---|
| Extra Small | 28px | 28×28 | Extra Small |
| Small | 32px | 32×32 | Small |
| Medium | 40px | 40×40 | Medium |
| Large | 48px | 48×48 | Large |

Primary Action uses the same Button Size.

Menu now follows the same 28 / 32 / 40 / 48px size baseline as Combo Button. Every Combo Button size composes the matching Menu size, including Extra Small.

## Open and interaction states

### Closed

- Menu Slot hidden.
- Menu Trigger in normal Enabled/interaction state.
- Trigger icon is `chevron_down`.
- Primary Action state is independent.

### Open

- Menu Slot visible.
- Menu Trigger maps visually to Icon Button `Active`.
- Trigger icon is `chevron_up`.
- Primary Action keeps its own state.
- Width and height do not change.

`Open` is a Figma authoring/visual state. Runtime may use controlled or uncontrolled disclosure state; exact API naming remains unverified.

## Independent segment behavior

The two segments are separate focus and activation targets.

### Primary Action

- behaves like a normal Button;
- `Enter` / `Space` execute the dominant action;
- action state/loading does not automatically imply that the Menu is open.

### Menu Trigger

- opens/closes the Menu;
- follows Menu Button semantics;
- receives a meaningful accessible name;
- follows the Icon Button Tooltip contract;
- Open state applies only to this segment.

Do not make the entire combined rectangle one hit target.

## Loading

Combo Button has no outer Loading axis.

Loading belongs to the nested Primary Action because that is the segment executing the dominant operation.

When Primary Action is loading:

- preserve total Combo width and height;
- preserve Button loading behavior/focus as defined by Button;
- suppress repeated activation of the Primary Action;
- Menu Trigger may remain available when its alternatives are still valid.

If the in-progress operation makes all alternatives invalid or unsafe, disable the whole Combo at the flow level.

Do not convert the Menu Trigger to a spinner.

## Disabled

Normal whole-control Disabled behavior disables both segments and closes/prevents the menu.

Partial disable is allowed only when semantics are intentional:

- Primary Action unavailable;
- alternative actions in Menu remain valid;
- Menu Trigger remains operable and clearly understandable.

Do not partially disable merely for visual hierarchy.

## Menu Slot contract

`Menu content` is a native Figma Slot.

Rules:

- use shared Menu/Menu Item components;
- do not repeat the dominant Primary Action in the menu;
- keep alternatives closely related to the dominant action;
- keep Menu outside the Combo's layout flow;
- preserve the 2px anchored-surface gap;
- Menu may be wider than the Combo;
- Menu width must not resize the Combo.

Runtime overlay positioning, collision, and portal behavior remain implementation-owned.

## RTL

Use logical Start/End semantics.

In RTL:

- Primary Action is on the right — logical Start.
- Menu Trigger is on the left — logical End.
- the 1px non-interactive semantic Divider sits between the two Button instances inside their shared Wrapper.
- chevron up/down does not horizontally mirror.
- menu positioning uses logical alignment and viewport collision rules.

In LTR the physical order reverses naturally: Primary Action left, Menu Trigger right.

Do not hard-code left/right semantics into the runtime API.

## Accessibility and keyboard contract

Combo Button contains two Button semantics, not one composite tab stop.

### Primary Action

Follow the Button contract:

- native Button semantics where possible;
- visible label is the accessible name;
- `Enter` and `Space` activate;
- visible Focus;
- Loading/Disabled semantics from Button.

### Menu Trigger

Follow Menu Button + Icon Button contracts:

- native Button semantics where possible;
- meaningful accessible name such as “More [action] options” in the current product language;
- Tooltip label on hover/focus;
- `aria-haspopup="menu"`;
- `aria-expanded="true|false"`;
- optional `aria-controls` linking to Menu;
- `Enter` / `Space` open and move focus into Menu;
- optional ArrowDown/ArrowUp opening behavior may follow WAI-ARIA APG;
- `Escape` in Menu closes and returns focus to the Menu Trigger.

Focus order follows DOM order and language direction requirements without creating an artificial roving-focus composite.

If visible menu-item wording omits shared context from the primary action label, accessible labels/descriptions must still communicate the full action meaning.

External references:
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/
- https://www.w3.org/WAI/ARIA/apg/patterns/button/

## Runtime boundary

Runtime source and Storybook identity are currently unregistered.

Do not infer exact props from Figma labels.

Conceptually runtime must support:

```text
Combo Button
- style: primary | secondary | tertiary
- size
- primary action label/content
- primary action handler
- primary action loading/disabled state
- menu-trigger accessible name
- menu content
- whole-control disabled policy
- open/close state management
```

Exact Angular structure, prop names, class architecture, popup implementation, and Storybook identifiers remain unverified.

The implementation may compose shared Button, Icon Button, Menu, non-interactive Divider and Wrapper primitives internally if it preserves the unified shape, semantic separator, 2px menu gap and independent focus/activation behavior.

## QA checklist

**Figma design-source QA — PASS (2026-10-17)**

- Original component-set node ID/key preserved; exactly `3 Style × 4 Size × 2 Open = 24` variants.
- Every variant has exactly two direct children: **Wrapper** and native **Menu Slot**.
- Every Wrapper has three ordered children: canonical Icon Button, 1px semantic Divider Rectangle, canonical Button.
- Exposed Primary Action, internal Menu Trigger, their canonical instance IDs and native Slot property are preserved.
- Heights `28/32/40/48px`; default widths `98/118/134/150px` respectively. Divider has **0px layout width**.
- 0px layout gap; canonical Button and Icon Button surfaces physically touch (`Action.x = Trigger.width`); Wrapper is Hug-width; 6px shared radius; inner Button corners 0; no doubled Button strokes.
- Divider is a visible 1px Rectangle positioned **ABSOLUTE** at `Trigger.width − 1px` (not a third Auto Layout column), with height = control height − 16px; semantic fill tokens: Primary `line/inverse`, Secondary `line/emphasis`, Tertiary `line/default`.
- Tertiary outer `line/default` border is Wrapper-owned, outside-aligned and does not change control-frame height.
- Open changes only Trigger Active/chevron; Open/Closed widths match.
- Menu Slot remains out of flow, 2px below control; no matrix overlaps.
- All 13 live Playground instances remain connected; Action Focus, Trigger Focus, Action Loading and whole-control Disabled overrides pass.
- RTL open-menu labels and Extra Small shared Menu remain intact; temporary prototype removed.

**Implementation QA — pending:** real browser Focus, keyboard/screen-reader behavior, dynamic label width, token contrast across supported product/theme modes, overlay collision/portal behavior and Loading semantics.

## Known gaps

- The Divider now uses semantic `line/*` tokens, but **actual contrast across product/theme modes remains pending runtime/theming QA**. Translate the Tertiary outside-aligned Figma border carefully into the implementation's box-sizing model.
- runtime component/API, code repository/package, and Storybook are unregistered;
- exact overlay/collision implementation is unverified;
- exact partial-disabled runtime API is intentionally not specified;
- executable keyboard/screen-reader behavior must be verified when the runtime component exists;
- the exposed nested Primary Action Button still technically allows Style/Size overrides that can diverge from the outer Combo axes; the Menu Trigger is internal/not exposed, so this authoring risk is limited to the Primary Action until its content/loading properties can be promoted individually without exposing the whole nested instance.

## Related

- `button.md`
- `icon-button.md`
- `menu-button.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../accessibility/core.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../../accessibility/focus-management.md`
- `../../integrations/component-mapping.md`
