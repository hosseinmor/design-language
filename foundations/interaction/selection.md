---
id: design-system.experience-rule.selection
collection: design-system
type: experience-rule
title: Selection
summary: Selection is a component state, not a general color family.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Selection

## Scope

This foundation owns **cross-component interaction meaning** for a selected/current/checked/on/applied state. It does not define a separate global Selected Color matrix or override specific component state machines.

## Selection taxonomy

- `selected`: an item belongs to the current choice set; single- and multi-selection are distinct contracts.
- `current`: the active destination or position, such as the current Tab or pagination item; it does not necessarily mean a selectable value.
- `checked`: a selection control has a checked state, including mixed/indeterminate where the owning component supports it.
- `on`: a Toggle/Switch represents an enabled boolean setting.
- `applied`: a Filter is currently active; changing it may directly change results rather than merely edit a draft selection.

These are distinct interaction meanings; a shared hue or token name does not make their behaviors interchangeable. A component or pattern defines whether selection occurs immediately, can be undone, permits multiple values, and remains interactive while selected.

## Interaction rules

- Do not invent Hover/Active styles for a current, non-interactive item. Only provide interaction states when the item still has a meaningful operation.
- A persistent selected item that remains interactive may receive a selected-hover treatment; the exact semantic role and recipe belong to the [Color Token Usage](../../design-system/tokens/color/usage.md) and owning component.
- Selecting, applying, dismissing or clearing a value are different actions; the component/pattern determines their semantics.
- For actual state machines, keyboard selection and focus, consult the relevant [Tabs](../../design-system/components/tabs.md), [Checkbox](../../design-system/components/checkbox.md), [Choice Group](../../design-system/components/choice-group.md), [Chip](../../design-system/components/chip.md), and [Table](../../design-system/components/table.md) contracts.

## Color and accessibility ownership

The [Color Semantics](../../design-system/tokens/color/semantics.md) document owns Accent, Neutral and selected-container role meanings; [Color Usage](../../design-system/tokens/color/usage.md) owns token recipes and retired Color roles. Do not repeat token inventories or historic v3 migration tables here.

Accessibility and keyboard/focus requirements belong to the owning component and [Accessibility](../../accessibility/keyboard-navigation.md); state cannot rely on color alone.

## Open scope

Specific selection behaviors for future components, such as a new selectable-card or pagination contract, remain TBD until those components are reviewed. This draft does not imply their implementation exists.
