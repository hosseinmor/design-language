---
id: content.content-guidelines
collection: content
type: content-guideline
title: Content Guidelines
summary: Routes shared product-content decisions across voice, terminology, localization, patterns, component contracts, and executable evaluations.
knowledge_state: unverified
document_maturity: draft
related:
  - content.product-voice
  - content.terminology
  - content.localization
  - content.component.button
  - content.component.text-input
  - content.component.modal
  - content.component.notification
  - content.pattern.error
  - content.pattern.confirmation
  - content.pattern.empty-states
  - content.pattern.notifications
  - content.pattern.loading-and-progress
  - content.pattern.ai-content-and-disclosure
  - content.pattern.instructions-and-helper-text
---

# Content Guidelines

This document is the shared human entry point. Detailed voice is owned by
[`product-voice.md`](product-voice.md), terminology by
[`terminology.md`](terminology.md), and machine-readable terms by
[`terminology/terms.yml`](terminology/terms.yml).

Persian language, RTL, mixed-direction text, number/date formatting,
translation, and dynamic variables are owned by
[`localization.md`](localization.md). Its machine-readable contract and evals
are in [`localization.yml`](localization.yml) and
[`../../ai/evals/content/localization-cases.yml`](../../ai/evals/content/localization-cases.yml).

Use the smallest relevant layer:

```text
Foundation
→ Voice, Persian language, terminology, localization

Pattern
→ Instructions, errors, confirmations, empty states, notifications, loading,
  and AI content

Component contract
→ Button, input, modal, notification, and other component-specific copy

Eval
→ Executable examples and regression cases
```

Do not copy Product Knowledge into this directory. JobVision concepts and
behavior remain canonical at <https://docs-jv.jvoffice.ir/>; Cando concepts and
behavior remain canonical at <https://docs-cd.jvoffice.ir/>. Content owns
naming and communication rules, not product behavior.

## Voice and Tone

Use [`product-voice.md`](product-voice.md) for the evidence-backed voice,
precedence order, operational tone dimensions, and surface matrix. Use
[`product-voice.yml`](product-voice.yml) when an AI or validator needs the
structured contract.

Voice remains consistent; tone changes with task, risk, and user state. Do not
apply warmth or brand expression at the expense of product truth, recovery, or
accessibility.

## UI Copy Principles

- Prefer explicit outcomes over generic labels.
- Preserve product truth; do not improve tone by changing meaning.
- Apply terminology for the current audience and surface.
- Keep unknown product behavior explicit.

## Localization

Use the localization foundation whenever copy contains numbers, dates, times,
units, amounts, user-entered text, English passages, URLs, identifiers, or
runtime variables. Do not infer calendar, digit, timezone, or currency policy
from the Persian UI language.

## Audience and Product Context

Load audience-, product-, and feature-specific terminology from the owning
Product Knowledge source after applying these shared rules. Do not copy those
contracts into Design Language. Product context may select among shared terms
and tones, but it owns lifecycle, permission, eligibility, validation, and flow.

## Labels

Use the preferred label for the concept and surface from the terminology source.
Do not use implementation names as labels merely because they exist in code.

## Button Labels

Use [`components/button.md`](components/button.md) when content appears on a
Button or when choosing between Button, Link, and Icon Button semantics. Its
machine-readable contract and evals are in
[`components/button.yml`](components/button.yml) and
[`../../ai/evals/content/button-content-cases.yml`](../../ai/evals/content/button-content-cases.yml).

Name the real action or result with the shortest unambiguous label. Preserve the
action identity while Loading, make confirmation exits explicit, and do not use
generic labels, promotional pressure, internal terms, or early success language.

## Instructions

Use
[`patterns/instructions-and-helper-text.md`](patterns/instructions-and-helper-text.md)
to distinguish labels, mandatory instructions, helper text, placeholders,
examples, requirement indicators, and errors. Its machine-readable contract and
evals are in
[`patterns/instructions-and-helper-text.yml`](patterns/instructions-and-helper-text.yml)
and [`../../ai/evals/content/instruction-helper-cases.yml`](../../ai/evals/content/instruction-helper-cases.yml).

Required instructions must be available before users need them. Placeholder is
not a label or a reliable place for essential requirements, and Tooltip or Info
must not be the only source of information needed to complete the task.

### Text Input composition

Use [`components/text-input.md`](components/text-input.md) when composing Label,
Placeholder, Helper, Value, Requiredness, Error, Info, or an adornment action
inside a single-line Text Input. Its machine-readable contract and evals are in
[`components/text-input.yml`](components/text-input.yml) and
[`../../ai/evals/content/text-input-content-cases.yml`](../../ai/evals/content/text-input-content-cases.yml).

Keep each content role distinct, preserve essential requirements when Helper is
replaced by Error, and do not infer validation rules, input-purpose metadata,
normalization, or Disabled/Read only state from copy alone.

## Error Messages

Use [`patterns/errors.md`](patterns/errors.md) for error structure, placement,
tone, recovery, and accessibility. Its machine-readable rules and eval cases
are in [`patterns/errors.yml`](patterns/errors.yml) and
[`../../ai/evals/content/error-cases.yml`](../../ai/evals/content/error-cases.yml).

Minimum contract:

- identify the problem;
- identify recovery when it is known and safe;
- reuse the visible field or object terminology;
- do not blame the user, expose internal code as the explanation, or add brand
  personality.

## Confirmation Messages

Use [`patterns/confirmations.md`](patterns/confirmations.md) to decide whether a
confirmation is needed and to define its action, object, consequence,
recoverability, scope, and safe exit. The machine-readable contract and evals
are in [`patterns/confirmations.yml`](patterns/confirmations.yml) and
[`../../ai/evals/content/confirmation-cases.yml`](../../ai/evals/content/confirmation-cases.yml).

Do not infer destructive intent from a negative verb. Use Danger only when the
actual consequence is destructive or difficult to reverse.

### Modal composition

Use [`components/modal.md`](components/modal.md) when a confirmation, short
form, or response-required message appears in a blocking Modal. Its
machine-readable contract and evals are in
[`components/modal.yml`](components/modal.yml) and
[`../../ai/evals/content/modal-content-cases.yml`](../../ai/evals/content/modal-content-cases.yml).

Give the Modal a task- or decision-specific Title, keep it understandable
without the obscured background, and preserve context through Loading and
recoverable Error states. Do not invent Escape, backdrop, auto-close, initial
focus, or non-dismissible behavior while writing its content.

## Empty States

Use [`patterns/empty-states.md`](patterns/empty-states.md) to distinguish
first-use, empty collections, no-results, cold start, and post-removal states.
Its machine-readable contract and evals are in
[`patterns/empty-states.yml`](patterns/empty-states.yml) and
[`../../ai/evals/content/empty-state-cases.yml`](../../ai/evals/content/empty-state-cases.yml).

Loading, failure, missing permission, and missing eligibility are not empty
states. Do not hide them behind generic no-data language.

## Notifications

Use [`patterns/notifications.md`](patterns/notifications.md) to classify Info,
Success, Warning, and Error feedback and to choose between in-place feedback,
Inline Notification, Toast, and a response-requiring pattern. Its
machine-readable contract and evals are in
[`patterns/notifications.yml`](patterns/notifications.yml) and
[`../../ai/evals/content/notification-cases.yml`](../../ai/evals/content/notification-cases.yml).

Severity describes meaning; it does not determine presentation or assistive-
technology urgency. Announce success only after the product confirms completion,
and do not invent timeout, stacking, placement, or dismissal behavior that the
Design System and runtime have not defined.

### Notification composition

When feedback is rendered as an Inline Notification or Toast, use
[`components/notification.md`](components/notification.md) to map it into the
component anatomy. Its machine-readable contract and component evals are in
[`components/notification.yml`](components/notification.yml) and
[`../../ai/evals/content/notification-content-cases.yml`](../../ai/evals/content/notification-content-cases.yml).

Keep Message independently understandable. Use Inline Description or Toast
Title only when it adds context rather than repeating Message. Allow at most one
meaningful action, use Link for navigation and Button for an operation, and name
an available dismiss control «بستن». Inline Notification and Toast are separate
component identities, not values of one Type axis. Exact timing, stacking,
placement, default dismissibility, and live-region implementation remain runtime
or Design System decisions until their sources define them.

## Loading and Progress

Use [`patterns/loading-and-progress.md`](patterns/loading-and-progress.md) to
distinguish local loading, region busy states, determinate progress, and
indeterminate progress. Its machine-readable contract and evals are in
[`patterns/loading-and-progress.yml`](patterns/loading-and-progress.yml) and
[`../../ai/evals/content/loading-progress-cases.yml`](../../ai/evals/content/loading-progress-cases.yml).

Do not fabricate percentages or time estimates for indeterminate work. Loading
means the result is not known yet; it is not an empty, disabled, success, or
error state. Exact display thresholds and Skeleton behavior remain Design
System and runtime decisions.

## AI-Generated Content

Use
[`patterns/ai-content-and-disclosure.md`](patterns/ai-content-and-disclosure.md)
to classify an AI technology, feature, feature family, assistant, or output and
to define disclosure, review, action, uncertainty, and data-policy boundaries.
Its machine-readable contract and evals are in
[`patterns/ai-content-and-disclosure.yml`](patterns/ai-content-and-disclosure.yml)
and [`../../ai/evals/content/ai-content-cases.yml`](../../ai/evals/content/ai-content-cases.yml).

AI-generated product content follows the same terminology, localization,
pattern, component, and product-truth constraints as human-authored content.
Do not call every AI action an assistant, present a suggestion as a human
decision, guarantee quality or outcomes, or invent privacy and data-use claims.
