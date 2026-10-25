---
id: design-system.component.tooltip
collection: design-system
type: component
title: Tooltip
summary: Tooltip provides brief, passive, non-interactive supplementary information on hover or keyboard focus.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.component.icon-button
  - design-system.component.toggletip
  - design-system.experience-rule.contextual-guidance
---

# Tooltip

## Purpose

Tooltip provides short, supplementary information about a control or UI element.

Tooltip is passive. It appears as a consequence of pointer hover or keyboard focus and must not require an explicit click to reveal ordinary help.

Use Tooltip for information that is useful but nonessential to completing the task.

## When to Use

Use Tooltip when:

- an icon-only control needs a visible label;
- a compact control benefits from a short clarification;
- the information is supplementary and can remain unavailable on touch-only discovery;
- the content can be understood without actions, links, fields, or other interactive elements.

Every operable Icon Button must provide a visible Tooltip label.

## When Not to Use

Do not use Tooltip when:

- the information is essential to completing the task;
- the user must click or tap to intentionally reveal more information; use Toggletip;
- the content contains actions, links, fields, selectors, or other interactive controls; use Toggletip for a simple learn-more action or Popover for richer interaction;
- the product is proactively introducing a feature; use Coachmark;
- the guidance spans multiple ordered steps; use the Tour pattern;
- the experience depends on touch users discovering hover-only content.

Tooltip must not be used as a hidden replacement for persistent instructions, validation, error messaging, or state.

## Canonical Figma API

Component set: `Tooltip / Default`

Figma file key: `rROD8ctH9UfPGAMrRrOzHe`

Component set node: `22773:127299`

Component key: `e29f8f48a0b3ec52f9490d4a9c101df5fba9d769`

### Properties

| Property | Values / behavior |
|---|---|
| `Text` | Tooltip copy |
| `Side` | `Top`, `Bottom`, `Left`, `Right` |
| `Align` | `Start`, `Center`, `End` |

Default variant: `Top / Start`.

There is intentionally no `Visible`, `Open`, `State`, `Shadow`, or runtime collision property in the Figma API.

Runtime state plumbing, collision, flip, portal behavior, and timer implementation remain code-owned. The user-visible timing and dismissal behavior below are canonical Design Language requirements.

## Anatomy

Tooltip contains:

1. one inverse surface;
2. one text label.

Canonical Tooltip has **no caret / arrow**.

Tooltip has no interactive content and must not contain nested controls.

## Visual Contract

- Background: `surface/inverse`
- Foreground: `fg/on-inverse`
- Typography: `Body/Compact/SM` — 14/20
- Vertical padding: 8px
- Horizontal padding: 12px
- Radius: 6px
- Border: none
- Shadow: none
- Arrow / caret: none
- Maximum surface width: 288px
- Maximum text width at the current padding: 264px

Tooltip uses a high-contrast inverse surface because it is transient and should separate clearly from the underlying interface without introducing elevation.

Do not add `Shadow/Floating` or a border to the canonical Tooltip.

## Placement and RTL

Tooltip runtime placement supports four sides and three alignments.

The current Figma component still preserves the `Side` and `Align` matrix for placement authoring/runtime mapping, but those variants no longer change Tooltip anatomy because the caret has been removed.

RTL is canonical.

For `Top` and `Bottom`:

- `Start` = right;
- `Center` = center;
- `End` = left.

For `Left` and `Right`:

- `Start` = top;
- `Center` = center;
- `End` = bottom.

Text is right-aligned in the current RTL products.

Runtime collision and automatic side flipping must preserve the logical meaning of Start/End rather than hard-coding physical left/right assumptions.

Tooltip uses a 2px anchor offset. Because Tooltip has no arrow, measure this from the Tooltip Surface edge to the trigger edge.

## Behavior

### Trigger

Tooltip is revealed by:

- pointer hover;
- keyboard-origin focus, using `focus-visible` or an equivalent input-modality signal.

Tooltip is not click-triggered.

Pointer activation that merely causes the trigger to receive focus must not independently open or reopen Tooltip through the focus path. The focus trigger is for keyboard-origin focus, not pointer-induced focus.

### Timing

Canonical timing:

| Event | Behavior |
|---|---|
| Pointer enters trigger | Show after **300ms** |
| Keyboard-origin focus reaches trigger | Show after **300ms** |
| Pointer leaves both trigger and Tooltip | Close after **100ms** |
| Keyboard focus leaves trigger | Close immediately |
| `Escape` while shown | Close immediately |
| Trigger activation | Close immediately |

The 100ms pointer close delay is a grace interval for ordinary pointer movement. It does not permit Tooltip to linger after keyboard focus has moved or after explicit dismissal/activation.

Do not add a separate Figma delay/state axis. Runtime owns timer mechanics while preserving these values.

### Dismissal and reopen suppression

Tooltip dismisses when:

- pointer leaves the combined trigger + Tooltip hover region for 100ms;
- keyboard focus moves away from the trigger;
- the user presses `Escape` while Tooltip is shown;
- the trigger is activated.

After explicit dismissal by `Escape`, do not automatically reopen Tooltip while the same hover/focus condition remains active.

Reopening requires the relevant condition to reset:

- pointer: leave, then re-enter the trigger;
- keyboard: move focus away, then return with keyboard-origin focus.

After trigger activation, do not reopen Tooltip merely because the trigger retains pointer-induced focus.

When another Tooltip in the same interaction context opens, the previously visible Tooltip should close so competing Tooltip labels are not shown simultaneously.

### Hoverability and persistence

Hover/focus-triggered supplemental content must satisfy the shared accessibility requirement for dismissible, hoverable, and persistent content where applicable.

The rendered Tooltip surface must participate in pointer hit-testing when that is necessary to preserve hover. Do **not** use `pointer-events: none` on the Tooltip surface if doing so causes the Tooltip to close while the pointer moves from the trigger onto the Tooltip.

Runtime may satisfy the transition between trigger and Tooltip through direct hover retention, a hover bridge / safe-polygon strategy, or equivalent hit-area handling. The implementation technique is code-owned; the behavioral requirement is that a user can move the pointer onto the Tooltip without it disappearing prematurely, and the canonical close grace is 100ms after leaving both regions.

This hoverability requirement does not make Tooltip content interactive or keyboard-focusable.

## Content Guidelines

Tooltip copy should be brief and direct.

For Icon Button, default Tooltip text should match the control's accessible action name.

Good:

```text
ویرایش
حذف
بستن
مشاهده جزئیات
```

Avoid:

- paragraphs;
- headings;
- multi-step instructions;
- marketing copy;
- feature announcements;
- controls or actions.

Multiline text is allowed when a concise label cannot reasonably fit on one line, but Tooltip should not become a small article.

## Accessibility

### MUST

- Tooltip must not replace the trigger's programmatic accessible name.
- Tooltip content must not become a keyboard focus target.
- Tooltip must be available on keyboard focus when it is available on hover.
- `Escape` must dismiss it when shown.
- Tooltip must not contain essential task information that is unavailable elsewhere.
- Tooltip must not be the only way touch users can discover required information.

### Icon Button dependency

Every operable Icon Button must provide a visible Tooltip label.

Tooltip improves visible discoverability for Icon Button but does not provide Button semantics or accessible naming.

Disabled Icon Buttons are not required to expose Tooltip. A disabled control must not become focusable solely so Tooltip can appear.

If the reason for disabled state matters to task completion, expose that reason through persistent UI or another appropriate feedback pattern.

### Assistive-technology relationship

When Tooltip text simply repeats the trigger's accessible name, implementation must avoid creating a redundant duplicate announcement.

If Tooltip carries a short supplementary description rather than the visible action label, runtime may expose an appropriate programmatic description relationship when verified.

The exact ARIA wiring remains runtime-owned until Karbon behavior is registered and tested. Do not make Tooltip the source of the trigger's accessible name.

## Touch / Mobile

Tooltip has no canonical touch activation.

Do not use tap or long-press merely to reproduce desktop Tooltip behavior.

When the user must be able to intentionally request the information on touch, use Toggletip instead.

Touch users must not lose essential instructions, state, or task-critical information because Tooltip is unavailable.

## Motion

Use shared overlay motion when a runtime implementation provides one.

Do not animate dimensions or move the trigger.

Reduced-motion preferences must be respected.

Exact duration/easing remain runtime-owned until the implementation source is registered.

## Development Contract

Runtime source is currently unregistered, so exact package/component/prop names are not authoritative yet.

The conceptual implementation must support:

```text
Tooltip
- text / content
- side
- align
- trigger relationship
```

Do not model hover/focus visibility, collision results, or automatic flip as application-facing Figma variants.

Runtime must handle:

- use the canonical 2px Surface-to-trigger anchor offset;
- 300ms show delay for pointer hover;
- 300ms show delay for keyboard-origin focus;
- 100ms pointer close grace after leaving both trigger and Tooltip;
- immediate close on keyboard blur;
- immediate close on `Escape`;
- immediate close on trigger activation;
- suppression of automatic reopen until the relevant hover/focus condition resets after `Escape`;
- no focus-triggered reopen caused only by pointer-induced focus after activation;
- hover persistence across trigger ↔ Tooltip movement;
- only one visible Tooltip within the same interaction context;
- collision/flip;
- portal/layering;
- accessibility relationship without duplicate naming;
- RTL logical Start/End;
- no Tooltip-specific tap/long-press contract.

## QA Checklist

Verify:

- text is readable and right-aligned in RTL;
- Tooltip renders without a caret in every Side × Align combination;
- Surface-to-trigger spacing remains 2px in every placement;
- Top/Bottom Start maps to the right in RTL;
- Top/Bottom End maps to the left in RTL;
- Left/Right Start maps to top;
- Left/Right End maps to bottom;
- max width and wrapping do not exceed the contract;
- anchored examples preserve the 2px Surface-to-trigger offset;
- Tooltip has no border or shadow;
- pointer hover reveals Tooltip after 300ms;
- keyboard-origin focus reveals Tooltip after 300ms;
- pointer-induced focus from click does not independently open/reopen Tooltip;
- moving the pointer from the trigger onto the Tooltip does not cause premature dismissal;
- leaving both trigger and Tooltip closes after 100ms;
- keyboard blur closes immediately;
- Tooltip does not create a tab stop;
- `Escape` dismisses immediately and Tooltip stays suppressed until hover/focus resets;
- trigger activation closes Tooltip immediately;
- opening another Tooltip closes the previous Tooltip in the same interaction context;
- essential information is not Tooltip-only;
- touch flows do not depend on Tooltip discovery or Tooltip-specific tap/long-press behavior.

## Live References

- Figma file: `rROD8ctH9UfPGAMrRrOzHe`
- Component set: `Tooltip / Default`
- Node: `22773:127299`
- Component key: `e29f8f48a0b3ec52f9490d4a9c101df5fba9d769`
- Matrix: 4 Sides × 3 Alignments = 12 variants
- Runtime / Storybook / Code Connect: unregistered / unverified

## Related

- `icon-button.md`
- `toggletip.md`
- `popover.md`
- `coachmark.md`
- `../../foundations/interaction/contextual-guidance.md`
- `../../accessibility/core.md`
- `../../accessibility/focus-management.md`
