---
id: design-system.component.chip
collection: design-system
type: component
title: Chip
summary: Chip is the interactive compact-control family for direct selection, committed removable values, disclosure controls, and value-level add/start actions.
knowledge_state: verified
document_maturity: reviewed
design_status: ready-for-dev
design_maturity: handoff-ready
last_reviewed: '2026-10-24'
related:
  - design-system.component.tag
  - design-system.component.badge
  - design-system.component.switch
  - design-system.foundation.radius
  - design-system.accessibility.focus-management
  - design-system.reference.component-mapping
---

# Chip

## Purpose

Chip is the compact interactive-control family for value/data interaction.

The public family is split by **interaction capability**, not by product use case:

- **Chip / Selectable** — the value itself is selected or deselected.
- **Chip / Removable** — a committed value/object can be removed; its body may also be independently actionable.
- **Chip / Disclosure** — a compact control opens a secondary surface to choose or edit its state.
- **Chip / Action** — a compact, stateless action starts/adds/configures a value.

A large Chip family is acceptable; a single mega Chip component is not.

Names such as Choice Chip, Filter Chip, Input Chip, and Suggestion Chip are usage patterns, not public component-set names.

## Boundary with Tag

**Tag describes. Chip interacts.**

Tag remains a separate component:

- passive;
- descriptive;
- categorical;
- non-actionable;
- non-selectable;
- may use `tag/{color}/*` because hue carries categorization/grouping meaning.

Chip:

- is interactive;
- uses shared Semantic color tokens;
- does not use Tag color tokens;
- does not introduce Chip-specific color tokens in the current contract.

Example:

- `[Senior]` beside a job title as metadata → Tag.
- `[Senior]` as a selectable/filter value → Chip / Selectable.

## Shared Geometry and Visual Language

All public Chip sets share the same control recipe:

| Property | Contract |
|---|---|
| Extra Small height | `28px` |
| Small height | `32px` |
| Medium height | `40px` |
| Radius | `Radius / Full` — current Chip visual direction |
| Radius status | Temporary/current direction; revisit if the family moves back to the shared control radius |
| Default width | Hug content |
| Label | Single-line |
| Label text style | `Label/XS` (Extra Small); `Label/SM` (Small/Medium) |
| Main content gap | `8px` |
| Secondary content internal gap | `4px` |
| Direction | RTL-first; use logical start/end |
| Focus | Shared [Focus Management](../../accessibility/focus-management.md) treatment |
| Color | Semantic roles only |
| Interaction State | `Default / Hover / Active / Focus / Disabled` |

Persistent meaning (`Selected`, `Applied`), transient interaction (`State`) and popup visibility (`open`) are independent. **Opening does not change Chip surface colors.** For Disclosure, only the Chevron direction changes through an exposed nested `Chevron / Open` control (not a parent Variant axis); for Removable, no separate Figma Open control or visual treatment is needed.

The current family intentionally has no public `Type=Filter/Input/Suggestion` axis and no public `Color` axis.

## Public Figma Model

Canonical file: `[DS] Job Vision NEXT`

### Chip / Selectable

- Component set: `Chip / Selectable`
- Figma node ID: `20783:128158`
- Figma component key: `5571e8e324b47155d7e9fd384aaea289c2e54d89`
- Variant properties:
  - `Size = Extra Small / Small / Medium`
  - `Selected = false / true`
  - `State = Default / Hover / Active / Focus / Disabled`
- Content properties:
  - `Label`
- Variant count: `30 = 3 Size × 2 Selected × 5 State`

Purpose: use when the value itself is directly selected or deselected.

Canonical usages:

- **Choice/data selection** — e.g. employment type: حضوری / دورکاری / ترکیبی.
- **Direct filter** — e.g. `[ دورکاری ] → [ ✓ دورکاری ]`.

The component itself does not know whether it is Choice or Filter; the owning group/pattern gives the selection its product meaning.

#### Selected treatment

`Selected=true` uses a leading check at logical Start plus `surface/accent-muted`, `line/accent`, and `fg/accent`. Hover and Active use the corresponding direct semantic Accent surfaces: `surface/accent-muted-hover` and `surface/accent-muted-active`. Focus preserves the base selected surface and adds the shared visible-Focus treatment. Disabled continues to use the shared disabled treatment.

Rules:

- selected state must remain legible outside Hover/Focus;
- do not communicate selection by color alone;
- `×` is never a selection indicator;
- do not add a leading-icon property until a valid recurring use case requires it.

### Chip / Removable

- Component set: `Chip / Removable`
- Figma node ID: `23124:358`
- Figma component key: `193062043a2194024cc06c6d45f11b96b4a238b3`
- Variant properties:
  - `Size = Extra Small / Small / Medium`
  - `State = Default / Hover / Active / Focus / Disabled`
- Content properties:
  - `Label`
  - `Detail`
  - `Show detail`
  - `Show leading visual`
  - `Leading visual` instance swap
- Variant count: `15 = 3 Size × 5 State`
- Trailing remove affordance: mandatory

Purpose: represent a **committed value/object** that can be removed. Because the value is already committed, Removable uses the same Accent value treatment as other committed/selected Chip states.

Examples:

- `[ ali@email.com × ]`
- `[ Figma × ]`
- `[ Microsoft Word · متوسط × ]`
- `[ English · B2 × ]`

#### Leading visual

The optional leading visual may be an icon or avatar when the value benefits from recognition. Keep this as content composition; do not add an Icon/Avatar variant axis unless geometry later requires it.

#### Detail

`Detail` is compact secondary value information such as skill level or proficiency. The `Detail` property stores the value only, for example `متوسط` or `B2`; it must not include the separator. Visually, Detail is composed inside a `Detail content` container as `Divider (·) + Detail`, with a 4px internal gap. `Show detail` controls the whole container. It is content, not a semantic state.

#### Body action

The body may be independently actionable.

Example:

`[ Microsoft Word · متوسط × ]`

- body activation → edit/inspect/open detail such as Level editing;
- `×` → remove the committed software.

`Body action` is a behavioral capability, not a Variant. **There is no Open authoring property or Open-specific visual style** in Removable: a committed chip looks the same whether a related editor is open or closed. The component now has two structurally independent targets: `Body / action target` and the existing `__Chip Remove Action`, with independent Hover/Active/Focus and remove behavior. Popup visibility belongs to the owning interaction pattern; `aria-expanded` (where needed) belongs to Body only.

Runtime requirements:

- body and Remove are independent hit targets;
- when body is actionable, body and Remove are independent focus targets;
- do not nest one button inside another;
- when body opens a secondary surface, `aria-expanded` is placed on the body trigger, not the Remove action;
- disabled forces effective `open=false` in runtime;
- use an appropriate compound-control DOM structure;
- body action may be edit, inspect, disclosure, or another value-level interaction; do not rename the capability to Disclosure.

### Chip / Disclosure

- Component set: `Chip / Disclosure`
- Figma node ID: `20783:534`
- Figma component key: `3ba6c8dc36a76632d1569108e024ae47c841a50c`
- Variant properties:
  - `Size = Extra Small / Small / Medium`
  - `Applied = false / true`
  - `State = Default / Hover / Active / Focus / Disabled`
- Exposed nested instance: `Chevron / Open = false / true` (glyph direction; **not** a parent Variant axis)
- Content properties:
  - `Label`
  - `Summary`
  - `Show summary`
- Variant count: `30 = 3 Size × 2 Applied × 5 State`
- Trailing chevron: mandatory; down (Closed) / up (Open)

Purpose: use for compact facets/controls that open a secondary surface such as Popover or Menu to choose or edit state.

Examples:

- `[ صنعت ▾ ] → [ صنعت · ۳ ▾ ]`
- `[ مدیر ▾ ] → [ مدیر: هلن ▾ ]`

#### Applied versus Open

`Applied` and `Open` are independent concepts:

- `Applied` = the control currently has a committed/applied value;
- `Open` = the owning secondary surface is currently visible.

**Current Figma treatment (2026-10-17, updated after benchmark review):** The Chip's surface styling is entirely driven by `Applied × State`, never by Open. An exposed nested Chevron helper has an `Open=false/true` option: `Icon/chevron_down` when closed, `Icon/chevron_up` when expanded. Its semantic color follows the **actual State**: `__Chip Chevron / Neutral` uses `fg/secondary` when unapplied and enabled; `__Chip Chevron / Accent` uses `fg/accent` when applied and enabled; `__Chip Chevron / Disabled` uses `fg/disabled` in **both Applied conditions and both icon directions**. Always match the adjacent Label foreground token, not just Applied. This nested property is exposed to the consuming Figma instance. In runtime `open` is owned by the popup/pattern, controls Chevron orientation and `aria-expanded`, and is forced false when disabled; opening must not add a persistent Active background or Focus ring.

#### Summary

Summary is optional compact applied-state information.

Examples:

- selected count value: `۳`;
- selected value: `هلن`.

The separator is structural rather than part of the `Summary` string. Visually, Summary is composed inside a `Summary content` container as `Divider (·) + Summary`, with a 4px internal gap.

Rules:

- `Summary` is supplemental content, not another state axis;
- `Show summary` is available on applied instances and controls the whole `Summary content` container;
- keep Summary compact and store only the value, without a leading `·` or `|`;
- Single/Multiple selection is not a Chip property; the owning Popover/Menu/selection surface owns that behavior.

The trailing chevron remains the disclosure affordance after a value is applied. Do not replace it with `×`; clearing belongs to the owning surface unless a separate product pattern is approved.

### Chip / Action

- Component set: `Chip / Action`
- Figma node ID: `23123:125056`
- Figma component key: `876535cdb18030fe2d38c6c6221036d770838586`
- Variant properties:
  - `Size = Extra Small / Small / Medium`
  - `State = Default / Hover / Active / Focus / Disabled`
- Content properties:
  - `Label`
  - `Show trailing icon`
  - `Trailing icon` instance swap
- Variant count: `15 = 3 Size × 5 State`

Purpose: a compact, stateless value-level action.

Canonical example:

`[ Microsoft Word + ]`

Activation may open a Level surface. Only after the required value is committed does the representation become:

`[ Microsoft Word · متوسط × ]`

That lifecycle is:

`Chip / Action → configure/commit → Chip / Removable`

Action has no `Selected`, `Applied`, or `Removable` state.

Generic task actions such as “Summarize”, “Generate questions”, or “Edit” remain Button / Tertiary rather than becoming Chip merely because they are compact.

## Usage Mapping

| Product/use-case concept | Canonical primitive |
|---|---|
| Choice / short compact data selection | Chip / Selectable |
| Direct filter | Chip / Selectable |
| Faceted filter / opens Popover or Menu | Chip / Disclosure |
| Committed input/value/object | Chip / Removable |
| Available value / add-start action | Chip / Action |
| Contextual suggestion | Chip / Action only when it is genuinely a value-level compact action |
| Generic task/utility action | Button / Tertiary |
| Passive category/metadata | Tag |

## Visual Grammar

Use the affordances consistently:

- `✓` = selected; place it at logical Start before the label;
- `▾` / `▴` = secondary surface closed/open;
- `×` = remove committed value;
- `+` = add/start/configure a value.

Do not swap these affordances based on superficial visual similarity.

## Group and Pattern Architecture

Do not build one mega `Chip Group` with SelectionMode, RemoveMode, ActionMode, FilterMode, DisclosureMode, and other orthogonal behavior switches.

Collection behavior belongs to composition/pattern-level contracts.

### Choice Group

Uses `Chip / Selectable` for short, compact choices.

Potential group behavior:

- `Selection = Single / Multiple`;
- empty/required policy is separate from Selection mode;
- horizontal/wrap as the common layout;
- vertical only when a real product need exists;
- individual Chips hug content by default.

`Single` does not imply `Required`.

### Filter Pattern

May combine:

- `Chip / Selectable` for direct filters;
- `Chip / Disclosure` for faceted filters.

Example:

`[ ✓ دورکاری ] [ صنعت · ۲ ▾ ] [ مدیر ▾ ]`

They share one visual language but retain distinct interaction contracts.

### Tokenized Input / Selected Values

Uses `Chip / Removable`.

Examples:

`[ Ali × ] [ Sara × ] [ input… ]`

or

`[ Word · متوسط × ] [ Excel · پیشرفته × ]`

The owning input/picker controls creation, validation, keyboard navigation, ordering, and collection behavior.

## Software Lifecycle

The software use case intentionally crosses two Chip capabilities.

Before commit:

`[ Microsoft Word + ]` → Chip / Action

Activation opens the Level configuration surface.

Only after the required Level is chosen and committed:

`[ Microsoft Word · متوسط × ]` → Chip / Removable (same appearance while editing surface is shown)

Then:

- body may reopen Level editing; there is no special Open style on the Removable Chip;
- `×` removes the committed software independently of the Open state.

Whether the committed item stays in the same location or moves from Available to Selected is a **product-level collection decision**, not part of the Chip component contract.

The Figma Chip documentation includes a real `Chip / Disclosure` + existing Popover composition example for the Industry filter to make the component/surface boundary explicit.

### Figma token-compliance audit — 2026-10-20

The **four current public Chip component sets** have been audited separately from Playground, helper sources and legacy Open=True variants. Current Size, State, Selected/Applied, interaction API and **Radius / Full** decisions remain unchanged.

- All 90 public source variants (30 Selectable, 15 Removable, 30 Disclosure, 15 Action) now use governed Spacing, Typography, Radius and public Semantic Color bindings at their owned source layers.
- In **Chip / Removable**, 45 previously raw but scale-correct properties on the 15 `Body / Edit action target` frames are now bound to shared Spacing variables: 15 each of `paddingRight` (8/12/16 by Size), `paddingLeft` (8px), and `itemSpacing` (8px). The independent Remove target was not changed.
- Exactly **nine** disabled root fills (Selected Selectable, Removable, Applied Disclosure × three Sizes) were bound to the current **surface/disabled** role instead of the retired `surface/surface-selected-disabled` alias. This is an intentional appearance refinement, especially for Dark. The legacy variable remains intact for other consumers.
- Source QA: **315/315 effective Spacing** property bindings, **180/180 Text Styles**, **90/90 Radius/Full** source radii and **378/378 solid visible public Semantic paints**. Heights remain 28/32/40px by Size; no set identities or variant axes were regenerated.

Scope and risk: the old `__Legacy Chip Open=True variants` collection was **not** migrated or deleted; existing Figma references must be handled through a separate compatibility review. QA in both Products × Light/Dark, keyboard interaction and consumer published overrides remains required before runtime certification.

See Chip Token Compliance Audit for node IDs, migration counts and remaining acceptance checks.
## State and Token Contract

Color is a semantic state mapping, not a public Chip axis.

Current mappings:

- default structured base: `surface/default + line/default + fg/primary`;
- default-base hover: `surface/default` base + `surface/transparent-hover` overlay;
- default-base active: `surface/default` base + `surface/transparent-active` overlay;
- Selectable selected default/focus: `surface/accent-muted + line/accent + fg/accent`;
- Selectable selected hover: `surface/accent-muted-hover + line/accent + fg/accent`;
- Selectable selected active: `surface/accent-muted-active + line/accent + fg/accent`;
- Disclosure applied default/focus: `surface/accent-muted + line/accent + fg/accent`;
- Disclosure applied hover: `surface/accent-muted-hover + line/accent + fg/accent`;
- Disclosure applied active: `surface/accent-muted-active + line/accent + fg/accent`;
- Removable default/focus: `surface/accent-muted + line/accent + fg/accent`;
- Removable hover: `surface/accent-muted-hover + line/accent + fg/accent`;
- Removable active: `surface/accent-muted-active + line/accent + fg/accent`;
- disabled: shared disabled foreground/line/surface treatment;
- focus: preserve the underlying persistent state and add the shared focus effect.

Structured Chip colors must stay in their semantic family: default/unselected/unapplied and Action use `surface/default` with transparent Hover/Active overlay; Selected Selectable and Applied Disclosure use their direct semantic state tokens. Removable has a stable committed Accent base, while Hover/Active feedback is applied to **Body only**, leaving the separate Remove control unchanged. **Open never alters a Chip surface color or Focus ring.**

Do not:

- create `chip/*` color tokens;
- borrow `tag/{color}/*`;
- use Brand color without a semantic role;
- use Magic except for explicitly AI-specific cases.

## Focus

All public Chip sets use the shared [Focus Management](../../accessibility/focus-management.md) treatment.

Rules:

- visible Focus follows the shared [Focus Management](../../accessibility/focus-management.md) behavior;
- use the outside ring/effect, not border thickening;
- preserve the underlying Selected/Applied treatment;
- parent containers must not clip the ring;
- pointer activation alone need not force keyboard-style focus when the platform's focus-visible algorithm does not require it.

For compound Removable Chips, Body and Remove have separate focus targets. The Figma Body and Remove action retain independent shared Focus treatments; neither is a permanent indicator of popup visibility.

## Content, Long Labels, and Layout

Chips are single-line compact controls.

Rules:

- keep labels short and scannable;
- do not introduce a multiline Chip variant;
- Figma instances hug content;
- constrained runtime labels truncate rather than wrap;
- the parent owns available width and wrapping;
- wrap whole Chips at the collection level;
- do not equalize Chip widths by default.

Exact runtime maximum width and truncation measurement remain unverified until the runtime source is registered.

## RTL

Do not create separate RTL variants.

Use logical anatomy:

- content ordering follows RTL reading direction;
- Selectable check is logical Start, before the label;
- Action add/action icon sits at logical End (visually left in RTL);
- Removable leading visual/icon is logical start;
- trailing Disclosure chevron is logical end;
- trailing Remove is logical end;
- Chip groups follow product RTL ordering;
- directional icons follow their own shared icon mirroring contract.

The canonical Playground includes RTL examples.

## Choice vs Other Selection Controls

Selectable Chip does not replace Radio, Checkbox, SelectBox, Segmented Control, or Toggle Button.

### Radio / Radio Group

Use for explicit classic single-selection form controls.

### Checkbox / Checkbox Group

Use for explicit classic multiple-selection form controls.

### Chip / Selectable + Choice Group

Use for compact selection with short labels that benefits from horizontal/wrapped standalone choices.

### SelectBox / SelectBox Group

Use for richer/full-width choices, long labels, descriptions, or survey/onboarding options that need more room.

### Segmented Control

Use for exactly-one connected view/mode switching such as Day / Week / Month or List / Grid.

### Toggle Button

Use for persistent tool state such as Bold / Italic / Pin.

Selectable Chip is for value/data/filter selection and does not need to be connected.

## Accessibility Contract

All public Chip sets must be keyboard operable and expose meaningful accessible names.

Shared requirements:

- Disabled controls do not perform actions;
- state is not communicated only by color;
- Focus uses the shared focus-visible treatment;
- RTL visual order must not break logical keyboard/reading order.

### Selectable

Runtime must expose selected state semantically. Do not infer a specific DOM role or `aria-pressed` solely from the Figma `Selected` property.

### Removable

Remove has its own accessible name, e.g. “Remove Microsoft Word”.

If the body is actionable, body and Remove are separate operable/focusable targets with a valid compound-control DOM structure.

### Disclosure

Runtime must expose that the control owns/opens a secondary surface and expose open/closed state using appropriate platform semantics.

Focus transfer, dismissal, keyboard navigation, and selection behavior belong to the owning Popover/Menu/selection pattern.

### Action

Expose the value-level action in the accessible name, e.g. “Add Microsoft Word”, rather than relying on the `+` icon alone.

Exact DOM/ARIA choices remain unverified until the runtime implementation is registered.

## Figma Authoring Rules

- Choose the Component Set by interaction capability, not product wording.
- Keep `Selected` / `Applied` separate from `State`.
- Do not add product-use-case variants.
- Do not add Open to the parent Chip State/Variant axes. Disclosure exposes a nested Chevron direction property only; Removable, Selectable and Action have no Open visual property.
- Do not add Single/Multiple to Disclosure; it belongs to the secondary surface.
- Use the existing icon library; do not draw ad hoc Chip icons.
- Override shared icon foreground where the consuming Chip state requires it.
- Keep Divider structural: Summary/Detail properties store value only; do not prefix their values with `·` or `|`.
- Use the shared 8px spacing variable for the main Chip content gap and 4px inside `Summary content` / `Detail content` between Divider and the value.
- Use semantic State tokens as shown in the canonical Figma components. In Removable, apply transient Hover/Active/Focus to Body independently of Remove. Do not style Open as Active.
- Use the shared `Radius / Full` variable for the current Chip direction; do not use a literal radius. This is a current family decision rather than a global control-radius change.
- Do not create `_Chip Base` until repeated maintenance evidence proves a shared private primitive is useful.
- Do not create new work from legacy Carbon-derived Chip or old Chip Group artifacts.

## Canonical Figma Page

- Figma file key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Chip`, node `13500:300199`
- Documentation frame: `Chip / Documentation · canonical sources`, node `23900:128061`
- Sections:
  1. Component Set
  2. Playground
  3. Usage & composition
  4. Usage & handoff

Playground coverage includes:

- employment-type Choice and direct Remote filter;
- Industry and Manager Disclosure filters;
- Email recipient;
- Software + Level;
- Add Software with `+`;
- Focus/Disabled states;
- long-label behavior;
- real Disclosure + existing Popover composition for Industry.

## Legacy and Migration

Published identities were preserved where safe.

Identity-preserving migration:

- old Toggle identity/key → `Chip / Selectable`;
- old Trigger identity/key → `Chip / Disclosure`;
- On 2026-10-17, the initial Open background treatment was rejected after benchmark review. The canonical Disclosure retains the original 30 closed-variant component IDs, with nested Chevron direction instead; Removable retains the original 15 component IDs and two independent target areas. The 45 old Open=True source components were retained in a separate __Legacy frame for compatibility rather than deleted;
- `Chip / Removable` and `Chip / Action` are new canonical capability sets.

Older Carbon-derived Chip artifacts and old Chip Group components remain reference-only where deleting them could break existing consumers.

Do not use them for new design.

There is no public `_Chip Base`.

## Runtime Boundary

The owning JV Design System runtime repository/package and verified Storybook source are not registered in Design System Knowledge.

Therefore these remain explicitly unverified:

- exact runtime component/API names;
- exact props/inputs/outputs;
- exact DOM roles/elements and ARIA attributes;
- compound Removable DOM implementation;
- Disclosure popup ownership and focus-transfer implementation;
- exact selected-state runtime semantics;
- exact truncation/max-width algorithm;
- exact framework/Tailwind classes;
- Storybook story/docs identifiers;
- Figma-property → code-prop mapping;
- Code Connect mapping.

Do not infer them from Figma property names.

## Current simplified Open-state contract — 2026-10-17

The canonical Figma library now contains **30 Selectable, 15 Removable, 30 Disclosure and 15 Action** public variants (**90 total**) plus **15 internal Remove** variants. `Open` is not a parent Variant axis in either set: Disclosure exposes only nested Chevron orientation, and Removable has no Open visual treatment. The original 45 closed component IDs were preserved and the 45 historical Open=True components remain available in an __Legacy frame so prior linked instances are not deleted. New designs should not use the legacy sources. Final simplification audit supersedes the earlier 150-variant audit.

## QA Checklist

Verify:

- four public sets exist: Selectable / Removable / Disclosure / Action;
- no `Type=Filter/Input/Suggestion` mega set exists;
- Figma variant counts are Selectable 30, Removable 15, Disclosure 30, Action 15, internal Remove 15;
- Extra Small = 28px; Small = 32px; Medium = 40px;
- radius is the shared Full variable for the current Chip direction;
- State is Default / Hover / Active / Focus / Disabled;
- Selectable has persistent Selected and uses a leading ✓ at logical Start, never ×;
- Removable always has ×, optional Detail / leading visual, independent Body/Remove visual feedback, and no Figma Open property;
- Removable body-action capability does not create invalid nested-button semantics;
- Disclosure has persistent Applied, optional Summary, and mandatory chevron;
- Disclosure exposes a nested Chevron/ Open false/true control that changes only the icon orientation; runtime owns independent expanded state. Removable has no visual Open property;
- Disclosure Chevron icon foreground must match the Label token for each State: `fg/secondary`, `fg/accent`, or `fg/disabled`; verify **both Chevron directions** and both Applied values. Disabled icon colors are bound to semantic variables, never hard-coded.
- Action is stateless and can express `+` add/start with the optional trailing icon after the label;
- focus uses the shared outside ring;
- semantic colors are used; Tag/Chip-specific colors are not;
- labels remain one line;
- RTL anatomy is correct;
- parent collections can wrap whole Chips;
- Playground covers Choice, direct filter, faceted filter, committed values, software lifecycle, long label, focus/disabled, and Disclosure + Popover;
- legacy components are clearly reference-only;
- runtime semantics are re-verified when the owning implementation source is registered.

## Live References

- Selectable node/key: `20783:128158` / `5571e8e324b47155d7e9fd384aaea289c2e54d89`
- Removable node/key: `23124:358` / `193062043a2194024cc06c6d45f11b96b4a238b3`
- Disclosure node/key: `20783:534` / `3ba6c8dc36a76632d1569108e024ae47c841a50c`
- Action node/key: `23123:125056` / `876535cdb18030fe2d38c6c6221036d770838586`
- Runtime code: unregistered
- Storybook: unregistered
