---
id: design-system.pattern.confirmation
collection: design-system
type: pattern
title: Confirmation and Modal Actions
summary: Cancel is usually Ghost.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Confirmation and Modal Actions

## Default Modal Combinations

| Modal type | Default combination |
|---|---|
| Standard modal | Primary + Ghost |
| Modal with a valid alternative | Primary + Tertiary |
| Approved Brand conversion modal | Brand + Ghost |
| Brand conversion modal with a valid alternative | Brand + Tertiary |
| Destructive confirmation | Danger Filled + Ghost |

`Brand` is used only when the modal action is an approved product conversion or product-defining moment. Do not use Brand merely because the modal contains the visually strongest action; ordinary confirmation remains Primary.

## Cancel

Cancel is usually Ghost.

Tertiary is defensible when a product policy requires a clearer container for Cancel, but the choice must be consistent within that product.

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
