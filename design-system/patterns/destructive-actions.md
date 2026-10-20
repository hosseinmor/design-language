---
id: design-system.pattern.destructive-actions
collection: design-system
type: pattern
title: Destructive Actions
summary: Distinguishes destructive consequences and maps low-emphasis entry points to final confirmation.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Destructive Actions

## Determine Whether an Action Is Destructive

Use destructive treatment when an action:

- Deletes data
- Removes access
- Causes irreversible cancellation
- Has another serious and difficult-to-recover consequence

A negative verb alone is not enough. A reversible rejection action is not automatically destructive.

## Entry Point and Final Confirmation

| Stage | Button treatment |
|---|---|
| Low-emphasis or inline entry point | Danger Ghost |
| Visible independent destructive action | Danger Tertiary |
| Final destructive confirmation | Danger Primary |

Danger Primary is not the default destructive Button. It is reserved for final confirmation.

## Risk and Recoverability

When an action is low-risk and undoable, a neutral treatment may be more appropriate.

Rare destructive actions should generally be placed in an overflow menu.

## Confirmation Group

Use the [Action Hierarchy](../../foundations/interaction/action-hierarchy.md) for the action-group combination, normally `Danger Primary` with a low-emphasis safe exit. The destructive label should describe the consequence; [Confirmation Content](../../foundations/content/patterns/confirmations.md) owns its copy.

## Disabled State

A disabled destructive Button uses neutral disabled tokens. Disabled state takes priority over danger tone.

## Related Documents

- `../components/button.md`
- `confirmation.md`
- `../../foundations/interaction/action-hierarchy.md`
