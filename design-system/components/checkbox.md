---
id: design-system.component.checkbox
collection: design-system
type: component
title: Checkbox
summary: Checkbox lets users select zero, one, or many independent options and can represent a single optional boolean choice.
knowledge_state: canonical
document_maturity: reviewed
last_reviewed: '2026-09-19'
related:
  - design-system.component.radio
  - design-system.reference.component-mapping
  - design-system.accessibility.keyboard-navigation
---

# Checkbox

## Purpose

Checkbox lets users select zero, one, or many independent options.

A standalone Checkbox may also represent one optional boolean choice. A Checkbox Group owns a shared multi-select decision and may contain any number of independent Checkbox items.

`Indeterminate` represents a mixed or partial-selection state, usually calculated from child selection. It is not a third persisted end-user choice.

## When to Use

Use Checkbox when:

- users may select multiple independent options;
- one optional choice can be independently on or off;
- a parent option summarizes partial child selection through Indeterminate;
- users may submit or commit several selections together.

## When Not to Use

Do not use Checkbox when:

- users must choose exactly one mutually exclusive option from a visible set; use Radio;
- a setting changes immediately and behaves as an on/off system preference; use Toggle;
- the option itself needs a larger descriptive surface or richer supporting content; use the approved Checkbox Card / selection-card pattern if one exists rather than enlarging the base Checkbox;
- button-like actions need a persistent pressed state; use the appropriate Toggle Button or selection control.

## Boundary: Checkbox vs Radio vs Toggle

- **Checkbox**: zero, one, or many independent selections; may also represent one optional boolean choice.
- **Radio**: exactly one mutually exclusive choice in a group.
- **Toggle**: an immediate on/off setting whose change is applied directly rather than committed as part of a multi-field selection flow.

Do not use visual styling alone to change the underlying interaction semantics.

## Anatomy

A Checkbox item contains:

1. a 20px Checkbox icon instance;
2. an item label;
3. 8px spacing between label and control.

The source icon components remain unchanged at their library size; the nested instance is resized proportionally to 20×20 inside Checkbox.

The canonical control must use the exact local JobVision icon-library components:

- `Icon/check_box_outline_blank` — node `15087:365340`, key `b4b5e8aad25d7be4009568638bc86a3b85a6a185`;
- `Icon/check_box` — node `15087:365337`, key `a9b3101d611597626af94d5f3a63a08058bbceab`;
- `Icon/indeterminate_check_box` — node `15087:365343`, key `ae823e542df2e4ac6c644e4ce8b97fe13aaa5b89`.

Use those components directly as nested instances. Do not redraw, clone, or substitute another published/stale Checkbox icon source. Semantic color is overridden on the nested icon instance.

The whole visible item row is one interaction target. The label is not a separate interaction.

The default Figma authoring width is 240px so multiline behavior can be tested. The label fills the available row width and grows vertically. The icon and label block are top-aligned so the 20px control aligns with the first 20px text line when the label wraps.

## Figma Property Model

### Checkbox

| Property | Values | Notes |
|---|---|---|
| `Selection` | `Unchecked`, `Checked`, `Indeterminate` | Selection state |
| `State` | `Default`, `Focus`, `Disabled` | Interaction state |
| `Label` | text | Visible item label |
| `Show label` | Boolean | Hide only when another accessible name is provided |

Variant count: **9 = 3 Selection × 3 State**.

There are deliberately no `Position`, `Indented`, `Skeleton`, `Hover`, `Active`, `Loading`, or standalone field-label axes in the canonical component.

### Checkbox Group

| Property | Values | Notes |
|---|---|---|
| `Direction` | `Vertical`, `Horizontal` | Vertical is the default layout |
| `Group label` | text | Shared question/decision label |
| `Show group label` | Boolean | Hide only when group labeling exists elsewhere |

Validation is not represented as a Checkbox or Checkbox Group interaction-state variant. Error/helper/requirement presentation belongs to the surrounding form-field composition.

Checkbox Group does not expose a fixed item-count property. The Figma examples contain three items for authoring and QA only; product usage may contain a variable number of Checkbox items.

## Visual Contract

### Default, unchecked

- icon: exact local `Icon/check_box_outline_blank`;
- icon instance: 20px;
- icon color: `fg/secondary`;
- label: `fg/primary`.

### Default, checked

- icon: exact local `Icon/check_box`;
- icon instance: 20px;
- icon color: `fg/accent`;
- label remains `fg/primary`.

### Default, indeterminate

- icon: exact local `Icon/indeterminate_check_box`;
- icon instance: 20px;
- icon color: `fg/accent`;
- label remains `fg/primary`.

Checked and Indeterminate are Accent semantic states, not Brand states.

The base Checkbox does not create a custom filled container behind the icon. The icon artwork itself communicates Unchecked, Checked, and Indeterminate geometry.

### Focus

Focus is independent from selection.

Use the shared focus treatment:

- 2px `focus/default` outer ring;
- 1px visual gap between the icon-instance boundary and focus ring using the normal surface;
- no layout/dimension change.

Unchecked, Checked, and Indeterminate retain their selection geometry while focused.

Focus is the keyboard-visible state represented in Figma. Pointer Hover and Active are not separate Figma variants for the canonical Checkbox.

### Disabled

- preserve Unchecked, Checked, or Indeterminate geometry;
- icon vector uses `fg/disabled`;
- label uses `fg/disabled`;
- selection geometry remains visible;
- no Hover/Active treatment is introduced.

## Size and Spacing

Current canonical values:

- Checkbox icon instance: **20px**;
- label gap: **8px** using the shared Spacing 8px variable;
- item label: Vazirmatn **14/20 Regular**, using the shared component label text style;
- group label: Vazirmatn **14/20 Medium** using `fg/secondary`, aligned with Radio Group;
- Vertical group item gap: **8px**;
- Horizontal group item gap: **16px**;
- Horizontal Checkbox items: **Hug contents**; the group width hugs the combined items;
- group-label-to-items gap: **8px**.

No size variant is defined. Add one only after a repeated product need is validated.

## Label Behavior

- The label may wrap to multiple lines.
- The Checkbox icon and label block are top-aligned so multiline labels align the control with the first text line.
- Do not truncate required option meaning only to preserve a one-line row.
- The entire item row, including the label, activates the Checkbox.
- Hiding the visible label requires another accessible name.

## Checkbox Group Behavior

- A group contains independent Checkbox items under one shared decision label.
- Selecting one item does not change sibling items unless explicit product logic defines a parent-child or select-all relationship.
- Vertical is the default direction.
- Horizontal layout is valid for concise options when available width and readability are sufficient.
- In a Horizontal Checkbox Group, each Checkbox item hugs its own content; do not force equal or fixed item widths unless a product layout explicitly requires it.
- Group label belongs to the group, not the first Checkbox item.
- A group may contain a variable number of options; the Figma examples are not a product maximum.
- Indeterminate is normally derived from child state when used for parent/select-all behavior.
- The exact product rule for activating an Indeterminate parent belongs to the consuming feature; the base component only represents the mixed state.

## Keyboard and Accessibility

Prefer native checkbox inputs where implementation allows.

Expected behavior:

- `Tab` / `Shift+Tab` moves through enabled Checkbox controls according to normal document order;
- `Space` toggles the focused Checkbox;
- disabled options are not activatable;
- keyboard focus remains visibly distinct from Checked and Indeterminate states;
- Indeterminate exposes a mixed state such as `aria-checked="mixed"` where native semantics do not provide it automatically.

Visible item text must be programmatically associated with the Checkbox control.

A labeled Checkbox Group should use appropriate grouping semantics such as `fieldset` / `legend` where appropriate, or an equivalent accessible group label.

The full labeled option should remain an operable target. Runtime implementation should preserve at least a 24×24 CSS-pixel operable target or equivalent compliant spacing without enlarging the visible 20px icon.

Do not rebuild native checkbox semantics with generic `div` elements and ad-hoc key handlers without a justified implementation requirement.

## RTL

RTL/LTR is a layout direction, not a Checkbox variant axis.

- The control sits at logical inline-start.
- The label sits at logical inline-end.
- In JobVision's RTL authoring examples, this renders as control on the right and label on the left.
- Runtime LTR layouts mirror through logical layout/CSS direction rather than using a `Position=Start|End` component variant.
- Group Direction remains `Vertical` or `Horizontal`; it does not encode RTL/LTR.

## Validation

Validation belongs to the shared field/group composition.

- Do not add `Error` or `Warning` as Checkbox interaction-state variants.
- Group-level error/helper content describes the shared decision.
- A validation message must not replace the accessible group label.
- Disabled is not a validation state.

## Loading

Loading is not part of the base Checkbox state matrix.

If a screen needs loading placeholders, render a Skeleton pattern for the option list rather than multiplying Checkbox selection variants by `Skeleton`.

## Indeterminate / Select-all

Indeterminate is a visual and semantic mixed state, not an independent persisted answer.

For parent/select-all patterns:

- parent Checked generally means all relevant children are selected;
- parent Unchecked generally means no relevant children are selected;
- parent Indeterminate generally means some, but not all, relevant children are selected;
- the consuming product owns the exact child-selection update when the parent is activated.

Do not add a separate `Select all` visual variant to the base Checkbox.

## Product Variations

Checkbox is a shared JobVision/Cando component.

Product and Appearance differences resolve through the Theme/Semantic token architecture. Do not create product-specific Checkbox variants.

## Figma Reference

File: `-DS- Job Vision`

File key: `rROD8ctH9UfPGAMrRrOzHe`

### Checkbox

- Component Set: `Checkbox / Default`
- Node: `3193:29303`
- Component key: `af1fdbe97bf103d8ae5e4540d36f4ffb284cc35b`
- Variant properties: `Selection / State`
- Content properties: `Label / Show label`

### Checkbox Group

- Component Set: `Checkbox Group / Default`
- Node: `23020:127117`
- Component key: `9c6f915d8bc3399d2f02fd0aad20218757b0749f`
- Variant properties: `Direction`
- Content properties: `Group label / Show group label`
- Vertical variant preserves the reconciled legacy group component node `3200:36969`.

The Figma page also contains Axes & properties, real-instance Playground coverage for states/multiline/group direction, and a migration note for removed legacy structures.

## Runtime / Storybook Reference

Code repository/package: **Unregistered**

Runtime component/API: **Unverified**

Storybook: **Unregistered**

Figma property → runtime prop mapping: **Unverified**

Do not infer exact DOM structure, event names, prop names, or implementation API from Figma. Register the owning runtime Design System source before mapping these details.

## Migration Notes

The legacy Checkbox component set was reconciled in place to preserve its stable component identity.

The canonical visual control now uses the exact local JobVision icon-library components `Icon/check_box_outline_blank`, `Icon/check_box`, and `Icon/indeterminate_check_box`. These are nested directly at 20px; no custom Checkbox box or hand-drawn check/indeterminate artwork is maintained.

Removed legacy structures/axes:

- standalone top Field label;
- `Indented` spacer;
- `Skeleton` variants;
- fixed five-item Checkbox Group;
- Slot-based Checkbox Group experiment;
- custom filled-box selection treatment;
- separate Hover/Active variants.

The canonical model intentionally mirrors Radio's sizing, typography, label behavior, focus treatment, RTL geometry, group-direction model, and documentation-page structure while preserving Checkbox-specific multi-selection and Indeterminate semantics.
