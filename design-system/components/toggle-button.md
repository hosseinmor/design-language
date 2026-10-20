---
id: design-system.component.toggle-button
collection: design-system
type: component
title: Toggle Button
summary: Toggle Button represents a Button-like control with persistent selected and unselected states.
knowledge_state: unverified
document_maturity: draft
related:
- design-system.component.rich-text-editor
---

# Toggle Button

## Purpose

Toggle Button represents a Button-like control with persistent selected and unselected states.

It is separate from the action Button component because selected state represents a value, mode, or choice rather than completion of a one-time action.

## Selection Model

Document whether the control supports:

- Independent on/off selection
- Single selection within a group
- Multiple selection within a group

## v4 Selection Semantics

Selection is a component state, not a complete global color family.

Do not bind every Toggle Button to one universal selected token. Choose the treatment according to the component anatomy and required emphasis.

Possible approved directions include:

```text
Chromatic checked/on treatment
→ surface/accent-emphasis + fg/on-color

Strong neutral current/exclusive treatment
→ surface/neutral-emphasis + fg/on-color

Selected container treatment when appropriate
→ surface/selected + fg/primary
```

A selected/on Toggle Button may use Accent as its visual cue, but Accent itself does not mean Selected.

Disabled suppresses tone:

```text
Disabled filled control
→ surface/disabled + fg/disabled
```

Do not use Brand semantics to represent selected/on state merely because Brand and Accent share Blue in JobVision.

The exact default mapping for Toggle Button remains a component-level design decision and must be validated with the final anatomy rather than inferred from the old v3 Selected matrix.

See `../../foundations/interaction/selection.md`.

## Known TBD Use Case

Rich Text Editor currently uses a temporary internal `_Rich Text Toolbar Toggle` to represent persistent selected formatting such as Bold, list type, alignment, and text direction.

TBD when the shared Toggle Button component is designed:

- define whether `Icon Toggle Button` is a first-class shared form of Toggle Button;
- replace the Rich Text Editor internal toggle with the shared component;
- preserve the semantic distinction between persistent `Selected` state and transient Button `Active` interaction state;
- define group behavior for independent/multiple selection versus mutually-exclusive single selection.

This is intentionally deferred; the current Rich Text Editor internal toggle is temporary and must not be treated as the final shared Toggle Button API.

## Not Yet Defined

The shared guideline does not yet define:

- Toggle Button anatomy
- Group behavior
- Keyboard model
- Exact states
- Default mapping for unselected rest state
- Whether the default selected treatment is Accent or strong Neutral
- Sizes

These require a separate component guideline.
