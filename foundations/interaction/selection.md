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

## Principle

Selection is a component state, not a normal action Button state and not a complete global color family.

A component may call the state:

```text
selected
current
checked
on
applied
```

The state name does not require a same-named global color token.

Use a dedicated selection component or pattern such as:

- Toggle Button
- Segmented Control
- Filter Button
- Applied Filter Chip
- Tab
- Selectable Card
- Selectable row/list item

The items above are a selection taxonomy. Their presence in this document does not by itself mean every item already has a complete shared component specification.

## Semantic Treatment

Choose the visual treatment based on component anatomy.

### Chromatic cue

Use Accent semantics when selection needs a colored indicator:

```text
Selected line Tab
→ fg/primary + line/accent

Checked Checkbox
→ surface/accent-emphasis + fg/on-color

Saved Bookmark
→ fg/accent
```

Accent itself does not mean Selected. The component state is using Accent as its visual cue.

A selected line Tab does not need a selected Hover state when the selected Tab itself has no meaningful interaction. Hover on unselected Tabs does not imply Hover on the current Tab.

### Persistent selected container

For rows/items/containers that need a neutral selected background:

```text
surface/selected
surface/selected-hover
```

Examples:

- Selected table row
- Selected dropdown/menu item
- Selected tree node
- Selected navigation item
- Selectable list item

Use `surface/selected-hover` only when the selected container remains interactive while selected. If selected state removes meaningful interaction, use only `surface/selected`.

Use `fg/primary` for ordinary content unless the component specification defines another semantic foreground.

### Strong neutral selection

When a current/exclusive choice is clearly communicated by component anatomy and grouping, a component may use an existing strong Neutral treatment such as `surface/neutral-emphasis` rather than introducing a global selected-emphasis token.

Pill Tabs, Segmented Controls, and current Pagination are examples that should be decided in their component specs. When the selected/current item is not meaningfully interactive, do not generate Hover/Active states merely because the underlying Neutral family has them available.

## Removed v3 Selected Color Matrix

Do not use:

```text
surface/selected-muted*
surface/selected-emphasis*
surface/selected-disabled
surface/selected-inverse*
fg/selected
line/selected
fg/on-color-disabled
```

Only the neutral persistent-container roles remain globally approved:

```text
surface/selected
surface/selected-hover
```

`surface/selected-hover` is conditional on continued interaction; it is not a universal selected-state requirement.

## Brand Separation

Do not use Brand semantics to represent selection merely because Brand and Accent happen to share a hue in JobVision.

Brand communicates product identity or an approved key conversion moment. Selection is a component state and should be expressed with Accent, Neutral, or the minimal selected-container surface according to anatomy.

## Applied Filter

Treat `applied` as a valid selection-like component state, but do not force it into one global visual treatment.

A tonal applied-filter treatment is a validated use case for Accent Muted when the filter remains interactive:

```text
Applied Filter Chip
→ surface/accent-muted
→ surface/accent-muted-hover when interactive
→ surface/accent-muted-active when a pressed/active visual is required
→ fg/accent or fg/primary according to anatomy
→ line/accent only if the component has a semantic Accent outline
```

First try shared Semantic roles. If the Filter Chip needs a stable component-specific applied treatment that cannot be represented semantically, create a reviewed `filter-chip/*` Component token contract. Do not consume Tag tokens as a generic palette unless the UI is actually rendering the Tag component.

## Stress-Test Summary

The current Color architecture resolves common selection anatomies without a full Selected color matrix:

```text
Line Tab           → Accent indicator
Checked Checkbox   → Accent Emphasis
Applied Filter     → Accent Muted
Selected Row       → Selected surface
Strong Pill choice → Neutral Emphasis
```

The treatment communicates selection; the token family name does not need to repeat the component state name.

## Related Documents

- `../../design-system/components/toggle-button.md`
- `../../design-system/components/button.md`
- `../../design-system/tokens/color/semantics.md`
- `../../design-system/tokens/color/component-tokens.md`
