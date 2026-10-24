---
id: design-system.component.radio
collection: design-system
type: component
title: Radio
summary: Radio lets users choose exactly one mutually exclusive option from a group.
knowledge_state: canonical
document_maturity: reviewed
last_reviewed: '2026-10-24'
related:
  - design-system.component.checkbox
  - design-system.reference.component-mapping
  - design-system.accessibility.keyboard-navigation
---

# Radio

## Purpose

Radio lets users choose one option from a mutually exclusive set.

A Radio item is not a standalone boolean control. It belongs to a Radio Group that owns the shared decision and ensures only one option is selected at a time.

## When to Use

Use Radio when:

- users must choose exactly one option from a small, visible set;
- comparing the available options side by side is useful;
- all choices should remain visible without opening a Select or Menu.

## When Not to Use

Do not use Radio when:

- users can choose multiple independent options; use Checkbox;
- a single setting turns on or off immediately; use Toggle;
- there are many options and persistent visibility is not useful; use Select/Combobox as appropriate;
- the option itself needs a larger descriptive surface or richer content; use the approved Radio Card pattern instead of enlarging the base Radio.

## Boundary: Radio vs Checkbox vs Radio Card

- **Radio**: one mutually exclusive choice in a group.
- **Checkbox**: zero, one, or many independent choices; may also represent one optional boolean choice.
- **Radio Card**: the same single-selection semantics as Radio, but the option requires a larger card surface, richer supporting content, or a stronger selected container treatment.

Do not use visual styling alone to change the underlying selection semantics.

## Anatomy

A Radio item contains:

1. a 20px Radio icon instance;
2. an item label;
3. 8px spacing between label and control.

The source icon components remain unchanged at their library size; the nested instance is resized proportionally to 20×20 inside Radio.

The canonical control must use the exact local JobVision icon-library components:
- `Icon/radio_button_unchecked` — node `15087:365350`, key `c8005abc2598ad492de5ac17df5cfb9dc1a4509b`;
- `Icon/radio_button_checked` — node `15087:365346`, key `5acf2d061791622a49c9826cd671f165d6648f73`.

Use those components directly as nested instances. Do not redraw, clone, or substitute another published/stale Radio icon source. Semantic color is overridden on the nested icon instance.

The whole visible item row is one interaction target. The label is not a separate interaction.

The default Figma authoring width is 240px so multiline behavior can be tested. The label fills the available row width and grows vertically. The icon and label block are top-aligned so the 20px control aligns with the first 20px text line when the label wraps.

## Figma Property Model

### Radio

| Property | Values | Notes |
|---|---|---|
| `Selected` | `False`, `True` | Selection state |
| `State` | `Default`, `Focus`, `Disabled` | Interaction state |
| `Label` | text | Visible item label |
| `Show label` | Boolean | Hide only when another accessible name is provided |

Variant count: **6 = 2 Selected × 3 State**.

There are deliberately no `Position`, `Skeleton`, `Hover`, or `Active` axes in the canonical component.

### Radio Group

| Property | Values | Notes |
|---|---|---|
| `Direction` | `Vertical`, `Horizontal` | Vertical is the default layout |
| `Group label` | text | Shared question/decision label |
| `Show group label` | Boolean | Hide only when group labeling exists elsewhere |

Validation is not represented as a Radio or Radio Group interaction-state variant. Error/helper/requirement presentation belongs to the surrounding form-field composition.

## Visual Contract

### Default, unselected

- icon: exact local `Icon/radio_button_unchecked`;
- icon instance: 20px;
- icon color: `fg/secondary`;
- label: `fg/primary`.

### Default, selected

- icon: exact local `Icon/radio_button_checked`;
- icon instance: 20px;
- icon color: `fg/accent`;
- label remains `fg/primary`.

Selection is an Accent semantic state, not a Brand state.

### Focus

Focus is independent from selection.

Use the shared focus treatment:

- visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) contract around the Radio control;
- Focus does not change layout or the selection geometry.

Both selected and unselected Radio options retain their selection geometry while focused.

### Disabled

- preserve the checked or unchecked icon geometry;
- icon vector uses `fg/disabled`;
- label uses `fg/disabled`;
- selection geometry remains visible;
- no Hover/Active treatment is introduced.

## Size and Spacing

Current canonical values:

- Radio icon instance: **20px**;
- label gap: **8px** using the shared Spacing 8px variable;
- item label: Vazirmatn **14/20 Regular**, using the shared component label text style;
- group label: Vazirmatn **14/20 Medium** using `fg/secondary`, aligned with Checkbox Group;
- Vertical group item gap: **8px**;
- Horizontal group item gap: **16px**;
- Horizontal Radio items: **Hug contents**; the group width hugs the combined items.
- group-label-to-items gap: **8px**.

No size variant is defined. Add one only after a repeated product need is validated.

## Label Behavior

- The label may wrap to multiple lines.
- The Radio icon and label block are top-aligned so multiline labels align the control with the first text line.
- Do not truncate required option meaning only to preserve a one-line row.
- The entire item row, including the label, activates the Radio.
- Hiding the visible label requires another accessible name.

## Radio Group Behavior

- A Radio item belongs to a Radio Group.
- A group contains at least two mutually exclusive options.
- Selecting one option deselects the previously selected option.
- Vertical is the default direction.
- Horizontal layout is valid for concise options when available width and readability are sufficient.
- In a Horizontal Radio Group, each Radio item hugs its own content; do not force equal or fixed item widths unless a product layout explicitly requires it.
- Group label belongs to the group, not the first Radio item.
- A group may contain a variable number of options; the Figma examples are not a product maximum.

## Keyboard and Accessibility

Prefer native radio inputs where implementation allows.

The group follows established native/APG radio behavior:

- `Tab` / `Shift+Tab` enters or leaves the Radio Group as a composite interaction stop;
- Arrow keys move among options according to native/platform Radio Group behavior and update selection;
- `Space` selects the focused Radio when applicable;
- disabled options are not activatable;
- keyboard focus remains visibly distinct from the selected state.

Visible item text must be programmatically associated with the Radio control.

A labeled group should use native grouping semantics such as `fieldset` / `legend` where appropriate, or an equivalent accessible group label.

Do not rebuild native radio semantics with generic `div` elements and ad-hoc key handlers without a justified implementation requirement.

## RTL

RTL/LTR is a layout direction, not a Radio variant axis.

- The control sits at logical inline-start.
- The label sits at logical inline-end.
- In JobVision's RTL authoring examples, this renders as control on the right and label on the left.
- Runtime LTR layouts mirror through logical layout/CSS direction rather than using a `Position=Start|End` component variant.
- Do not blindly reverse Arrow-key behavior; preserve native/platform Radio Group behavior.

## Validation

Validation belongs to the shared field/group composition.

- Do not add `Error` or `Warning` as Radio interaction-state variants.
- Group-level error/helper content describes the shared decision.
- A validation message must not replace the accessible group label.
- Disabled is not a validation state.

## Loading

Loading is not part of the base Radio state matrix.

If a screen needs loading placeholders, render a Skeleton pattern for the option list rather than multiplying Radio selection variants by `Skeleton`.

## Benchmark Review

The final Radio contract was reconciled against current external references:

- **WAI-ARIA APG Radio Group**: confirms group semantics, one sequential Tab stop, Space selection, and Arrow-key navigation within the group.
- **Carbon Radio Button**: uses a 20px visual radio control, 14px Regular option label, and 8px control-to-label spacing.
- **Material Web Radio**: uses a 20px default radio icon size.
- **Primer RadioGroup accessibility**: requires a clear persistent option label, visible focus, and at least a 24×24 CSS-pixel operable target/spacing contract.

JV therefore keeps the **visual Radio instance at 20px** while treating the full labeled option as the interaction target. Runtime implementation must preserve a minimum 24×24 operable target or equivalent compliant spacing without enlarging the visible mark.

Primer currently documents vertical RadioGroup orientation only; JV's Horizontal direction remains an intentional product-system extension for short, concise option sets and is not inferred from Primer.

External systems are references, not owning runtime sources for JV.

## Product Variations

Radio is a shared JobVision/Cando component.

Product and Appearance differences resolve through the Theme/Semantic token architecture. Do not create product-specific Radio variants.

## Figma Reference

File: `-DS- Job Vision`

File key: `rROD8ctH9UfPGAMrRrOzHe`

### Radio

- Component Set: `Radio / Default`
- Node: `2930:23442`
- Component key: `a1e6b8ca998c57f78abd75b97b190aacbd662f44`
- Variant properties: `Selected / State`
- Content properties: `Label / Show label`

### Radio Group

- Component Set: `Radio Group / Default`
- Node: `2927:28166`
- Component key: `8a24b1caa72671235a5c9d26706efcc845f45eee`
- Variant properties: `Direction`
- Content properties: `Group label / Show group label`

Canonical Presentation: [Radio Button / Documentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=23835-186). Both original Component Sets above are embedded in Section 01 with their existing node IDs, while the Playground uses source-linked instances. The previous documentation layout is archived on the same Figma page.

## Runtime / Storybook Reference

Code repository/package: **Unregistered**

Runtime component/API: **Unverified**

Storybook: **Unregistered**

Figma property → runtime prop mapping: **Unverified**

Do not infer exact DOM structure, event names, prop names, or implementation API from Figma. Register the owning runtime Design System source before mapping these details.

## Migration Notes

The legacy Figma model was reconciled in place to preserve component identity.

The canonical visual control uses the exact local JobVision icon-library components `Icon/radio_button_unchecked` and `Icon/radio_button_checked` from the Icons page. These are nested directly; no cloned internal Radio asset is maintained.

Removed legacy axes/states:

- `Position=Start|End`;
- `Skeleton`;
- Radio Group `Error`;
- Radio Group `Warning`.

The canonical model is intentionally smaller and separates interaction state, selection state, layout direction, validation, and loading concerns.
