---
id: design-system.component.menu
collection: design-system
type: component
title: Menu
summary: Menu is a temporary action/command surface composed from Menu Items, optional grouping, separators, shortcuts, checked state, destructive tone, and submenus.
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: 2026-09-23
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=17332-167748
source_node: 17332:167748
related:
  - design-system.component.menu-button
  - design-system.component.combo-button
  - design-system.accessibility.core
  - design-system.accessibility.component-authoring-contract
---

# Menu

## Purpose

Menu is the canonical temporary **action/command surface**.

Use it for contextual commands that appear on demand from a Menu Button, overflow trigger, Combo Button menu trigger, context action, or another approved disclosure pattern.

Menu is intentionally separate from its trigger. The trigger owns disclosure and anchoring; Menu owns the floating surface, item composition, grouping, menu-specific states, and composite keyboard behavior.

## Component boundary

### Menu vs Select

Use **Select** when choosing an option sets the current value of a field or form control.

Use **Menu** when activating an item executes a command, toggles a command state, opens a submenu, or performs contextual navigation within an application-menu interaction model.

Checkable Menu Items are command state, not a replacement for normal form selection.

### Menu vs Dropdown

`Dropdown` is not the canonical semantic name for this action surface. Classify existing Dropdown patterns by behavior:

- value selection → migrate toward Select/listbox behavior;
- contextual actions → migrate toward Menu;
- generic floating content → use the appropriate Popover/contextual-surface pattern.

Do not create a second action-menu implementation under a Dropdown name.

### Menu vs Overflow Menu

Overflow is a **trigger pattern**, not another menu surface.

New overflow actions should use an approved compact trigger, normally Icon Button/Menu Button behavior, and open the same canonical Menu.

The legacy published Overflow Menu component is retained in Figma only for migration compatibility.

### Menu vs Menu Button / Combo Button

Menu Button and Combo Button own the trigger and open/closed state.

Menu owns action-item anatomy, interaction states, grouping, separators, checked state, shortcut presentation, submenu indicators, destructive tone, and menu composite keyboard semantics.

Do not duplicate Menu Item behavior inside trigger components.

### Menu vs navigation

The v1 canonical Menu is action/command-oriented. Do not use it as the default pattern for persistent site/product navigation, large information architecture, or side navigation.

## Canonical Figma source

### Menu

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Menu / Default`
- Node ID: `17332:167748`
- Component key: `5b8278235b0cefb99927a2507739afb15ace8f3b`
- Matrix: `4 Size × 2 Layout = 8 variants`
- Native content property: `Content` SLOT

| Property | Type | Values / behavior |
|---|---|---|
| `Size` | Variant | `Extra Small / Small / Medium / Large`; default `Medium` |
| `Layout` | Variant | `Simple / Complex`; default `Simple` |
| `Content` | Native Slot | Compose Menu Item, Menu Group Label, Menu Divider, and approved Menu content |

### Menu Item

- Component set: `Menu Item / Default`
- Node ID: `17332:167436`
- Component key: `77d84f9c0d0377652a87f13ef915c65412655073`
- Matrix: `4 Size × 5 State × 2 Tone = 40 variants`
- Active anatomy is flat: `Trailing + Label + Leading` are direct children of Menu Item. There is no active nested Menu Item Content component.

| Property | Type | Values / behavior |
|---|---|---|
| `Size` | Variant | `Extra Small / Small / Medium / Large` |
| `State` | Variant | `Default / Hover / Active / Focus / Disabled` |
| `Tone` | Variant | `Default / Danger`; Disabled remains a State and visually overrides Tone |
| `Label` | Text | Single-line item label |
| `Leading` | Boolean | 16px logical Start slot; Menu `Layout` controls this automatically in default composition |
| `Checked` | Boolean | Shows the checked indicator |
| `Show start icon` | Boolean | Shows an optional leading/action icon |
| `Start icon` | Instance swap | Shared icon-library source; consumer must explicitly override icon color |
| `Show shortcut` | Boolean | Shows shortcut metadata |
| `Shortcut` | Text | Shortcut text |
| `Submenu` | Boolean | Marks a Root Menu Item as a submenu trigger and shows the logical-End indicator; child submenus do not expose another submenu trigger in JV v1 |

### Composition helpers

| Component | Node ID | Component key | Role |
|---|---|---|---|
| `Menu Group Label / Default` | `23038:129820` | `ae3dbe7236e339083cccd60ad047306201c0f6c6` | Optional non-interactive group heading |
| `Menu Divider / Default` | `23038:129822` | `8cb217e111f87fa16785890815d769083ac7e5ec` | Optional non-interactive group separator |

Grouping is Menu composition. Divider/group properties do not belong on every Menu Item.

## Anatomy

Logical item anatomy is implemented directly in Menu Item:

1. **Start / Leading** — optional checked indicator or optional start/action icon.
2. **Label** — one clear primary label.
3. **End / Trailing** — optional shortcut metadata or submenu indicator.

Do not introduce a nested content component for this anatomy.

Authoring constraints:

- `Layout=Simple` is for menus where no item uses a leading icon/check indicator; the leading column collapses completely.
- `Layout=Complex` reserves a 16px logical Start column across every item. Use it when any item in the menu uses a Start icon, checked/selection indicator, or another approved leading visual. Default Figma authoring content shows the shared Start icon; individual items may hide or swap it.
- In a Complex Menu, an item with no visible leading visual keeps the 16px slot empty so labels remain aligned with neighboring items.
- Checked indicator and ordinary Start icon are normally mutually exclusive.
- Shortcut metadata and Submenu indicator are normally mutually exclusive.
- Do not use trailing metadata to repeat a submenu's selected value.
- Group labels and dividers are non-interactive.

## Size and density

Menu Size aligns 1:1 with the trigger/control baseline. The canonical default is `Medium` (40px) for both Menu and Menu Item.

| Size | Menu Item height |
|---|---:|
| Extra Small | 28px |
| Small | 32px |
| Medium | 40px |
| Large | 48px |

Shared item geometry:

- Complex leading column: fixed `16px`; Simple leading column: collapsed;
- Leading and Trailing containers are transparent and must not add their own background fill;
- icon-library components intentionally keep a fixed base color; Menu Item consumers must explicitly override icon color rather than inherit the library default;
- horizontal padding: `12px`;
- Menu owns the `160–320px` width constraint; Menu Item has no independent min/max width and fills the available Menu content slot;
- item radius: Medium radius `6px`;
- label: `Body/Compact/SM` = 14/20 Regular;
- item icons: `16px`.

Menu shell geometry:

- default width: `200px`;
- minimum width: `160px`;
- maximum width: `320px`;
- shell padding: `4px`;
- shell radius: Large radius `12px`;
- shell fill: `surface/raised`;
- elevation: `Shadow/Floating`.

The 320px maximum is the JV v1 authoring ceiling so Persian labels and trailing metadata have more usable space than the legacy menu.

## Width, wrapping, and long labels

Menu Items are single-line.

- Do not wrap the primary label.
- Long labels use ending ellipsis.
- Increase Menu width only within `160–320px` before relying on truncation.
- Shortcut/submenu metadata keeps its own End space and must not overlap the label.
- Essential meaning must not exist only in the truncated suffix; rewrite the label or provide equivalent accessible context.
- Menu may be wider than its trigger, but must never resize the trigger.

## Supported item types

### Standard action

Default treatment for ordinary commands.

### Danger action

Use `Tone=Danger` for destructive or difficult-to-reverse commands.

Danger is a **content tone**, not an interaction state. Hover and Active continue to use the shared neutral interaction overlays. Prefer destructive items at the end of a group/list where practical.

### Disabled action

Use `State=Disabled`. Disabled visually wins over Default/Danger tone and cannot activate.

### Checked action

Use `Checked=True` for persistent command/toggle state inside a Menu. A menu containing checked/selectable items uses `Layout=Complex` so selected and unselected labels stay aligned.

The check indicator is the persistent state cue. v1 does not add a separate selected-background state axis. Runtime uses `menuitemcheckbox` or `menuitemradio` semantics only when the interaction truly represents checkable/radio command state.

### Submenu trigger

Use `Submenu=True` on an item in the **Root Menu**. The item becomes a parent trigger rather than a terminal command.

JV v1 supports **one child submenu level only**:

```text
Root Menu
└── Child Submenu
```

Do not place another submenu trigger inside the child submenu. Two visible Menu surfaces is the maximum authored depth in v1.

This is a deliberate product/design constraint rather than a WAI-ARIA platform limitation. APG, Primer, and Radix can represent deeper nesting, while Carbon explicitly advises avoiding multiple levels because navigation becomes harder. JV keeps one child level to reduce pointer, keyboard, and scanning complexity.

If a command hierarchy needs another level, prefer one of these restructures instead:

- flatten related commands with a group label or divider;
- move the deeper choice into the resulting flow, dialog, or page;
- reconsider whether the interaction is actually a Menu rather than a selection/navigation surface.

#### Child surface composition

The child surface is another instance of the same canonical `Menu / Default`; do not create a separate Submenu component.

- child `Size` matches its parent Menu Size;
- child `Layout` may be Simple or Complex according to its own items;
- child width remains independently authorable within the same `160–320px` Menu limits;
- keep a **2px** surface-to-surface gap;
- when space allows, align the first child item with the parent trigger row;
- open toward logical End: left in RTL, right in LTR;
- collision handling may flip the child to the opposite side at runtime.

The submenu indicator occupies logical End. In the RTL-authored JV source it points left, toward the preferred opening direction. Shortcut metadata and the submenu indicator remain mutually exclusive.

#### Pointer and focus behavior

Hovering or focusing a parent item may reveal its submenu, but exact hover-intent delay, safe-polygon behavior, pointer corridor, portal strategy, and collision engine are runtime-owned and remain unverified.

Opening a child submenu must not resize either Menu surface.

## Grouping and separators

Use `Menu Group Label / Default` when a visible group name improves comprehension. Use `Menu Divider / Default` between meaningful groups, not between every item.

Runtime grouping must preserve semantic grouping. Visible group labels provide the group accessible name; separators are non-focusable and non-interactive.

## Visual states and tokens

### Container

| Role | Token / style |
|---|---|
| Background | `surface/raised` |
| Elevation | `Shadow/Floating` |
| Radius | Large `12px` |

### Standard Menu Item

| State / element | Treatment |
|---|---|
| Default background | Transparent |
| Hover background | `surface/transparent-hover` |
| Active background | `surface/transparent-active` |
| Label / actionable icon | `fg/primary` — explicit override on icon instances |
| Secondary shortcut metadata | `fg/secondary` |
| Disabled content | `fg/disabled` |
| Focus | shared `Focus/Default` non-layout-affecting ring |
| Divider | `line/muted` |

### Danger Menu Item

| State / element | Treatment |
|---|---|
| Default content | `fg/danger` — explicit override on icon instances |
| Hover background | `surface/transparent-hover` |
| Active background | `surface/transparent-active` |
| Hover / Active content | remains `fg/danger` |

Do not use a solid danger-filled row for normal Menu Hover/Active feedback.

## Focus

Focus uses the shared `Focus/Default` effect and must not change item dimensions. Do not use a layout-affecting border.

Runtime should show the focus treatment for keyboard navigation under the shared `:focus-visible` contract.

## Interaction

- Opening a trigger reveals Menu without changing trigger dimensions.
- Activating an enabled terminal command normally executes it and closes the Menu.
- `Escape` closes and returns focus to the invoking trigger/context.
- Clicking outside closes the Menu.
- `Tab` / `Shift+Tab` close the Menu and move focus out rather than walking through Menu Items.
- A submenu trigger opens its child Menu rather than executing a terminal command.
- Opening a child submenu does not close or resize the Root Menu; both surfaces remain visible until the child or full menu stack is dismissed.
- Closing the child submenu returns interaction context to its parent item while keeping the Root Menu open.

A checkable command may remain open while toggling several related options when the product flow requires it. That choice is runtime/product-owned and must not be inferred from Figma.

## Keyboard and accessibility contract

JV Menu follows the WAI-ARIA application-menu interaction model.

### Roles

- container: `role="menu"`;
- ordinary item: `role="menuitem"`;
- checkable item: `role="menuitemcheckbox"` or `role="menuitemradio"`;
- checked state: `aria-checked`;
- disabled item: `aria-disabled="true"`;
- submenu trigger: `role="menuitem"` with `aria-haspopup="menu"` and `aria-expanded` reflecting its child surface; `aria-controls` may be used when the runtime owns a stable relationship;
- divider: separator semantics and not focusable;
- groups: appropriate group semantics and accessible group naming.

### Opening and focus

When opened from a Menu Button, overflow trigger, or Combo Button, move focus into Menu and normally focus the first Menu Item.

### Inside Menu

- `ArrowDown` / `ArrowUp` move among Menu Items.
- `Home` / `End` move to first / last Menu Item.
- Printable-character typeahead moves to the next matching item.
- `Enter` activates a terminal item; on a submenu trigger it opens the child submenu and moves focus into it.
- `Space` activates/toggles according to item role; on a submenu trigger it opens the child submenu rather than executing a terminal command.
- The directional arrow toward logical End opens a submenu and places focus on its first item. The opposite directional arrow closes the child and returns focus to the parent item. Runtime mirrors these physical keys under RTL/LTR.
- `Escape` closes only the current child submenu first and returns focus to its parent item; a subsequent `Escape` from the Root Menu closes the root and returns focus to the original invoker.
- `Tab` / `Shift+Tab` close the Menu and move focus out.
- Disabled Menu Items remain discoverable in arrow-key navigation but cannot activate, following WAI-ARIA APG Menu convention.
- Group labels and separators are skipped because they are not Menu Items.

Submenu directional keyboard behavior follows the standard Menu pattern and active document direction. In LTR, Right normally opens and Left closes; in RTL this mirrors. Runtime must derive this from document direction rather than hard-code physical keys.

The exact focus implementation—roving `tabindex` versus `aria-activedescendant`—is runtime-owned. The resulting behavior above is the contract.

## RTL

Figma is authored for RTL.

- Start = right;
- End = left;
- checked/start icon = logical Start;
- shortcut/submenu indicator = logical End;
- label is right-aligned;
- submenu chevron points toward the preferred submenu opening direction;
- child submenu opens toward logical End (left in RTL) and may flip on collision.

Runtime uses logical positioning/document direction. In LTR, Start/End and submenu direction mirror naturally.

## Placement and collision boundary

Menu owns visual surface, content, width limits, and menu semantics.

The trigger/overlay runtime owns anchor reference, preferred placement, collision detection, flip/shift behavior, viewport padding, portal/layer strategy, and dismissal wiring.

When attached to Menu Button, Combo Button, or an approved overflow trigger, preserve the shared **2px** trigger-to-surface gap. The open surface must stay outside the trigger's normal layout flow so opening it never changes trigger dimensions. Do not create placement variants in Menu.

## Benchmarks used

The v1 contract was reviewed against WAI-ARIA APG Menu/Menu Button, Primer ActionMenu/ActionList, Carbon Menu, and Radix Dropdown Menu.

Primer treats leading visuals as optional and recommends them only when they improve scanability. Carbon similarly distinguishes ordinary options from selectable options and reserves leading space where selection alignment requires it. JV captures that authoring distinction at the Menu level with `Layout=Simple / Complex`.

For submenus, APG defines nested menu keyboard and accessibility semantics, Primer and Radix demonstrate multi-level submenu composition, and Carbon cautions against multiple nesting levels. JV therefore supports the standard submenu semantics but intentionally caps authored depth at one child submenu level.

JV deliberately differs from Carbon Extra Small sizing: JV uses the shared 28px control baseline rather than Carbon's 24px menu option.

References:

- https://www.w3.org/WAI/ARIA/apg/patterns/menubar/
- https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/
- https://primer.style/product/components/action-menu/
- https://primer.style/product/components/action-list/
- https://carbondesignsystem.com/components/menu/style/
- https://www.radix-ui.com/primitives/docs/components/dropdown-menu

## Runtime boundary

Runtime component source, package/API, Storybook identity, and Code Connect mapping are currently unregistered.

Therefore this document does **not** assert exact Angular component/tag name, prop/event names, DOM nesting, focus-management technique, portal library, collision engine, submenu timing, animation timing, or Storybook story ID.

Implementation must satisfy this design/accessibility contract, but exact runtime API details remain unverified until an owning source is registered.

## Legacy / migration

Figma retains three published legacy assets only so old instances remain resolvable:

- `Legacy / Menu Item Content` — key `3c4735684b5eb1146dab273119bcc59dbceee8aa`; deprecated after flattening Menu Item;
- `Legacy / Keyboard shortcut` — key `e2113c87df4d0d02d41477f4c706fb6b30a6437a`;
- `Legacy / Overflow menu` — key `89d20a2413e0b877ce2d9c358ce75bb903155bfb`. Its retained Figma open variants place Menu as an absolute overlay with `clip content = false` and a 2px trigger gap, so Open does not change the trigger/component bounds.

Do not use them in new designs.

The old Menu `Function=Simple/Complex` semantics are retired. The current `Layout=Simple/Complex` axis is intentionally narrower: it controls only whether the 16px leading column is collapsed or reserved. Legacy item Divider/Spacer/Indented booleans, 24px Extra Small size, and Danger-as-state are also retired.

## QA checklist

Verify:

- Menu has exactly `4 Size × 2 Layout = 8` variants and one native `Content` Slot, with `Medium + Simple` as the default variant;
- Menu Item has exactly `4 Size × 5 State × 2 Tone = 40` variants, with `Medium + Default + Default Tone` as the default variant;
- Menu Item anatomy is flat (`Trailing + Label + Leading`) with no active nested Menu Item Content component;
- heights are `28 / 32 / 40 / 48`;
- Menu width is within `160–320px`; Menu Item has no independent min/max width and fills the inner content width (for a 160px Menu with 4px shell padding, items fill 152px);
- shell uses `surface/raised + Shadow/Floating + 12px radius`;
- item radius is 6px and horizontal padding 12px;
- long labels are single-line with ending ellipsis;
- Hover / Active / Focus / Disabled use semantic treatments;
- Danger is Tone, not State;
- Simple collapses the leading column completely; Complex reserves exactly 16px across items and default Figma content shows a Start icon;
- any menu containing a Start icon or checked/selection indicator uses Complex layout, including blank reserved slots on neighboring items;
- Leading and Trailing containers remain transparent in every Tone;
- every Menu Item icon has an explicit semantic color override: Default → `fg/primary`, Danger → `fg/danger`, Disabled → `fg/disabled`; after any icon swap, verify the override is still present;
- Checked / Start icon and Shortcut / Submenu authoring constraints are respected;
- Submenu depth is Root Menu + one child submenu only; child submenu items do not expose another submenu trigger;
- child submenu reuses canonical Menu, matches parent Size, keeps an independent `160–320px` width, uses a 2px surface gap, opens toward logical End, and may flip on collision;
- submenu keyboard behavior opens toward logical End, closes toward the parent, and `Escape` unwinds one menu level at a time;
- groups/dividers are composed at Menu level;
- RTL Start/End anatomy and submenu direction are correct;
- real instances can replace Menu Slot content without detaching;
- Menu Button and Combo Button sizes map 1:1 to Menu size, including Extra Small;
- Menu Button, Combo Button, and retained legacy Overflow open states keep Menu outside normal layout flow with a 2px gap and do not grow the trigger/control bounds;
- disabled items cannot activate;
- keyboard behavior follows the Menu composite contract;
- runtime API facts remain unverified where no owning source exists.

## Related documents

- `menu-button.md`
- `combo-button.md`
- `select.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../accessibility/core.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../../accessibility/focus-management.md`
- `../../integrations/component-mapping.md`
