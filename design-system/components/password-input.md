---
id: design-system.component.password-input
collection: design-system
type: component
title: Password Input
summary: Password Input captures a secret single-line value through the shared RTL-first Field contract, with native-password-oriented masking and a dedicated reveal/hide action.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.text-input
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Password Input

## Purpose

Password Input captures a secret single-line value.

It shares the same reusable Field contract as Text Input for:

- Label;
- Required marker;
- optional Info affordance;
- Helper and Error content;
- Disabled and Read only semantics;
- Focus and validation treatment;
- RTL layout;
- Small / Medium / Large control sizing.

Password Input adds one specialized behavior: a dedicated visibility action that can reveal or hide the entered password.

Use the canonical Password Input instead of composing a generic Text Input with an arbitrary trailing icon. The reveal/hide action has its own semantics, accessibility requirements, and authoring behavior.

## When to Use

Use Password Input for values that should normally be obscured, such as:

- current password;
- new password;
- password confirmation;
- other credential secrets when a password-style input is the correct product primitive.

## When Not to Use

Do not use Password Input for:

- ordinary single-line text → use Text Input;
- one-time verification codes → use the appropriate verification-code pattern;
- API keys, tokens, or secrets whose copy/reveal behavior materially differs from passwords → define the relevant specialized pattern;
- immutable masked data that is not an editable form field.

## Canonical Figma API

Component set: `Password Input`

Figma node: `22823:128654` in `-DS--Job-Vision-NEXT`.

### Top-level properties

| Property | Values / behavior |
|---|---|
| `Size` | `Small`, `Medium`, `Large`; `Medium` is default |
| `State` | `Default`, `Hover`, `Focus`, `Error`, `Error focus`, `Disabled`, `Read only`, `Read only focus` |
| `Filled` | Boolean Figma-authoring switch; `False` shows Placeholder, `True` shows masked content |
| `Placeholder` | Placeholder copy |
| `Value` | Actual password value used when the password is revealed |
| `Show password` | Boolean Figma-authoring switch; reveals Value and switches the visibility affordance |
| `Show label` | Shows/hides the visible label row |
| `Show helper` | Shows/hides helper content in non-error states |

### Contextual nested properties

`Field label` exposes:

- `Label`
- `Required`
- `Show info`

Supporting content is contextual:

- non-error states → `Helper > Text`
- Error / Error focus → `Error > Text`

## Figma-only Authoring Properties

### Filled

`Filled` is an authoring convenience, not a runtime state.

```text
Filled = False
→ Placeholder visible

Filled = True
→ masked password representation visible
```

Runtime implementation should derive empty/filled presentation from the actual native input value.

### Show password

`Show password` is also a Figma authoring convenience.

```text
Show password = False
→ masked representation visible
→ visibility icon represents “show password”

Show password = True
→ Value visible
→ visibility-off icon represents “hide password”
```

Runtime visibility must be driven by the password input's actual type/visibility behavior, not by a Figma-only state prop.

The fixed mask shown in Figma is representational only. It does not encode or reveal the actual password length.

## Anatomy

```text
Password Input
├── Field label
│   ├── Label
│   ├── Required marker
│   └── Optional info affordance
├── Control
│   ├── Content
│   │   ├── Placeholder
│   │   ├── Masked representation
│   │   └── Revealed Value
│   └── Visibility action
│       ├── Show-password icon
│       └── Hide-password icon
└── Supporting content
    ├── Helper
    └── Error
```

The visibility action is specialized and built into Password Input. It is not a generic trailing-icon slot.

## Sizes and Geometry

| Size | Control height | Inline padding |
|---|---:|---:|
| Small | 32 px | 12 px |
| Medium | 40 px | 16 px |
| Large | 48 px | 16 px |

Shared geometry:

- Medium is the default size.
- Border radius: `6px`.
- Gap between visibility action and content: `8px`.
- Gap between Field label, Control, and Supporting content: `4px`.
- Visibility glyph: `16×16px`.
- Visibility action area: `24×24px`.
- The action area sits at the trailing/left edge in RTL.
- Error border is a 2px overlay and must not alter padding or height.
- The Focus indicator is separate from the control border and follows the shared [Focus Management](../../accessibility/focus-management.md) contract.
- Width is flexible and resizing must preserve padding, action position, and RTL order.
- In Figma, Placeholder, masked content, and revealed Value fill the available Content width, remain single-line, and use ending ellipsis for overflow. Runtime password editing may use native horizontal scrolling instead of reproducing ellipsis while the value is actively edited.

## RTL and Directionality

Password Input is RTL-first for the current JobVision/Cando context.

In RTL:

```text
right edge
→ password content
→ visibility action
→ left edge
```

Rules:

- Placeholder and Value are right-aligned by default.
- The visibility action is on the left/trailing side.
- Small keeps 12px from the outer edge to the action area.
- Medium/Large keep 16px from the outer edge to the action area.
- Field-label visual order is `Label → Required → Info` from the RTL starting edge.
- Password value direction must remain usable for mixed Latin, numeric, and symbol content; Product/Frontend may need to apply an explicit direction strategy independently from surrounding RTL chrome.

## State Model

Password Input uses the same visual state model as Text Input.

### Default

- surface → `surface/default`
- line → `line/default`
- Placeholder → `fg/placeholder`
- password content → `fg/primary`
- visibility affordance → `fg/secondary`
- Label → `fg/secondary`
- Helper → shared helper foreground

### Hover

- line → `line/emphasis`
- geometry does not change.

### Focus

```text
Control border → line/emphasis, 1px
Focus indicator → shared [Focus Management](../../accessibility/focus-management.md) contract
```

### Error

```text
Error border → line/error, 2px
Error message → fg/error
Programmatic invalid state → required in implementation
```

Error message is required; a red border alone is insufficient.

### Error focus

```text
Error border → line/error, 2px
Focus indicator → shared [Focus Management](../../accessibility/focus-management.md) contract
Error message → fg/error
```

### Disabled

```text
surface → surface/disabled
line → line/disabled
content → fg/disabled
visibility affordance → fg/disabled
```

The reveal/hide action is unavailable when the password field is disabled.

### Read only

```text
surface → surface/default
line → line/muted
content → normal readable foreground
```

Read only is distinct from Disabled.

### Read only focus

Readonly native inputs remain focusable, so the Figma contract includes `Read only focus`; it preserves Read only styling while visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) contract.

Whether a readonly password may still be revealed is a product/runtime behavior decision; do not infer implementation behavior solely from the Figma authoring switch.

## Visibility Action

The visibility action is a real interactive control in runtime.

Requirements:

- expose a clear accessible name such as “Show password” / “Hide password”;
- update the accessible name when visibility changes;
- make the action keyboard operable;
- keep it in a predictable focus order;
- do not clear or replace the password value when toggled;
- preserve selection/caret behavior as far as the platform implementation allows;
- keep the action visually disabled when the field itself is disabled.

The Figma component uses a 16px glyph in a 24px action area. Runtime implementation may provide a larger effective hit target when needed by the platform/accessibility contract, as long as visible geometry remains aligned.

## Password Content

### Placeholder

Placeholder is optional guidance and must not be the only accessible name.

### Masked representation

The Figma mask is visual shorthand only.

Do not:

- infer password length from the number of Figma mask characters;
- implement a custom masking algorithm merely to copy the Figma representation;
- replace native password semantics with a custom text widget.

### Revealed Value

When visible, the actual password value is shown as ordinary readable text inside the same control geometry.

The reveal/hide operation must not:

- change control size;
- move the label;
- change validation state;
- destroy the actual value.

## Behavior

- Prefer native password-input semantics.
- Preserve browser password-manager behavior.
- Preserve paste/copy policy unless Product has an explicit justified requirement.
- Preserve autofill and credential-management behavior.
- Do not add Active/Pressed as a field state.
- Do not add Warning without a validated semantic use case.
- Do not use Skeleton as a Password Input state.
- `Filled` and `Show password` are Figma authoring properties only.
- Long values remain single-line and contained within the Control.

## Semantic Color Mapping

Password Input consumes shared Semantic roles.

| Part / state | Semantic role |
|---|---|
| Label | `fg/secondary` |
| Placeholder | `fg/placeholder` |
| Masked / revealed value | `fg/primary` |
| Helper | shared helper foreground |
| Error content | `fg/error` |
| Visibility affordance | `fg/secondary` |
| Default surface | `surface/default` |
| Default line | `line/default` |
| Hover / Focus line | `line/emphasis` |
| Error line | `line/error` |
| Disabled surface | `surface/disabled` |
| Disabled line | `line/disabled` |
| Disabled content/action | `fg/disabled` |
| Read-only line | `line/muted` |
| Focus indicator | shared [Focus Management](../../accessibility/focus-management.md) contract |

Do not create Password-Input-specific Color tokens merely to restate these roles.

## Accessibility

Password Input is a Level 2 stateful native-based form component with an additional interactive visibility action.

### Native primitive

Prefer a native HTML `<input type="password">` as the baseline primitive.

When revealing the password, implementation may switch the native input type in a way that preserves the input's value, label, descriptions, and focus behavior.

Do not recreate password editing/masking with a custom contenteditable widget.

### Accessible name

- Provide a meaningful label or equivalent accessible-name mechanism.
- Placeholder must not be the only accessible name.
- Requiredness must be communicated programmatically and visually.

### Visibility action

- Must have an accessible name independent of the glyph.
- Name/state must communicate the available action.
- Must be keyboard reachable/operable unless the implementation uses an equivalent accessible mechanism.
- Must not trap keyboard focus.
- Must not rely on eye/eye-off icon meaning alone.

### Error and description relationships

When invalid:

- expose invalid state programmatically;
- associate Error text with the password input;
- keep visible focus independently from Error styling.

### Autofill and password managers

The component mechanism must allow Product to supply correct autocomplete intent, typically concepts equivalent to:

- `current-password`
- `new-password`

The Design System does not choose which one applies.

Do not block browser/password-manager functionality without a product requirement and accessibility/security review.

### QA scenarios

Test:

- empty and filled;
- masked and revealed;
- Small / Medium / Large;
- keyboard reveal/hide;
- Focus / Error focus / Read only focus;
- Disabled;
- long generated passwords;
- mixed Latin, digit, and symbol values;
- password-manager/autofill behavior;
- zoom/text enlargement;
- RTL chrome with LTR password value;
- required + info;
- helper and error copy.

## Mechanism vs Product Policy

| Password Input / Design System owns | Product / Form owns |
|---|---|
| Label/Required/Info mechanism | Actual label and requiredness |
| Masked/revealed presentation mechanism | Whether reveal is enabled in a product context |
| Visibility-action visual/accessible mechanism | Exact action copy if product localization differs |
| Helper/Error association mechanism | Actual helper/error copy |
| Invalid visual/semantic mechanism | Validation rules and timing |
| Disabled / Read only support | Which state applies |
| Autocomplete/type pass-through | `current-password` vs `new-password` and related product intent |
| Focus visuals | Form-level failed-submit recovery |
| Size/geometry contract | Contextual size selection |

## Development Contract

The exact Angular/package API is not yet registered as a canonical runtime source.

Implementation should support concepts equivalent to:

```text
PasswordInput
- size: sm | md | lg
- value
- placeholder
- disabled
- readonly
- invalid
- required
- label / accessible-name mechanism
- helper / error description mechanism
- password visibility toggle
- native input attributes
- autocomplete / input-purpose pass-through
```

Do not model Figma-only authoring concepts as required runtime props:

```text
Filled          → derive from actual value
Hover           → CSS/platform state
Focus           → CSS/platform state
Error focus     → invalid + focus
Read only focus → readonly + focus
Show password   → runtime visibility behavior/state, not a visual-only prop contract
```

The runtime may expose Password Input as a specialized component or as a Text Input wrapper around a native password input. That package/API decision remains unverified until the code source is registered.

## QA Checklist

Verify:

- all 24 Size × State variants exist;
- Medium is default;
- Small / Medium / Large control heights are 32 / 40 / 48px;
- inline padding is 12 / 16 / 16px;
- Filled toggles Placeholder vs masked content without destroying Value;
- Show password reveals Value and simultaneously switches eye → eye-off;
- visibility action remains trailing/left in RTL;
- visibility glyph is 16px inside a 24px action area;
- helper expands outer height without changing Control height;
- Error border is 2px without layout shift;
- Error focus preserves Error + Focus;
- Read only focus remains visibly focused;
- Disabled uses disabled surface/line/content/action;
- horizontal resize preserves padding, action position, overlays, and clipping;
- Small/Large component-property bindings remain functional;
- long secret values remain single-line and contained; in Figma, Placeholder, masked content, and revealed Value use Fill + ending ellipsis;
- Figma mask is not treated as real password length.

## Figma Reference

Canonical editable source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Password Input`
- Page node: `3556:37675`
- Documentation frame: `22890:124582`
- Header: `22890:124583`
- Variant matrix: `22890:124590`
- Axes & properties: `22890:124591`
- Canonical component set: `Password Input`
- Component set node: `22823:128654`
- Playground: `22890:125615`
- Examples: `22824:129182`

Shared internal Field helpers are owned by the Text Input family. Password Input has no separate public sub-component; its visibility action is embedded in the control.

Legacy Password Input base, Outline, Fill, Warning, Skeleton, and old documentation assets were removed from the canonical Figma page.

## Code / Storybook Reference

No runtime component package or Storybook source is currently registered as canonical for Password Input.

Do not infer the exact Angular API, class names, DOM wrapper structure, or visibility-button implementation from Figma alone.

## Open Items

- register the canonical runtime/Storybook source when available;
- align exact Angular/Tailwind API with Frontend;
- confirm whether runtime exposes a dedicated `PasswordInput` or a specialized Text Input API;
- confirm the final implementation hit-target strategy for the visibility action while preserving visual geometry;
- verify password-manager/autofill behavior in Storybook/browser tests.

These open items do not block the current visual and authoring contract.

## Related Documents

- `./text-input.md`
- `./textarea.md`
- `../../accessibility/forms.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/color/semantics.md`
- `../tokens/color/usage.md`
- `../../foundations/visual/radius.md`
