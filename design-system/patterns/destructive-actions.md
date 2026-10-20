---
id: design-system.pattern.destructive-actions
collection: design-system
type: pattern
title: Destructive Actions
summary: 'Use destructive treatment when an action:'
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
| Visible independent destructive action | Danger Outline |
| Final destructive confirmation | Danger Filled |

Danger Filled is not the default destructive Button. It is reserved for final confirmation.

## Risk and Recoverability

When an action is low-risk and undoable, a neutral treatment may be more appropriate.

Rare destructive actions should generally be placed in an overflow menu.

## Confirmation Group

Default final confirmation:

```text
Danger Filled + Ghost
```

The destructive label should describe the consequence.

## Disabled State

A disabled destructive Button uses neutral disabled tokens. Disabled state takes priority over danger tone.

## Related Documents

- `../components/button.md`
- `confirmation.md`
- `../../foundations/interaction/action-hierarchy.md`
