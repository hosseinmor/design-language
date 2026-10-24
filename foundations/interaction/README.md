# Interaction foundations

These documents own **cross-component interaction rules only**.

Create or keep an interaction foundation when the same decision materially
affects several components or patterns and has one stable shared meaning.

Do not use this directory to duplicate:
- component-specific behavior → keep it in the component;
- reusable composition/flow behavior → keep it in the pattern;
- normative accessibility requirements → Accessibility owns them;
- product-specific business behavior → Product Knowledge owns it.

A non-owner document may summarize the integration point and link to the canonical owner.

## Current ownership map

| Interaction decision | Canonical owner |
|---|---|
| Action-group hierarchy | [Action Hierarchy](action-hierarchy.md) |
| Choosing Tooltip/Toggletip/Popover/Coachmark/Tour | [Contextual Guidance](contextual-guidance.md) |
| Meaning of selected/current/checked/on/applied states | [Selection](selection.md) |
| Editing compound dates/times through numeric segments | [Segmented Field Editing](segmented-field-editing.md) |
| Inherited RTL/LTR layout context, logical Start/End and mirroring (owner review pending) | [Directionality](directionality.md) |
| Link versus Button semantics | [Navigation](navigation.md) |
| Busy/loading composition | [Loading and Progress pattern](../../design-system/patterns/loading-and-progress.md) |
| Inline versus Toast feedback | [Notifications pattern](../../design-system/patterns/notifications.md) |
| Normative focus/keyboard accessibility | [Focus Management](../../accessibility/focus-management.md) |

Unfinished Interaction files are **explicit TBD placeholders**, not approval of missing rules. Use their referenced canonical source for currently reviewed behavior. A separate `draft` may still document supported design decisions; [AI retrieval](../../ai/retrieval.md) explains the distinction.
