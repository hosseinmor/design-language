---
id: design-system.pattern.confirmation
collection: design-system
type: pattern
title: Confirmation and Modal Actions
summary: Defines confirmation composition and safe exit decisions, delegating action hierarchy, Dialog anatomy and copy to their owners.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Confirmation and Modal Actions

## Action hierarchy

Use the shared [Action Hierarchy](../../foundations/interaction/action-hierarchy.md) for Button combinations across action groups; do not define a second preset matrix here. For destructive confirmation, follow [Destructive Actions](destructive-actions.md) and the canonical `Danger Primary` Button Style.

The confirmation pattern owns **how a consequential confirmation is composed** and the relationship between the consequence, safe alternative, and Close/Cancel. The feature owner determines whether a confirmation is mandated by product policy; the [Confirmation Content pattern](../../foundations/content/patterns/confirmations.md) owns the wording and decision-oriented copy. The [Dialog component](../components/dialog.md) owns modal anatomy, focus, dismissal and shell behavior. [Confirmation Content](../../foundations/content/patterns/confirmations.md) owns message wording and labels.

## Cancel

Cancel is usually Ghost.

A Tertiary alternative may be appropriate when a documented product context requires more visual prominence; do not silently establish it as a universal Cancel default.

The final cross-product rule remains open.

## Close Icon and Cancel Button

A modal may contain both a Close icon and a Cancel Button when both behaviors are clear and consistent.

## Risk and Data Loss

When closing or cancelling causes data loss, show an explicit confirmation. Do not rely on Button appearance alone.

A destructive confirmation may include a `surface/danger-muted` callout when the interface needs a persistent pre-action explanation of irreversible consequences. Danger communicates destructive intent; it is not an Error state.

## Related Documents

- `../components/button.md`
- `../../foundations/interaction/action-hierarchy.md`
- `destructive-actions.md`
- `multi-step-flow.md`
