---
id: design-system.component.popover
collection: design-system
type: component
title: Popover
summary: Popover is a generic floating surface for a small contextual task or interaction.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.component.toggletip
  - design-system.component.coachmark
  - design-system.experience-rule.contextual-guidance
---

# Popover

## Purpose

Popover is a generic floating container for a small contextual task or interaction anchored to another UI element.

Popover owns the floating shell, placement, elevation, caret, and composition boundary. The consuming feature owns the task-specific content placed inside it.

## When to Use

Use Popover when the user intentionally opens a small contextual surface to perform work without leaving the current context.

Examples include:

- a compact filter;
- a small settings form;
- a contextual action group that is not semantically a Menu;
- a short selector or task-specific control cluster;
- a small edit/configuration surface.

## When Not to Use

Do not use Popover when:

- the content is only a brief passive label; use Tooltip;
- the user only needs a contextual explanation or learn-more disclosure; use Toggletip;
- the product is proactively introducing a feature; use Coachmark;
- the interaction is a semantic Menu, Select, Date Picker, or another dedicated component with stronger behavior semantics;
- the task is large enough to require a Dialog, Drawer, full page, or another larger surface.

Do not use Popover merely because content visually fits inside a floating rectangle.

## Canonical Figma API

Component set: `Popover / Default`

Figma file key: `rROD8ctH9UfPGAMrRrOzHe`

Component set node: `22790:127700`

Component key: `4e88b783a0b479a8bb90e8771604a04fd39785ba`

### Properties

| Property | Values / behavior |
|---|---|
| `Content` | Native Figma Slot for arbitrary composition |
| `Arrow` | Boolean; default `False` |
| `Side` | `Top`, `Bottom`, `Left`, `Right` |
| `Align` | `Start`, `Center`, `End` |

Default variant: `Top / Start` with `Arrow=False`.

There is intentionally no `Visible`, `Open`, `Shadow`, or runtime collision property in the Figma API.

## Default Content

Popover's `Content` Slot is not empty by default.

It contains the recommended `Popover content` component so ordinary Popovers begin with a consistent anatomy while still allowing complete replacement for specialized cases.

### Popover content

Component set: `Popover content`

Node: `22794:128045`

Component key: `302481b4cf7da6fe1d450f281752fe1e7a9b28ec`

Properties:

| Property | Values / behavior |
|---|---|
| `Title` | Boolean |
| `Body` | Boolean |
| `Title text` | Text |
| `Body text` | Text |
| `Actions` | `None`, `One`, `Two` |

Component default: Title + Body + `Actions=None`.

Inside `Popover / Default`, the recommended embedded `Popover content` preset is intentionally configured with `Actions=Two`. This shell preset does not change the standalone `Popover content` component default.

The action buttons are real instances of the canonical Button component and are exposed nested instances for further configuration.

Use the default content anatomy for ordinary explanatory/task Popovers. Replace the entire Slot when the content is structurally different, such as a filter group, action list, or small form.

Do not add more and more booleans to `Popover content` to simulate every possible task layout.

## Anatomy

Popover contains:

1. floating `Surface`;
2. `Content` Slot;
3. optional caret.

The default Slot content contains:

1. optional Title;
2. optional Body;
3. optional one- or two-action row.

## Visual Contract

Popover shell:

- Background: `surface/raised`
- Foreground: content-owned; normal text starts from `fg/primary`
- Radius: 12px
- Padding: 16px
- Explicit border: none
- Floating separation: `Shadow/Floating` (1px outline-like layer + two elevation layers)
- Surface minimum width: 240px
- Surface maximum width: 360px
- Content Slot minimum width: 208px
- Content Slot maximum width: 328px

`Shadow/Floating` intentionally includes the subtle 1px outline-like first layer used by the floating family. Do not add a second explicit border to Popover by default.

When `Arrow=True`, the shared raised caret uses a two-layer construction so the Floating boundary visually continues around the arrow without a seam.

## Placement and RTL

Popover supports four sides and three alignments.

RTL is canonical.

For `Top` and `Bottom`:

- `Start` = right;
- `Center` = center;
- `End` = left.

For `Left` and `Right`:

- `Start` = top;
- `Center` = center;
- `End` = bottom.

The Content Slot aligns children to the right by default.

Runtime collision/flip must preserve logical Start/End semantics.

Popover uses a 2px anchor offset:
- when `Arrow=False`, measure from the Surface edge to the trigger edge;
- when `Arrow=True`, measure from the caret tip to the trigger edge.

## Arrow

`Arrow=False` is the default.

Use `Arrow=True` only when the anchored relationship would otherwise be ambiguous or when the consuming pattern intentionally needs stronger visual pointing.

For ordinary task-oriented Popovers, proximity and placement should normally establish the relationship without a caret.

Do not create separate arrow/no-arrow component sets.

## Behavior

Popover is opened by explicit user activation such as click, tap, `Enter`, or `Space` on an appropriate trigger.

Popover is not hover-triggered as its primary interaction.

Expected dismissal behavior includes:

- activating the trigger again when the product pattern supports toggle behavior;
- clicking/tapping outside when appropriate;
- pressing `Escape`;
- completing an action that intentionally closes the Popover.

Exact focus movement and return depend on the content/task and remain part of the runtime/pattern contract.

Popover is non-modal by default and must not trap focus merely because it is floating.

## Content and Composition

### Default content

The standalone `Popover content` component defaults to Title + Body with `Actions=None`.

The canonical `Popover / Default` shell is prepopulated with that component configured as `Actions=Two` so the common two-action anatomy is immediately available in the shell preset.

Consumers may choose `None`, `One`, or `Two` according to the task. Keep action groups to two Buttons whenever possible.

In RTL:

- Primary action is on the right;
- Secondary/low-emphasis action is to its left.

Button hierarchy follows the shared Action Hierarchy contract.

### Slot replacement

Replace the entire Content Slot when the content has a materially different information architecture.

Suitable specialized slot content may include:

- compact filters;
- small form controls;
- task-specific option groups;
- short action collections.

If the content has dedicated semantics such as Menu, Select, or Date Picker, prefer that component rather than rebuilding its behavior inside generic Popover.

## Accessibility

### MUST

- The trigger must be keyboard operable.
- Popup state/relationship must be exposed programmatically where applicable.
- `Escape` must close the Popover.
- Focus must not be lost when the Popover closes.
- Interactive content inside the Popover must follow normal keyboard order.
- Non-modal Popover must not trap focus.
- Visual placement must not be the only indication of the trigger relationship when assistive technology needs an explicit relationship.

### Focus

Focus strategy depends on the task:

- a simple popup may retain focus on the trigger until the user moves into content;
- a form-like or task surface may move focus into the Popover;
- closing should restore focus to a sensible element, normally the trigger when it remains available.

Exact implementation remains runtime-owned.

## Touch / Mobile

Popover may be opened by tap.

On narrow screens, if the content cannot remain usable within the Popover's width and viewport constraints, switch to an appropriate larger responsive pattern rather than shrinking controls below their usability contract.

## Development Contract

Runtime source is currently unregistered.

Conceptual API:

```text
Popover
- content
- side
- align
- arrow
- trigger relationship
```

Runtime owns:

- open/closed state;
- click/tap/keyboard activation;
- outside dismissal;
- Escape;
- focus management;
- collision/flip;
- portal/layering;
- RTL logical placement.

Do not expose runtime collision results as design variants.

## QA Checklist

Verify:

- all 12 Side × Align combinations;
- caret direction for all four sides;
- Start/End mapping in RTL;
- anchored examples preserve the 2px offset from Surface when `Arrow=False` and caret tip when `Arrow=True`;
- Arrow true/false;
- `surface/raised`, radius 12, and the canonical three-layer `Shadow/Floating`;
- no additional explicit component border;
- Arrow uses the shared two-layer raised caret and preserves the floating boundary without a seam;
- Surface remains within 240–360px;
- Slot remains within 208–328px;
- default `Popover content` is present and editable;
- default shell is `Side=Top`, `Align=Start`, `Arrow=False`;
- standalone `Popover content` defaults to Title + Body with `Actions=None`;
- the embedded `Popover / Default` shell preset uses `Actions=Two`;
- Title, Body, and Actions properties work;
- one- and two-action layouts do not overflow;
- custom Slot compositions resize the shell correctly;
- Escape and keyboard interaction work in runtime;
- focus does not become trapped in non-modal use.

## Live References

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Popover component set: `Popover / Default`
- Popover node: `22790:127700`
- Popover component key: `4e88b783a0b479a8bb90e8771604a04fd39785ba`
- Default content component set: `Popover content`
- Default content node: `22794:128045`
- Default content component key: `302481b4cf7da6fe1d450f281752fe1e7a9b28ec`
- Runtime / Storybook / Code Connect: unregistered / unverified

## Related

- `tooltip.md`
- `toggletip.md`
- `coachmark.md`
- `button.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../foundations/interaction/action-hierarchy.md`
