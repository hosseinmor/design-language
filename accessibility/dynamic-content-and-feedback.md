---
id: design-system.accessibility.dynamic-content-and-feedback
collection: design-system
type: accessibility
title: Dynamic Content and Feedback
summary: Defines accessible status messages, alerts, loading, async updates, toasts, progress, and dynamic-content announcement behavior.
knowledge_state: canonical
document_maturity: reviewed
related:
- design-system.accessibility.core
- design-system.accessibility.focus-management
- design-system.accessibility.screen-reader-semantics
- design-system.accessibility.forms
last_reviewed: '2026-09-02'
---

# Dynamic Content and Feedback

This document owns programmatic feedback for important changes that occur without moving focus. Focus movement itself belongs to `focus-management.md`; form validation ownership is in `forms.md`.

## Status Messages — WCAG 4.1.3 AA

When a status message is presented without receiving focus, **MUST** expose it programmatically so assistive technology can present it without requiring focus.

Typical examples:
- save/submission succeeded;
- save/submission failed when focus does not move to the error;
- search results/count updated;
- item added/removed;
- background action completed;
- important loading/progress state.

Not every DOM update is a status message and not every visual change requires a live announcement.

## Use the least interruptive mechanism

**SHOULD** use non-interruptive status semantics for routine updates. Reserve assertive/alert behavior for genuinely urgent information that requires immediate attention.

Do not use `role="alert"` as the default for every Toast, validation message, or loading event.

## Focus vs announcement

If the user must immediately interact with a newly created context (for example a Modal or focused error summary), focus may carry the orientation and a separate announcement may be unnecessary or duplicative.

If focus should remain where the user is working, use status/live semantics where required instead of stealing focus.

**MUST NOT** move focus to a spinner or Toast merely to make it discoverable.

## Loading and progress

A component/flow should define whether loading is:
- local control state;
- page/region busy state;
- determinate progress;
- indeterminate progress.

**MUST** keep the operation understandable and prevent accidental duplicate activation where repeated submission would be harmful.

Use `aria-busy`, progress semantics, or status messages only when they correctly describe the actual state; do not add them mechanically.

For long-running operations, **SHOULD** communicate progress or continued activity sufficiently to avoid the appearance of a stalled task.

## Toasts and notifications

A Toast is a visual presentation pattern, not a semantic role.

The semantic behavior depends on the message importance and whether the user needs to act.

**SHOULD** keep routine confirmation non-interruptive. If a Toast contains interactive controls, those controls must be keyboard accessible, but the Toast should not automatically steal focus just because it appeared.

If a transient message disappears automatically, ensure users have sufficient opportunity to perceive/use it when timing requirements apply.

## Search/filter/result updates

When search/filtering updates results in place:
- preserve the user's focus unless the workflow intentionally changes context;
- **SHOULD** announce a concise result/status change when users who cannot see the update would otherwise miss essential feedback;
- avoid announcing every keystroke or every minor result mutation.

## Add/remove/reorder

For an operation that changes a collection:
- if the focused element remains, preserve focus where practical;
- if the focused element is removed, `focus-management.md` requires deliberate relocation;
- announce the result when users otherwise would not know the operation succeeded/failed.

## Errors

Field error mechanics belong to `forms.md`.

Do not both move focus to an error summary and redundantly fire a highly interruptive alert unless the behavior has been deliberately tested and justified.

## Emerging announcement APIs

Experimental/draft APIs such as `ariaNotify` may be tracked for future use, but they are **not the production baseline** while support/specification remains emerging.

**MUST NOT** rely on an emerging announcement API as the sole production path for required status communication.

The stable baseline remains native/ARIA semantics supported by the adopted browser/AT matrix.

## Ownership

| Component/Design System owns | Product/Pattern owns |
|---|---|
| Supported status/loading mechanism | Which event deserves feedback |
| Toast/Notification semantic capability | Actual message and severity |
| Busy/progress mechanism | Business progress/state |
| Component focus behavior | Cross-flow next focus target |

## Testing

For applicable async/dynamic work, test success/failure, rapid/repeated actions, focus preservation/removal, status exposure in the accessibility tree, representative screen-reader output, and whether routine updates become noisy or interruptive.

## AI contract

AI **MUST** distinguish status announcements from focus management, use the least interruptive adequate mechanism, avoid alert-everything behavior, and treat `ariaNotify` or other emerging APIs as experimental rather than baseline production guidance.

## References

- WCAG 2.2 — 4.1.3 Status Messages
- WCAG 2.2 — 2.2 Timing requirements where applicable
- WAI-ARIA 1.2 live/status semantics
