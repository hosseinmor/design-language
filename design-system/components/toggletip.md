---
id: design-system.component.toggletip
collection: design-system
type: component
title: Toggletip
summary: Toggletip reveals supplemental contextual explanation when the user explicitly asks for more information.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.component.tooltip
  - design-system.component.popover
  - design-system.experience-rule.contextual-guidance
---

# Toggletip

## Purpose

Toggletip provides contextual explanation that the user explicitly requests.

It is appropriate when the interface needs a small help/info affordance that works with click, tap, and keyboard activation rather than relying on hover discovery.

Toggletip is primarily a learn-more surface, not a task surface.

## When to Use

Use Toggletip when:

- a user intentionally activates an info/help trigger to understand a nearby concept;
- the explanation may be longer than a Tooltip;
- the content must work on touch devices;
- the content may include one simple learn-more link/action;
- the information is contextual but does not need to remain persistently visible.

Typical triggers include an info icon, help icon, or another explicit contextual-help control.

## When Not to Use

Do not use Toggletip when:

- a short passive label on hover/focus is sufficient; use Tooltip;
- the user must complete a small task, change settings, fill fields, or interact with several controls; use Popover;
- the product proactively introduces a feature without the user asking for help; use Coachmark;
- the guidance spans multiple ordered steps; use Tour;
- the information is essential to task completion and should remain visible persistently.

If the content grows into a mini application surface, it is no longer a Toggletip.

## Canonical Figma API

Component set: `Toggletip / Default`

Figma file key: `rROD8ctH9UfPGAMrRrOzHe`

Component set node: `22778:127362`

Component key: `54bf6a92136594a94c18def1a16c5378786884cf`

### Properties

| Property | Values / behavior |
|---|---|
| `Title` | Boolean; default `False` |
| `Action` | Boolean; default `False` |
| `Title text` | Text |
| `Body text` | Text |
| `Action text` | Text |
| `Side` | `Top`, `Bottom`, `Left`, `Right` |
| `Align` | `Start`, `Center`, `End` |

Default variant: `Top / Start` with `Title=False` and `Action=False`.

There is intentionally no `Visible`, `Open`, `State`, `Shadow`, `Type`, or `Arrow` property in the canonical Figma API.

The caret is part of canonical Toggletip anatomy and is always shown.

Runtime open/close state, outside dismissal, focus behavior, collision, and portal behavior are code-owned.

## Anatomy

Toggletip contains:

1. floating raised surface;
2. optional Title;
3. required Body;
4. optional simple Action;
5. directional caret.

The optional Action is intended for a single lightweight learn-more destination.

Do not add checkboxes, inputs, multiple Buttons, selectors, or other task controls to Toggletip.

## Visual Contract

- Background: `surface/raised`
- Title/body foreground: `fg/primary`
- Action foreground: `fg/accent`
- Title typography: `Heading/Compact/SM` — 14/18
- Body typography: `Body/Compact/SM` — 14/20
- Action typography: `Label/SM` — 14/20
- Padding: 16px
- Internal gap: 8px
- Radius: 12px
- Explicit border: none
- Floating separation: `Shadow/Floating` (1px outline-like layer + two elevation layers)
- Maximum surface width: 320px
- Caret wrapper: 44×7px
- Caret outer boundary layer: 14×7px using the Floating boundary color
- Caret inner raised-surface layer: 12×6px using `surface/raised`

Toggletip uses the same raised floating-surface language as Popover and Coachmark.

It does not use the inverse Tooltip surface.

## Placement and RTL

Toggletip supports four sides and three alignments.

RTL is canonical.

For `Top` and `Bottom`:

- `Start` = right;
- `Center` = center;
- `End` = left.

For `Left` and `Right`:

- `Start` = top;
- `Center` = center;
- `End` = bottom.

Title, Body, and Action align to the right.

The caret follows the verified shared two-layer floating-caret geometry. The outer layer continues the Floating boundary around the arrow while the inner layer matches `surface/raised` without adding an explicit stroke to the triangle:

- Top: surface then caret; caret rotation 0;
- Bottom: caret then surface; caret rotation 180;
- Left: surface then caret; caret rotation 90;
- Right: caret then surface; caret rotation -90.

Runtime collision/flip must preserve logical Start/End semantics.

Toggletip uses a 2px anchor offset measured from the caret tip to the trigger edge.

## Behavior

### Trigger

Toggletip is opened by explicit user activation:

- click;
- tap;
- `Enter`;
- `Space`.

Do not use hover as the only trigger.

### Dismissal

Toggletip should dismiss through:

- activating the trigger again when toggle behavior is used;
- outside interaction where appropriate;
- `Escape`.

Exact focus movement and return remain runtime-owned, but keyboard users must be able to reach any interactive Action that is present.

## Content Guidelines

Body copy may be longer than Tooltip copy, but should remain focused on one nearby concept.

Use Title when the explanation benefits from a short heading.

Use the Action only for a single lightweight learn-more destination.

Suitable Action labels include:

```text
بیشتر بدانید
مشاهده راهنما
درباره این قابلیت
```

Do not use Toggletip as a container for Save/Confirm/Apply workflows.

## Accessibility

### Trigger

The trigger should normally be a native Button or Icon Button with a meaningful accessible name.

When the popup state is programmatically relevant, expose the trigger/content relationship and expanded state using the appropriate platform semantics.

### Content

- Body text must be readable by assistive technology.
- If Action is visible, it must be keyboard reachable.
- `Escape` must close the Toggletip.
- Closing must not leave focus lost or stranded.
- Toggletip must not trap focus.

Toggletip is preferable to Tooltip when the information must be explicitly discoverable on touch.

## Touch / Mobile

Toggletip supports tap activation.

Do not invent long-press interaction to imitate desktop Tooltip behavior.

When the content grows too large for a small anchored surface on narrow screens, move to a larger responsive disclosure pattern instead of compressing the Toggletip beyond readability.

## Development Contract

Runtime source is currently unregistered.

Conceptual API:

```text
Toggletip
- title?
- body
- action?
- side
- align
- trigger relationship
```

Runtime owns:

- open/closed state;
- activation;
- outside dismissal;
- Escape;
- focus handling;
- collision/flip;
- portal/layering;
- RTL logical placement.

Do not expose collision outcomes or open state as Figma variants.

## QA Checklist

Verify:

- all 12 Side × Align combinations;
- caret direction and attachment;
- Start/End semantics in RTL;
- anchored examples preserve the 2px caret-tip-to-trigger offset;
- Title true/false;
- Action true/false;
- Title/Body/Action remain right-aligned;
- width does not exceed 320px;
- `surface/raised`, radius 12, and the canonical three-layer `Shadow/Floating` are used;
- no additional explicit component border is present;
- the shared caret shows the same boundary treatment as the floating Surface without a seam;
- click/tap/keyboard activation works in runtime;
- Action is keyboard reachable when visible;
- Escape dismisses the Toggletip;
- content does not grow into a multi-control task surface.

## Live References

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Toggletip / Default`
- Node: `22778:127362`
- Component key: `54bf6a92136594a94c18def1a16c5378786884cf`
- Matrix: 4 Sides × 3 Alignments = 12 variants
- Shared raised caret component: `__Floating caret / Raised`, node `22780:128095`
- Runtime / Storybook / Code Connect: unregistered / unverified

## Related

- `tooltip.md`
- `popover.md`
- `coachmark.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../accessibility/core.md`
- `../../accessibility/focus-management.md`
