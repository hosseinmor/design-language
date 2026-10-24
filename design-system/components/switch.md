---
id: design-system.component.switch
collection: design-system
type: component
title: Toggle
summary: Toggle is the canonical binary on/off control for settings that take effect immediately.
knowledge_state: canonical
document_maturity: reviewed
last_reviewed: '2026-09-19'
related:
  - design-system.component.checkbox
  - design-system.reference.component-mapping
---

# Toggle

## Purpose

Toggle is the canonical binary on/off control for a setting whose change takes effect immediately.

The canonical product/design term is **Toggle**. The repository path and document id retain the older `switch` identifier for compatibility with existing references.

## When to Use

Use Toggle when:

- a single setting has two persisted states: On and Off;
- changing the control takes effect immediately;
- users benefit from seeing the current state directly in the control.

## When Not to Use

Do not use Toggle when:

- the choice belongs to a form or batch submission flow; use Checkbox when the value is committed with the form;
- the control is a momentary action; use Button;
- a button-like control needs a persistent pressed/unpressed state; use Toggle Button;
- users choose one option from a set; use Radio or Segmented Control as appropriate.

## Anatomy

Toggle contains:

1. **Track** — the state surface.
2. **Thumb** — the movable state indicator.
3. **Label** — the optional visible label associated with the whole control row.

The visible label and Toggle form one logical interaction target. A label-less Toggle is allowed only when another persistent accessible name exists in product context.

## Variants and Properties

Canonical Figma axes:

| Property | Values |
|---|---|
| `Size` | `Medium`, `Small` |
| `State` | `Default`, `Hover`, `Active`, `Focus`, `Disabled`, `Read-only` |
| `Toggled` | `False`, `True` |

Content properties:

| Property | Type | Default |
|---|---|---|
| `Label` | Text | `Toggle label` |
| `Show label` | Boolean | `True` |

There is no Skeleton axis, no separate `Toggle only` axis, and no checkmark inside the Small Toggle.

## Sizes

| Size | Track | Thumb | Minimum authored row height |
|---|---:|---:|---:|
| Medium | 48 × 24 | 18 × 18 | 24 |
| Small | 32 × 16 | 10 × 10 | 24 |

The Small visual track remains 32 × 16 while the authored row preserves a 24px minimum height.

## States and Visual Treatment

### Off

| State | Track | Thumb |
|---|---|---|
| Default | `surface/neutral-muted` | `palette/bw/white` |
| Hover | `surface/neutral-muted-hover` | `palette/bw/white` |
| Active | `surface/neutral-muted-active` | `palette/bw/white` |
| Focus | Default Off track + shared [Focus Management](../../accessibility/focus-management.md) treatment | `palette/bw/white` |
| Disabled | `surface/disabled` | `palette/bw/white` |

Default, Hover, Active, and Disabled do not use a persistent border.

The fixed white Thumb is an intentional visual exception and binds directly to the Primitive `palette/bw/white`; no Toggle-specific Component Token is required.

### On

| State | Track | Thumb |
|---|---|---|
| Default | `surface/accent-emphasis` | `palette/bw/white` |
| Hover | `surface/accent-emphasis-hover` | `palette/bw/white` |
| Active | `surface/accent-emphasis-active` | `palette/bw/white` |
| Focus | Default On track + shared [Focus Management](../../accessibility/focus-management.md) treatment | `palette/bw/white` |
| Disabled | `surface/disabled` | `palette/bw/white` |

Brand and Success semantics are not used to communicate the On state.

### Read-only

Read-only is a distinct product/display state and retains a separate visual treatment:

- Off: `surface/default` + `line/default`; Thumb `fg/secondary`
- On: `surface/accent-muted` + `line/accent`; Thumb `fg/accent`

Do not infer a native HTML `readonly` behavior from this Figma state. Exact runtime semantics remain unverified.

## Theme Behavior

The neutral interactive surface scale is deliberately distinct from structural muted surfaces in Dark mode:

```text
surface/muted                → neutral/800
surface/neutral-muted        → neutral/700
surface/neutral-muted-hover  → neutral/600
surface/neutral-muted-active → neutral/500
```

This prevents neutral controls such as Off Toggle from collapsing into a muted structural background.

## Behavior

- Toggle represents a binary persisted setting.
- A user change takes effect immediately rather than waiting for a form-submit action.
- Thumb position is the primary redundant state cue; color is supportive and must not be the only cue.
- Disabled and Read-only do not receive Hover or Active treatment.
- Focus is independent from the current On/Off state.

## Label Guidance

- Prefer a visible concise label.
- The label describes the setting, not the action required to change it.
- Avoid labels that require the user to decode On/Off wording twice.
- When `Show label=False`, another persistent accessible name must exist.

## Motion

Use a short Thumb translation with a coordinated Track-color transition.

- Motion must not delay state feedback.
- Respect reduced-motion preferences in runtime implementations.
- Exact duration, easing, and implementation mechanism are not registered yet; do not invent component-specific constants.

## RTL

RTL is the primary authored direction in the canonical Figma component:

- Off places the Thumb on the right.
- On places the Thumb on the left.

Runtime direction should mirror the control in LTR rather than introduce a separate RTL variant axis.

## Accessibility

The production implementation must:

- expose switch semantics appropriate to the target platform;
- expose the current binary state programmatically;
- provide an accessible name from the visible label or another persistent source;
- support keyboard operation appropriate to the platform;
- preserve a visible focus indication;
- avoid relying on color alone to communicate On versus Off.

Exact DOM element choice, event API, prop names, and ARIA implementation are **unregistered / unverified** until an owning runtime source is registered.

## Product Variations

JobVision and Cando share the same component contract and public Semantic roles. Product and Appearance differences resolve through the Theme/token architecture rather than through Toggle variants.

## Figma Reference

Canonical editable source:

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Toggle`
- Page node: `467:0`
- Documentation frame: `22927:130230`
- Component set: `Toggle`
- Component set node: `22928:125569`
- Component key: `0c632b79747ffac5f05a4f2c762f81ddcb8293d7`
- Variant count: `24 = 2 Size × 6 State × 2 Toggled`

Legacy Toggle construction remains on the page for migration reference and is not the canonical component.

## Code Reference

- Code repository/package: **Unregistered**
- Runtime component/API: **Unverified**
- Storybook: **Unregistered**
- Figma-property → runtime-prop mapping: **Unverified**
- Code Connect: **No registered mapping**

Do not infer runtime prop names or DOM structure from the Figma property model.

## Known Gaps

- Exact runtime component/API and Storybook identity are not registered.
- Exact motion duration/easing is not registered.
- Read-only runtime semantics require validation before implementation.
- Legacy Figma Toggle instances may still require migration to the canonical set.

## Related Guidance

- `checkbox.md`
- `toggle-button.md`
- `../../foundations/interaction/selection.md`
- `../tokens/color/aliases.md`
- `../../integrations/component-mapping.md`
