---
id: design-system.component.text-input
collection: design-system
type: component
title: Text Input
summary: Text Input captures a single-line text value through a native-input-oriented, RTL-first field contract with shared label, supporting text, validation, and adornment behavior.
knowledge_state: verified
document_maturity: draft
related:
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Text Input

## Purpose

Text Input captures or displays a single-line text value.

Use the canonical Text Input instead of creating ad-hoc label, input, helper, validation, or icon arrangements. The component owns the reusable field mechanism and visual contract; the consuming Product or Pattern owns the actual field meaning, validation rule, copy, and input-purpose metadata.

Text Input is based on the behavior of a native HTML `<input>`. Figma represents the states designers need to specify, but the implementation should preserve native text editing, selection, browser shortcuts, autofill, paste, and input semantics.

## When to Use

Use Text Input for a single-line value such as:

- name;
- email;
- phone number;
- job title;
- search/query text when no Search-specific behavior is required;
- short identifiers or other single-line free text.

## When Not to Use

Do not use Text Input when:

- the value is expected to span multiple lines → use Textarea;
- the user chooses from a defined option set → use Select, Radio, Checkbox, or another selection control;
- the control has specialized behavior that materially changes its interaction contract → use or define the specialized component rather than overloading Text Input;
- the content is immutable and does not need input semantics → prefer ordinary readable content unless readonly form semantics are necessary.

Password Input may share this field/control architecture, but its reveal/hide action and authentication-specific behavior remain a separate component contract.

## Canonical Figma API

Component set: `Text Input`

Figma node: `22780:548` in `-DS--Job-Vision-NEXT`.

### Top-level properties

| Property | Values / behavior |
|---|---|
| `Size` | `Small`, `Medium`, `Large`; `Medium` is default |
| `State` | `Default`, `Hover`, `Focus`, `Error`, `Error focus`, `Disabled`, `Read only`, `Read only focus` |
| `Filled` | Boolean Figma-authoring switch; `False` shows Placeholder, `True` shows Value |
| `Placeholder` | Placeholder copy, preserved independently from Value |
| `Value` | Entered/displayed value, preserved independently from Placeholder |
| `Show label` | Shows/hides the visible label row |
| `Show helper` | Shows/hides helper content in non-error states |
| `Show leading icon` | Optional leading adornment |
| `Leading icon` | Instance swap; leading is on the right in RTL |
| `Show trailing icon` | Optional trailing adornment/action affordance |
| `Trailing icon` | Instance swap; default icon is Close; trailing is on the left in RTL |

### Contextual nested properties

`Field label` exposes:

- `Label`
- `Required`
- `Show info`

Supporting content is contextual:

- non-error states → `Helper > Text`
- Error / Error focus → `Error > Text`

### Filled is Figma-only authoring state

`Filled` exists to make design authoring fast and preserve both placeholder and value copy.

```text
Filled = False
→ Placeholder visible
→ Value retained but not displayed

Filled = True
→ Value visible
→ Placeholder retained but not displayed
```

`Filled`:

- is not a visual filled-background style;
- is not a runtime interaction state;
- should not become a required public code prop.

Runtime display should normally derive from the actual `value` and `placeholder` supplied to the native input.

## Anatomy

```text
Text Input
├── Field label
│   ├── Label
│   ├── Required marker
│   └── Optional info affordance
├── Control
│   ├── Leading adornment
│   ├── Content
│   │   ├── Placeholder
│   │   └── Value
│   └── Trailing adornment
└── Supporting content
    ├── Helper
    └── Error
```

The field label and supporting-content patterns are intended to be shared with related form controls such as Password Input and Textarea. That shared family architecture must not require designers to manually assemble a Field shell and a Control for normal use; public components should remain directly insertable.

## Sizes and Geometry

| Size | Control height | Inline padding |
|---|---:|---:|
| Small | 32 px | 12 px |
| Medium | 40 px | 16 px |
| Large | 48 px | 16 px |

Shared geometry:

- Medium is the default size.
- Border radius: `6px` / Control radius.
- Leading/trailing icon visual size: `16px`.
- Gap between icon and content: `8px`.
- Gap between Field label, Control, and Supporting content: `4px`.
- Border is implemented visually without changing content padding.
- The content area is single-line. In Figma, Placeholder and Value fill the available Content width and use ending ellipsis for overflow; the control must not grow vertically. Runtime native inputs may use their platform-native horizontal scrolling/editing behavior rather than reproducing ellipsis while editing.
- Width is flexible; resizing the component must preserve inline padding, icon gap, border geometry, and RTL order.

### Size scope

Text Input supports `Small / Medium / Large` only.

The shared control-size foundation also contains `Extra Small = 28px` for components such as Button, but Text Input does not expose Extra Small until a real input use case justifies the additional density.

## RTL and Directionality

Text Input is RTL-first for the current JobVision/Cando context.

In RTL:

```text
right edge
→ Leading
→ Content
→ Trailing
→ left edge
```

Rules:

- Leading is positioned on the right.
- Trailing is positioned on the left.
- Label, Placeholder, Value, Helper, and Error text are right-aligned in the default RTL presentation.
- Field-label visual order is `Label → Required → Info` when read from the RTL starting edge.
- Medium/Large keep 16 px from the outer control edge to an enabled icon slot; Small keeps 12 px.
- Mixed Persian/English values must remain readable and must not change the semantic meaning of Leading/Trailing.
- Directional icons must follow the icon system's mirroring rules; non-directional icons such as Search or Close do not mirror merely because the interface is RTL.

## State Model

Figma intentionally flattens the states designers need to specify into one `State` property. Runtime implementation does not need to expose the same state names as application props.

### Default

- surface → `surface/default`
- line → `line/default`
- Value → `fg/primary`
- Placeholder → `fg/placeholder`
- Label → `fg/secondary`
- Helper → `fg/secondary`
- Leading adornment → `fg/tertiary`
- Trailing affordance → `fg/secondary`

### Hover

- line → `line/emphasis`
- geometry and content positions do not change.

Hover is a platform/CSS interaction state, not normally a runtime component prop.

### Focus

Focus composes two independent visual layers:

```text
Control border → line/emphasis, 1px
Focus indicator → focus/default, 2px ring + 1px offset
```

The focus indicator must not change input height, content padding, or layout.

### Error

Error communicates validation failure through more than color:

```text
Error border → line/error, 2px
Error message → fg/error
Programmatic invalid state → required in implementation
```

The 2 px Error border is an overlay and must not change the component's dimensions or padding.

Error text is required for the canonical Error state; a red border alone is insufficient.

### Error focus

Error and Focus remain independently visible:

```text
Error border → line/error, 2px
Focus indicator → focus/default, 2px ring + 1px offset
Error message → fg/error
```

Do not replace Error meaning with Focus color or remove visible keyboard focus because the field is invalid.

### Disabled

Disabled represents an unavailable form control.

```text
surface → surface/disabled
line → line/disabled
content → fg/disabled
adornments → fg/disabled
```

Implementation should preserve native disabled semantics when the field is genuinely unavailable. Disabled is not a substitute for Read only.

### Read only

Read only represents a value that remains readable and semantically part of the form but cannot be edited.

Current visual treatment:

```text
surface → surface/default
line → line/muted
content → normal readable foreground
```

Read only remains distinct from Disabled.

A native readonly input remains focusable, so Figma also provides `Read only focus`.

### Read only focus

Read only focus preserves the Read only treatment and adds the shared `focus/default` 2px ring with a 1px offset.

## Label, Required, and Info

- A meaningful accessible name is always required.
- The visible Label is the normal accessible-name source.
- Placeholder must not be the only label.
- `Show label=False` is an authoring capability for compositions where another valid accessible-name mechanism exists; it does not permit an unlabeled runtime input.
- `Required` controls the visual required marker in Figma.
- Requiredness must also be communicated programmatically in implementation.
- Do not rely on the asterisk or color alone when users could misunderstand whether fields are required or optional.
- The optional Info affordance is for concise supplementary information. Instructions required to complete the field should not be hidden only behind Info.

## Placeholder and Value

Placeholder provides an example, hint, or expected format; it is not a replacement for the field label.

Use Placeholder sparingly when it adds information not already clear from the Label.

Value represents the actual input content.

Figma preserves Placeholder and Value independently so designers can toggle `Filled` without rewriting content.

Runtime implementation should preserve native input/value behavior, including:

- selection;
- cursor movement;
- copy/paste;
- autofill;
- browser and assistive-technology text editing conventions.

## Helper and Error Content

Helper content provides non-critical context or instructions.

Error content identifies a validation problem and should explain what is wrong and, when known, how to correct it.

Rules:

- Helper and Error occupy the supporting-content region below the Control.
- Error replaces the ordinary helper treatment while invalid.
- Error must be textually available; do not communicate invalid state through border color alone.
- Implementation must programmatically associate applicable helper/error text with the input.
- Validation timing, the validation rule, and exact error copy belong to Product/Form policy rather than Text Input itself.

## Leading and Trailing Adornments

### Leading

Leading is normally a contextual/decorative adornment and uses `fg/tertiary`.

Examples include a Search icon when the input is being used as a simple query field.

When the visible label/value already conveys meaning, decorative icons should not create duplicate accessible names.

### Trailing

Trailing uses `fg/secondary` by default. The default Figma swap is Close.

Text Input only owns the visual slot. If Trailing becomes an interactive action, such as:

- Clear value;
- Reveal password;
- Open a specialized picker;

the specialized component or consuming implementation must define its action semantics, focusability, hit target, accessible name, and keyboard behavior.

Do not assume an arbitrary trailing glyph inside a native `<input>` is automatically an accessible action.

## Behavior

- Preserve native single-line input editing behavior.
- Do not introduce a component-specific Active/Pressed state.
- Do not use Skeleton as a Text Input state; loading placeholders belong to the relevant loading/content pattern.
- Do not add Warning until a validated JobVision/Cando use case requires a distinct Warning semantic contract.
- Interaction states must not change control dimensions, padding, gap, or label layout.
- Long content must not cause the single-line control to grow vertically.
- Autofill is a runtime/browser scenario, not a Figma component state.
- Empty / has-value are content conditions; Figma's `Filled` switch exists only for authoring convenience.

## Semantic Color Mapping

Text Input consumes shared Semantic roles and does not require an `input/*` Color-token family.

| Part / state | Semantic role |
|---|---|
| Label | `fg/secondary` |
| Value | `fg/primary` |
| Placeholder | `fg/placeholder` |
| Helper | `fg/secondary` |
| Error content | `fg/error` |
| Leading adornment | `fg/tertiary` |
| Trailing affordance | `fg/secondary` |
| Default surface | `surface/default` |
| Default line | `line/default` |
| Hover / Focus line | `line/emphasis` |
| Error line | `line/error` |
| Disabled surface | `surface/disabled` |
| Disabled line | `line/disabled` |
| Disabled content | `fg/disabled` |
| Read-only line | `line/muted` |
| Focus indicator | `focus/default` |

Do not create `fg/helper`, `read-only/*`, input-specific focus tokens, or Text-Input-owned Color tokens solely to restate these roles.

## Accessibility

Text Input is a Level 2 stateful native-based component.

### Semantics and accessible name

- Prefer native `<input>`.
- Associate the input with a meaningful label/accessibile-name mechanism.
- Placeholder must not be the only accessible name.
- Pass through the correct input type and input-purpose/autocomplete metadata supplied by Product.
- Preserve native `required`, `invalid`, `readonly`, and `disabled` semantics as applicable.

### Keyboard and focus

- Preserve native text-input keyboard editing and browser shortcuts.
- Normal tab order applies.
- Disabled native inputs are unavailable to normal focus/interaction.
- Readonly native inputs remain focusable; retain visible focus.
- Do not remove native focus without the approved replacement focus treatment.

### Error and description relationships

The component provides the mechanism for programmatically associating Helper/Error content with the input.

When invalid:

- expose invalid state programmatically;
- expose the textual error relationship;
- keep Focus visible independently from Error.

Product/Form policy decides the validation rule, timing, and exact message.

### Visual accessibility

Error uses:

```text
line/error
+ textual Error content
+ programmatic invalid state
```

not color alone.

Focus uses the shared `focus/default` contract and remains visible in Error and Read only states.

### RTL, zoom, and content

Test:

- long Persian labels;
- mixed Persian/English input values;
- 200%+ zoom / text enlargement as applicable;
- long Placeholder and Value content;
- Label + Required + Info;
- Leading and Trailing combinations;
- RTL icon placement and directional mirroring.

Essential label/error information must remain discoverable even when the input value itself is clipped as a single line.

### Component accessibility tests

- Native input can be reached and edited with keyboard in editable states.
- Focus is visible in Focus, Error focus, and Read only focus.
- Accessible name remains present when the visual label is omitted in a supported composition.
- Required, readonly, disabled, and invalid semantics match the visual state.
- Helper/Error relationships are exposed programmatically.
- Error is not communicated by border color alone.
- Paste/autofill/browser text editing remain available unless a product-specific justified constraint exists.
- RTL and mixed-direction values remain usable.
- Long content and zoom do not remove essential information.

## Mechanism vs Product Policy

| Text Input / Design System owns | Product / Form owns |
|---|---|
| Label mechanism | Actual label |
| Required visual/programmatic support mechanism | Whether the field is required |
| Placeholder / Value presentation | Actual placeholder/value |
| Helper/Error association mechanism | Actual helper/error copy |
| Invalid visual and semantic mechanism | Validation rule and validation timing |
| Disabled / Read only support | Which state applies |
| Input-purpose/autocomplete pass-through | Correct input purpose/autocomplete value |
| Leading/Trailing visual slots | Whether a specialized trailing action is needed |
| Focus visuals | Form-level failed-submit focus/recovery strategy |

## Development Contract

### Native primitive

Use a native HTML `<input>` as the baseline primitive.

Do not recreate ordinary text editing with a custom widget.

### Conceptual runtime inputs

The exact Angular/package API is not yet registered as a canonical code source. Implementation should support concepts equivalent to:

```text
TextInput
- size: sm | md | lg
- value
- placeholder
- disabled
- readonly
- invalid
- required
- label / accessible-name mechanism
- helper / error description mechanism
- leading adornment?
- trailing adornment/action?
- native input attributes / autocomplete / type pass-through
```

Do not model Figma-only authoring concepts as runtime API without implementation need:

```text
Filled      → derive from actual value
Hover       → CSS/platform state
Focus       → CSS/platform state
Error focus → composition of invalid + focus
Read only focus → composition of readonly + focus
```

### Geometry requirements

- `sm` → 32 px control height, 12 px inline padding
- `md` → 40 px control height, 16 px inline padding
- `lg` → 48 px control height, 16 px inline padding
- radius → 6 px
- adornment size → 16 px
- adornment/content gap → 8 px
- default/hover/focus/read-only line → 1 px
- error line → 2 px overlay with no layout shift
- focus indicator → 2px ring + 1px offset with no layout shift

The exact CSS/Tailwind class architecture remains a Frontend implementation decision.

## QA Checklist

Verify representative combinations rather than only isolated master variants:

- Small / Medium / Large preserve exact height and inline padding.
- Medium remains the default.
- Placeholder and Value are independently editable.
- Toggling `Filled` never destroys either Placeholder or Value copy.
- `Filled` does not change component dimensions.
- Leading is right and Trailing is left in RTL.
- Medium/Large icon edge distance remains 16 px; Small remains 12 px.
- Icon/content gap remains 8 px.
- Leading uses `fg/tertiary`; Trailing uses `fg/secondary`; Disabled uses `fg/disabled`.
- Default trailing swap is Close.
- Icon swap preserves semantic component color.
- Label visual order in RTL is Label → Required → Info.
- Error border is 2 px without padding/layout shift.
- Error focus preserves both Error and Focus.
- Read only focus is available and visibly focused.
- Helper expands field height without changing Control height.
- In Figma, long Placeholder and Value content remain single-line, fill the available Content width, and truncate with ending ellipsis. Runtime editing may preserve native horizontal scrolling behavior.
- Horizontal resize preserves border stretch, inline padding, RTL order, and content clipping.
- Existing instance overrides survive component migration.

## Product Variation

No product-specific Text Input variant is currently approved.

Product themes resolve the same semantic component contract through the active theme mappings.

## Figma Reference

Canonical editable source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Text Input`
- Page node: `395:4`
- Documentation frame: `22884:401`
- Header: `22884:402`
- Variant matrix: `22884:409`
- Axes & properties: `22884:410`
- Component set: `Text Input`
- Component set node: `22780:548`
- Internal Field Label: `22766:61`
- Internal Field Helper: `22785:585`
- Internal Field Error: `22785:587`
- Playground: `22884:126397`
- Examples: `22780:127670`

Legacy Outline/Fill sets, the obsolete shared Supporting/Content drafts, and scratch instances were removed from the canonical Figma page.

## Code / Storybook Reference

No runtime component package or Storybook source is currently registered as canonical for Text Input.

Do not infer implemented Angular API, CSS class names, or Storybook behavior from Figma alone.

## Open Items

These items remain intentionally open while the form-field family is stress-tested:

- register the canonical runtime/Storybook source when available;
- align exact Angular/Tailwind public API with Frontend;
- confirm whether any real product use case requires Extra Small input density;
- confirm whether any real product use case requires Warning as a first-class validation tone.

These open items do not block the current Text Input visual and authoring contract.

## Related Documents

- `../../accessibility/forms.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../../foundations/visual/radius.md`
