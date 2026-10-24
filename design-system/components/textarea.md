---
id: design-system.component.textarea
collection: design-system
type: component
title: Textarea
summary: Textarea captures multiline free text through the shared RTL-first Field contract, with optional helper/count content, validation, and vertical resizing.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.text-input
- design-system.component.rich-text-editor
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Textarea

## Purpose

Textarea captures or displays multiline free text.

It shares the same reusable Field contract as Text Input for:

- Label;
- Required marker;
- optional Info affordance;
- Helper and Error content;
- Disabled and Read only semantics;
- Focus and validation treatment;
- RTL behavior.

Textarea adds multiline-specific behavior:

- a taller resizable control;
- optional character/count metadata;
- multiline overflow and text wrapping;
- a resize affordance.

Use the canonical Textarea instead of rebuilding label, validation, counter, or resize patterns ad hoc.

## When to Use

Use Textarea when users need to enter free text that may span multiple lines, such as:

- descriptions;
- notes;
- comments;
- explanations;
- longer profile or form content;
- free-text feedback.

## When Not to Use

Do not use Textarea when:

- the expected value is a single short line → use Text Input;
- the user chooses from a known option set → use a selection component;
- the content needs rich formatting, toolbar actions, mentions, attachments, or structured editing → use a dedicated rich-text/editor pattern;
- the content is immutable and does not need form semantics → use ordinary readable content unless readonly form semantics are required.

Legacy `Text area with toolbar` components are not part of the canonical Textarea contract.

## Canonical Figma API

Component set: `Textarea`

Figma node: `22800:128313` in `-DS--Job-Vision-NEXT`.

### Top-level properties

| Property | Values / behavior |
|---|---|
| `State` | `Default`, `Hover`, `Focus`, `Error`, `Error focus`, `Disabled`, `Read only`, `Read only focus` |
| `Supporting` | `Hidden`, `Visible` |
| `Filled` | Boolean Figma-authoring switch; `False` shows Placeholder, `True` shows Value |
| `Placeholder` | Placeholder copy, preserved independently from Value |
| `Value` | Multiline entered/displayed value, preserved independently from Placeholder |
| `Show label` | Shows/hides the visible label row |
| `Resizable` | Shows/hides the Figma resize affordance; default `True` |

Default variant:

```text
State = Default
Supporting = Hidden
Filled = False
Resizable = True
```

### Contextual nested properties

`Field label` exposes:

- `Label`
- `Required`
- `Show info`

When `Supporting=Visible` in non-error states, the nested Supporting row exposes:

- `Show helper`
- `Show count`
- `Count`
- `Helper > Text`

In Error / Error focus, Error text is mandatory. The nested Error row exposes:

- `Show count`
- `Count`
- `Error > Text`

### Supporting semantics

`Supporting` is a structural Figma axis because the outer Textarea height must remain freely resizable.

For non-error states:

```text
Supporting = Hidden
→ no supporting row

Supporting = Visible
→ fixed supporting row
→ Helper and/or Count can be configured
```

For Error and Error focus:

```text
Supporting = Hidden
→ Error row still remains visible

Supporting = Visible
→ Error row remains visible
→ optional Count can also be shown
```

Error text is never hidden by `Supporting=Hidden`.

## Filled is Figma-only Authoring State

Like Text Input, `Filled` exists only to make Figma authoring efficient.

```text
Filled = False
→ Placeholder visible
→ Value retained but not displayed

Filled = True
→ Value visible
→ Placeholder retained but not displayed
```

`Filled`:

- is not a filled-background visual style;
- is not a runtime interaction state;
- should not become a required public implementation prop.

Runtime display should derive from the actual textarea `value` and `placeholder`.

## Anatomy

```text
Textarea
├── Field label
│   ├── Label
│   ├── Required marker
│   └── Optional info affordance
├── Control
│   ├── Placeholder / Value
│   └── Resize affordance
└── Supporting row
    ├── Count                 ← left in RTL
    └── Helper / Error        ← right in RTL
```

The shared Field-label and message primitives come from the same family used by Text Input.

## Geometry

### Default dimensions

- default width: `288px`
- default Control height: `120px`
- minimum Control height: `120px`
- inline/block Control padding: `16px`
- Control radius: `6px`
- Field spacing: `4px`
- Supporting row height: `20px`
- resize handle: `8×8px`
- resize handle inset: `8px` from the left and bottom edges in RTL

Default outer heights:

```text
Non-error + Supporting Hidden → 144px
Non-error + Supporting Visible → 164px
Error / Error focus            → 164px minimum
```

### No Size axis

Textarea does not expose Small / Medium / Large.

Its useful density is governed primarily by available multiline height, not by the single-line control-height scale. Adding multiple Textarea sizes would multiply states without a validated product need.

If future products require a compact multiline control, treat that as a new use case rather than assuming Text Input size variants should be copied.

## Resizing

Textarea instances are vertically resizable in Figma.

The outer instance owns the resize interaction:

- the Field and Control absorb added vertical height;
- Label height stays stable;
- Supporting row height stays stable;
- Border and Value overlay stretch with the Control; the Control is the perceived Focus target and follows the shared [Focus Management](../../accessibility/focus-management.md) treatment;
- the resize handle remains anchored to the bottom-left in RTL;
- minimum Control height remains `120px`.

Horizontal resizing is also supported for layout authoring; padding and supporting-row order remain stable.

### RTL resize handle

The canonical Figma resize handle is a mirrored internal component:

- `_Textarea Resize Handle`
- node `22810:748`

It is designed for bottom-left placement in RTL rather than moving a bottom-right glyph without mirroring it.

The exact browser/runtime rendering of a native textarea resize handle is user-agent dependent. The Figma handle expresses the intended affordance and RTL direction; Frontend should preserve native textarea behavior where possible and confirm any custom handle implementation separately.

## RTL and Directionality

Textarea is RTL-first for the current JobVision/Cando context.

Rules:

- Label, Placeholder, Value, Helper, and Error text are right-aligned by default.
- Count is positioned at the left edge of the supporting row.
- Helper/Error occupies the right side of the supporting row.
- Field-label visual order follows the shared contract: `Label → Required → Info` from the RTL starting edge.
- The resize affordance is bottom-left and mirrored for RTL.
- Mixed Persian/English content must remain readable.
- Content direction and alignment should not be inferred solely from the characters in a single line; Product may need explicit direction behavior for special content.

## State Model

Figma uses a single `State` axis for authoring. Runtime implementation does not need matching public props for interaction-derived states.

### Default

- surface → `surface/default`
- line → `line/default`
- Value → `fg/primary`
- Placeholder → `fg/placeholder`
- Label → `fg/secondary`
- Helper → shared helper foreground
- Count → `fg/tertiary`
- resize affordance → `fg/tertiary`

### Hover

- line → `line/emphasis`
- geometry does not change.

Hover is a CSS/platform interaction state, not normally a runtime component prop.

### Focus

```text
Control border → line/emphasis, 1px
Focus indicator → shared [Focus Management](../../accessibility/focus-management.md) contract
```

Focus does not change Control dimensions or padding.

### Error

```text
Error border → line/error, 2px
Error message → fg/error
Programmatic invalid state → required in implementation
```

Error message is mandatory and remains visible even when `Supporting=Hidden`.

The 2px border is an overlay and does not shift content.

### Error focus

```text
Error border → line/error, 2px
Focus indicator → shared [Focus Management](../../accessibility/focus-management.md) contract
Error message → fg/error
```

Error meaning and keyboard focus remain independently visible.

### Disabled

```text
surface → surface/disabled
line → line/disabled
content → fg/disabled
supporting content → fg/disabled
resize affordance → fg/disabled
```

Disabled is not a substitute for Read only.

### Read only

```text
surface → surface/default
line → line/muted
content → normal readable foreground
```

Read only remains visually and semantically distinct from Disabled.

### Read only focus

A native readonly textarea remains focusable.

Read only focus preserves the Read only treatment while visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) contract.

## Placeholder and Value

Placeholder provides a hint, example, or expected format; it does not replace a field label.

Value is the actual multiline content.

Figma preserves Placeholder and Value independently so designers can toggle `Filled` without rewriting content.

Runtime should preserve normal multiline editing behavior, including:

- selection;
- cursor movement across lines;
- copy/paste;
- line breaks;
- browser text-editing shortcuts;
- scroll behavior when content exceeds the visible height.

## Helper, Error, and Count

### Helper

Helper provides non-critical instructions or context.

Use Helper when the user benefits from information that should remain visible while completing the field.

### Error

Error identifies a validation failure and should explain what is wrong and, when known, how to correct it.

Error must be textual and programmatically associated with the textarea.

A red border alone is insufficient.

### Count

Count is optional metadata in the supporting row.

Typical presentation:

```text
24/100
```

The Design System provides the visual position and formatting mechanism. Product decides:

- whether a count is needed;
- whether the number represents characters, words, or another unit;
- the actual maximum;
- whether exceeding the maximum is prevented, warned, or treated as an Error.

Do not make a changing counter an assertive live region by default; that can create excessive screen-reader announcements. If a limit is materially important, expose it using appropriate native/accessible semantics and description.

## Behavior

- Preserve native multiline text editing.
- Do not add Active/Pressed as a Textarea state.
- Do not use Skeleton as a Textarea state.
- Do not add Warning until a validated product use case requires a distinct warning contract.
- Long content wraps within the Control.
- Content beyond the visible area must not expand through the Control boundary unexpectedly.
- The baseline component is manually resizable rather than auto-growing.
- Auto-growing textarea behavior is not part of the current canonical contract.
- Toolbar/rich-text functionality is not part of Textarea.
- Supporting content must not shrink the Control below its minimum height.
- Changing State or Supporting must not alter padding or horizontal alignment.

## Semantic Color Mapping

Textarea consumes the same shared Semantic roles as Text Input.

| Part / state | Semantic role |
|---|---|
| Label | `fg/secondary` |
| Value | `fg/primary` |
| Placeholder | `fg/placeholder` |
| Helper | shared helper foreground |
| Error content | `fg/error` |
| Count | `fg/tertiary` |
| Resize affordance | `fg/tertiary` |
| Default surface | `surface/default` |
| Default line | `line/default` |
| Hover / Focus line | `line/emphasis` |
| Error line | `line/error` |
| Disabled surface | `surface/disabled` |
| Disabled line | `line/disabled` |
| Disabled content | `fg/disabled` |
| Read-only line | `line/muted` |
| Focus indicator | shared [Focus Management](../../accessibility/focus-management.md) contract |

Do not create a Textarea-specific Color-token family merely to restate these shared roles.

## Accessibility

Textarea is a Level 2 stateful native-based form component.

### Native primitive

Prefer native HTML `<textarea>` as the baseline implementation primitive.

Do not recreate ordinary multiline text editing with a custom editable widget.

### Accessible name

- Provide a meaningful label or equivalent accessible-name mechanism.
- Placeholder must not be the only accessible name.
- `Show label=False` is a Figma composition capability, not permission to ship an unlabeled textarea.
- Requiredness must be communicated programmatically as well as visually.

### Keyboard and focus

- Preserve native textarea keyboard editing.
- Normal tab order applies.
- Disabled textareas are unavailable to normal interaction/focus.
- Readonly textareas remain focusable.
- Keep Focus visible in Focus, Error focus, and Read only focus.
- Do not remove native focus unless the approved replacement focus treatment is present.

### Helper and Error relationships

The component provides the mechanism for programmatically associating Helper/Error content with the textarea.

When invalid:

- expose invalid state programmatically;
- associate the textual Error;
- keep Focus independently visible.

Validation timing, rule, and exact error copy belong to Product/Form policy.

### Character limits and Count

If Product enforces a real character limit:

- use appropriate native/implementation constraints where they match the product requirement;
- keep the user informed before they reach a hard limit when necessary;
- ensure Count is understandable in context;
- do not rely on visual Count alone if the limit is critical to task completion.

### Zoom, RTL, and long content

Test:

- long Persian labels;
- multiline Persian values;
- mixed Persian/English content;
- 200%+ zoom/text enlargement as applicable;
- long Error/Helper text;
- Count + Helper/Error together;
- Required + Info;
- resized short and tall instances;
- RTL handle placement.

Essential label/error information must remain discoverable even when textarea content scrolls.

## Mechanism vs Product Policy

| Textarea / Design System owns | Product / Form owns |
|---|---|
| Label mechanism | Actual label |
| Required support mechanism | Whether field is required |
| Placeholder / Value presentation | Actual placeholder/value |
| Helper/Error association mechanism | Actual helper/error copy |
| Count presentation | Whether to count, what unit, actual limit |
| Invalid visual/semantic mechanism | Validation rule and timing |
| Disabled / Read only support | Which state applies |
| Resizable visual/authoring contract | Whether resizing is permitted in a specific product context |
| Focus visuals | Form-level failed-submit focus/recovery strategy |

## Development Contract

### Conceptual runtime inputs

The exact Angular/package API is not yet registered as a canonical code source.

Implementation should support concepts equivalent to:

```text
Textarea
- value
- placeholder
- disabled
- readonly
- invalid
- required
- label / accessible-name mechanism
- helper / error description mechanism
- maxLength or equivalent product constraint when applicable
- count metadata when applicable
- resize behavior
- native textarea attributes
```

Do not model Figma-only authoring concepts as runtime API without implementation need:

```text
Filled          → derive from actual value
Hover           → CSS/platform state
Focus           → CSS/platform state
Error focus     → invalid + focus
Read only focus → readonly + focus
Supporting      → composition of helper/error/count presence
```

### Geometry requirements

- default/min Control height → `120px`
- Control padding → `16px`
- radius → `6px`
- Field spacing → `4px`
- optional supporting row → `20px`
- default/hover/focus/read-only line → `1px`
- error line → `2px` overlay
- focus indicator → shared [Focus Management](../../accessibility/focus-management.md) contract
- resize affordance → bottom-left in RTL in Figma, `8px` inset

The exact CSS/Tailwind implementation and whether the runtime uses native browser resize rendering or an approved custom affordance remain Frontend decisions until the code source is registered.

## QA Checklist

Verify representative combinations, not only master variants:

- all 8 State values exist;
- `Supporting=Hidden|Visible` exists;
- Default is `State=Default, Supporting=Hidden`;
- Filled preserves Placeholder and Value independently;
- Resizable hides/shows the affordance without changing geometry;
- non-error Supporting Hidden reserves no supporting row;
- Error and Error focus always retain Error text;
- Helper-only, Count-only, Helper+Count, Error-only, and Error+Count are all authorable;
- Count is left and Helper/Error is right in RTL;
- Disabled supporting content and resize handle use disabled foreground;
- Error border is 2px without layout shift;
- Error focus preserves Error + Focus;
- Read only focus remains visibly focused;
- resize handle is mirrored for bottom-left RTL placement;
- default Control height is 120px;
- outer instance can resize to larger widths/heights;
- on resize, Field/Control grow while Label and Supporting row remain stable;
- Border, Value overlay, shared Focus effect, and resize handle follow resized Control bounds;
- long multiline content remains contained;
- legacy toolbar behavior does not leak into canonical Textarea.

## Product Variation

No product-specific Textarea variant is currently approved.

Product themes resolve the same semantic component contract through active theme mappings.

## Figma Reference

Canonical editable source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Textarea`
- Page node: `5564:279849`
- Documentation frame: `22880:132462`
- Header: `22880:132463`
- Variant matrix: `22880:132470`
- Axes & properties: `22880:132471`
- Canonical component set: `Textarea`
- Component set node: `22800:128313`
- Playground: `22880:132541`
- Examples: `22810:865`

Internal canonical helpers:

- `_Textarea Supporting Row` → `22804:684`
- `_Textarea Error Row` → `22804:690`
- `_Textarea Resize Handle` → `22810:748`

Legacy `Text area`, duplicate Text area sets, `Text area with toolbar`, and scratch assets were removed from the canonical Figma page.

## Code / Storybook Reference

No runtime component package or Storybook source is currently registered as canonical for Textarea.

Do not infer implemented Angular API, class names, native-resize CSS, or Storybook behavior from Figma alone.

## Open Items

- register the canonical runtime/Storybook source when available;
- align the exact Angular/Tailwind public API with Frontend;
- confirm runtime resize policy and native-browser handle behavior;
- validate whether any product requires auto-grow behavior;

These open items do not block the current Textarea visual and authoring contract.

## Related Documents

- `./text-input.md`
- `./rich-text-editor.md`
- `../../accessibility/forms.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/color/semantics.md`
- `../tokens/color/usage.md`
- `../../foundations/visual/radius.md`
