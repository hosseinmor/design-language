---
id: design-system.component.rich-text-editor
collection: design-system
type: component
title: Rich Text Editor
summary: Rich Text Editor captures formatted multiline content through the shared Field contract and an internal formatting toolbar.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.textarea
- design-system.component.icon-button
- design-system.component.toggle-button
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: draft
design_maturity: usable-for-product-testing
---

# Rich Text Editor

## Purpose

Rich Text Editor captures multiline content that requires inline or paragraph-level formatting.

It is a separate public component from Textarea. Use Textarea when plain multiline text is sufficient. Rich Text Editor owns a formatting toolbar and richer editing semantics that require a dedicated editor implementation.

Both components share the same Field contract for Label, Required, Info, supporting content, validation, RTL treatment, semantic colors, resizing, and focus/error composition.

## Canonical Figma Contract

Component set: `Rich Text Editor`

Figma node: `22866:134455` in `-DS--Job-Vision-NEXT`.

### Variant axes

| Property | Values |
|---|---|
| `State` | `Default`, `Hover`, `Focus`, `Error`, `Error focus`, `Disabled` |
| `Toolbar` | `Compact`, `Expanded` |
| `Supporting` | `Hidden`, `Visible` |

Default: `State=Default, Toolbar=Compact, Supporting=Hidden`.

The public matrix contains 24 variants.

### Top-level authoring properties

| Property | Behavior |
|---|---|
| `Show label` | Shows/hides the shared Field label row |
| `Filled` | Figma-only content condition; False shows Placeholder, True shows Value |
| `Placeholder` | Placeholder copy |
| `Value` | Plain sample value used for Figma authoring |
| `Resizable` | Shows/hides the shared resize handle |

`Filled` is an authoring convenience in Figma, not a runtime interaction state or required code prop.

`Value` is only a visual representation of editor content in Figma. It does not define the runtime rich-text data model, HTML, JSON, Markdown, marks, links, or document schema.

### Contextual nested properties

`Field label` exposes the shared:

- `Label`
- `Required`
- `Show info`

Supporting content follows the Textarea pattern:

- non-error + `Supporting=Hidden` → the shared Supporting instance remains in the anatomy but is hidden;
- non-error + `Supporting=Visible` → Helper/Count row is visible;
- `Error` and `Error focus` → Error content is always retained; Count may also be shown.

Keeping the same nested Supporting instance across variants is required so helper/count overrides survive variant switching.

## Anatomy

```text
Rich Text Editor
├── Field
│   ├── Field label
│   └── Editor
│       ├── Rich Text Toolbar
│       ├── Divider
│       ├── Editable area
│       │   ├── Placeholder
│       │   ├── Value overlay
│       │   └── Resize handle
│       └── Border
└── Supporting content
    ├── Helper / Count
    └── Error / Count
```

Focus and validation styling belong to the complete Editor shell, not only the editable area. In Figma, Focus is applied to the Editor shell with the shared `Focus/Default` Effect Style rather than a separate Focus-ring layer.

## Geometry

Default width: `288px`.

This intentionally matches the canonical Textarea baseline instead of introducing a wider Rich Text-only default.

Shared editor geometry:

- radius → `6px`
- editable-area padding → `16px`
- editable-area typography → shared Textarea body style, currently Vazirmatn Regular `14/20`
- toolbar/body divider → `1px`
- editable-area minimum height → `120px`
- Toolbar owns the top `6px` corner radii and clips its own content; Editable area owns the bottom `6px` corner radii and clips body content. The outer Field/Editor must not clip the outside Focus effect.
- In Figma, the Filled Value layer starts at the same `16px` inset as Placeholder. A fixed `20px` surface overlay covers the one-line Placeholder while the Value text itself may grow to multiple lines; this keeps the top inset stable during horizontal and vertical resizing.

### Compact toolbar

```text
40 toolbar
+ 1 divider
+ 120 editable area
= 161px Editor shell
```

With visible Label and no visible supporting row, the outer field height is `185px`.

### Expanded toolbar

```text
81 toolbar
+ 1 divider
+ 120 editable area
= 202px Editor shell
```

With visible Label and no visible supporting row, the outer field height is `226px`.

A visible supporting row adds `20px` to the outer geometry.

### Resizing

The Figma instance may be resized horizontally and vertically.

On vertical growth:

- Label height remains fixed;
- Toolbar height remains fixed;
- Supporting height remains fixed;
- Editable area absorbs the additional height.

On horizontal growth:

- Toolbar stretches;
- Editable area stretches;
- Value overlay stays inset by the 16px body padding;
- Supporting content stretches;
- Border and focus indicator stretch.

Real-instance QA has been run at `480px` width and increased vertical height.

## State Model

### Default

- Editor surface → `surface/default`
- line → `line/default`, 1px
- Value → `fg/primary`
- Placeholder → `fg/placeholder`

### Hover

- line → `line/emphasis`, 1px

### Focus

```text
Editor line → line/emphasis, 1px
Focus indicator → focus/default, 2px ring + 1px offset
```

### Error

```text
Editor line → line/error, 2px
Error message → fg/error
Programmatic invalid state → required in implementation
```

The 2px Error line is overlay geometry and must not shift content.

### Error focus

Error meaning and keyboard focus remain independently visible:

```text
Editor line → line/error, 2px
Focus indicator → focus/default, 2px ring + 1px offset
Error message → fg/error
```

### Disabled

Disabled applies to the complete field:

- Editor surface → `surface/disabled`
- line → `line/disabled`
- Value / Placeholder → `fg/disabled`
- Label / Supporting / resize handle → disabled foreground treatment
- Toolbar controls → disabled
- Toolbar dividers → `line/disabled`

## Internal Rich Text Toolbar

Canonical internal component set: `_Rich Text Toolbar`

Figma node: `22865:3861`.

The toolbar is intentionally internal. It is part of the Rich Text Editor contract, not a general-purpose standalone Toolbar component.

### Toolbar axes

| Property | Values |
|---|---|
| `Layout` | `Compact`, `Expanded` |
| `State` | `Enabled`, `Disabled` |

The toolbar has four variants.

### Compact

Compact is one `40px` row and is designed to fit the canonical `288px` editor width.

RTL visual order from the starting edge:

```text
Character formatting
→ Lists
→ Link
→ Overflow
```

Controls:

- Bold
- Italic
- Underline
- Strikethrough
- Bulleted list
- Numbered list
- Link
- Overflow

### Expanded

Expanded adds a second `40px` row separated by a `1px` divider.

The second row contains:

- Align right
- Align center
- Align left
- Align justify
- RTL text direction
- LTR text direction
- Undo
- Redo

Expanded toolbar height: `81px`.

The RTL-first default presentation shows Align right and RTL direction as selected.

## Formatting Selection vs Interaction

Persistent formatting selection must not use Icon Button `Active`.

Icon Button `Active` is a transient interaction state. Rich-text formatting such as Bold, list type, alignment, and text direction is persistent selection/current-value state.

The internal component `_Rich Text Toolbar Toggle` owns this distinction **temporarily**. It is a Rich Text-specific stopgap until the shared Toggle Button / Icon Toggle Button component is designed.

Figma node: `22864:3503`.

### Toggle axes

| Property | Values |
|---|---|
| `Selected` | `False`, `True` |
| `State` | `Enabled`, `Hover`, `Active`, `Focus`, `Disabled` |

Selected treatment uses the existing selection surface tokens. Interaction states remain independent.

Examples:

- Bold selected when the caret/selection is in bold text;
- Bulleted list selected when the current block uses that list type;
- Align right selected for the current paragraph;
- RTL selected for the current paragraph/selection.

Do not create toolbar-level variants for combinations of formatting values.

Undo, Redo, and Overflow remain normal action Icon Buttons rather than selected toggles.

## Icons

Rich-text formatting icons are canonical general-DS icons on the `Icons` page, not private 16px assets owned by Rich Text Editor.

They follow the existing `24×24` icon component convention and are consumed through Icon Button / Toolbar Toggle icon slots.

Old local 16px draft icon assets were removed from the canonical Figma page. Use the general Design System icon components instead.

## Intentionally Excluded from Shared v1

The old CanDo toolbar included controls that are not part of the shared v1 contract:

- Add Token / Parameter;
- Font family;
- raw pixel Font size.

Add Token is product-specific behavior.

Font family should not bypass the product typography/theme contract.

Raw Font size should not be exposed until a shared semantic rich-text typography model exists, for example Paragraph / Heading styles.

Indentation may be added later if a real shared product requirement is validated.

## RTL

The component is RTL-first for current JobVision / CanDo products.

Toolbar group order is anchored to the RTL starting edge. Text direction is a content-formatting action; it does not flip the Design System component layout itself.

Mixed-direction content must not change the structural meaning or placement of toolbar groups.

## Behavior Boundary

The Design System owns:

- Editor shell anatomy;
- shared Field integration;
- toolbar grouping and visual hierarchy;
- persistent selected vs transient interaction semantics;
- focus/error/disabled visuals;
- default/minimum geometry and resizing;
- semantic token usage;
- formatting-action affordances.

The consuming editor implementation owns or must define:

- editor framework;
- runtime rich-text document model;
- selection and caret behavior;
- command execution;
- keyboard shortcuts;
- paste/sanitization behavior;
- output/serialization format;
- undo/redo history semantics;
- link editing UI/behavior;
- semantic paragraph/heading model if introduced.

Do not infer a specific runtime editor framework from Figma.

## Accessibility

Rich Text Editor is not a native Textarea and requires an explicit implementation contract.

### Editable region

Implementation must preserve:

- accessible labeling;
- keyboard text editing;
- selection/caret access;
- screen-reader-compatible editing semantics;
- invalid/disabled relationships as applicable.

### Toolbar

Every toolbar control requires:

- an accessible name independent of its icon;
- keyboard operability;
- exposed pressed/selected state for persistent formatting toggles;
- visible focus;
- predictable focus movement;
- selection preservation when a toolbar action is executed.

Undo/Redo and other unavailable actions must expose disabled state when applicable.

### Focus

Visible focus must remain clear for both:

- the Editor/editable region;
- an individual toolbar control during keyboard navigation.

Editor-shell focus does not replace button-level focus.

### Error

Error requires:

- textual Error content;
- programmatic invalid state or equivalent editor semantics;
- visible Error styling;
- independent visible Focus when focused.

## QA Checklist

Verify:

- exactly 24 public variants exist;
- default is Default / Compact / Hidden;
- public authoring properties are Show label / Filled / Placeholder / Value / Resizable;
- default width is 288px;
- editable-area minimum height is 120px;
- body padding is 16px;
- Compact toolbar is 40px and fits 288px;
- Expanded toolbar is 81px;
- Filled preserves Placeholder and Value independently;
- Compact ↔ Expanded preserves Value and supporting overrides;
- Supporting Hidden ↔ Visible preserves Helper / Count overrides;
- Error always retains textual Error content;
- Error focus preserves Error + Focus simultaneously;
- Disabled applies to editor, toolbar, label, supporting content, and resize handle;
- persistent formatting uses Selected semantics, not Icon Button Active;
- horizontal resizing stretches toolbar/body/support/border/focus;
- Toolbar/background content never bleeds outside the 6px editor corners;
- Error border always covers the complete Editor shell height;
- The Focus effect remains visible outside the Editor shell and is not clipped by Field/Editor containers;
- Filled Value and Placeholder remain anchored at the 16px top inset during multiline content growth and resizing;
- vertical resizing grows only the editable area;
- Resizable controls only resize-handle visibility;
- hiding the visual label requires another accessible-name mechanism in implementation;
- RTL toolbar order remains correct.

## Figma Reference

Canonical source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Rich Text Editor`
- Page node: `22875:6289`
- Documentation frame: `22877:133693`
- Header: `22877:133694`
- Variant matrix: `22877:133701`
- Axes & properties: `22877:133702`
- Rich Text Editor set: `22866:134455`
- Internal Toolbar set: `22865:3861`
- Internal Toolbar Toggle set: `22864:3503`
- Playground: `22878:10007`
- Examples: `22868:133907`

Obsolete Rich Text / Textarea toolbar drafts were removed from the canonical target file after migration. The canonical nodes listed above are the only Figma source of truth for this component family.

## Runtime / Storybook Status

No runtime editor package or Storybook implementation is currently registered as canonical for Rich Text Editor.

Do not infer:

- Angular API;
- DOM/contenteditable structure;
- editor framework;
- serialization format;
- command API;
- keyboard-shortcut implementation.

## Open Items

Before the runtime contract is finalized:

- select/register the canonical editor implementation;
- define the rich-text value/output model;
- define toolbar keyboard navigation and selection-preservation behavior;
- define Link editing behavior;
- define semantic Paragraph/Heading styles before adding typography controls;
- decide whether indentation is shared;
- define paste/sanitization rules;
- define a first-class Read only contract if a real product use case requires it;
- replace the temporary `_Rich Text Toolbar Toggle` with the shared Icon Toggle Button after the Toggle Button component is designed (TBD);
- register Storybook and browser accessibility tests.

Read only is intentionally not a Figma state yet because Rich Text Editor needs an explicit behavior decision for the toolbar and editable region rather than inheriting Textarea semantics blindly.

The current visual/Figma-authoring contract is usable for product testing, but these unresolved runtime/editor behaviors keep the component at `draft` rather than `handoff-ready`.

## Related Documents

- `./textarea.md`
- `./text-input.md`
- `./icon-button.md`
- `./toggle-button.md`
- `../../accessibility/forms.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/color/semantics.md`
- `../tokens/color/usage.md`
