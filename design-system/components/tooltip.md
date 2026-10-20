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

Runtime visibility, delay, collision, flip, portal behavior, and dismissal implementation remain code-owned.

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
- keyboard focus.

Tooltip is not click-triggered.

### Dismissal

Tooltip dismisses when:

- pointer hover leaves the relevant trigger/content region;
- keyboard focus moves away;
- the user presses `Escape` while the Tooltip is shown.

Exact open and close delays are not yet locked in the design-system runtime contract.

### Hoverability and persistence

Hover/focus-triggered supplemental content must satisfy the shared accessibility requirement for dismissible, hoverable, and persistent content where applicable.

The rendered Tooltip surface must participate in pointer hit-testing when that is necessary to preserve hover. Do **not** use `pointer-events: none` on the Tooltip surface if doing so causes the Tooltip to close while the pointer moves from the trigger onto the Tooltip.

Runtime may satisfy the transition between trigger and Tooltip through direct hover retention, a hover bridge / safe-polygon strategy, or a short close grace interval. The implementation technique and exact timing remain code-owned; the behavioral requirement is that a user can move the pointer onto the Tooltip without it disappearing prematurely.

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

Tooltip improves visible discoverability for Icon Button but does not provide Button semantics or accessible naming.

A disabled control must not become focusable solely so Tooltip can explain why it is disabled.

If the reason for disabled state matters to task completion, expose that reason through persistent UI or another appropriate feedback pattern.

## Touch / Mobile

Tooltip is not a primary touch disclosure pattern.

Do not require long-press or hidden tap behavior merely to preserve desktop Tooltip content.

When the user must be able to intentionally request the information on touch, use Toggletip instead.

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
- hover + focus triggers;
- Escape dismissal;
- collision/flip;
- portal/layering;
- accessibility relationship;
- RTL logical Start/End;
- touch fallback boundary.

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
- hover and keyboard focus both reveal Tooltip;
- moving the pointer from the trigger onto the Tooltip does not cause premature dismissal;
- Tooltip does not create a tab stop;
- Escape dismisses it;
- essential information is not Tooltip-only;
- touch flows do not depend on Tooltip discovery.

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
