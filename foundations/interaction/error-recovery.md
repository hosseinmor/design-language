---
id: design-system.experience-rule.error-recovery
collection: design-system
type: experience-rule
title: Error Recovery
summary: TBD cross-component recovery guidance; message content and feature-specific retry policy remain in their owning sources.
knowledge_state: unverified
document_maturity: scaffold
related:
  - content.pattern.error
  - design-system.pattern.notifications
---

# Error Recovery

> **TBD / Unverified — this document is a reserved scope, not an approved guideline.** Do not infer behavior, tokens, timing or implementations from this placeholder.

## Intended scope (TBD)

Reusable guidance for helping users recover after an operation fails, without inventing product retry/rollback behavior.

## Questions to resolve

- When should retry appear inline versus in a surrounding flow?
- What does the consuming surface preserve when an error occurs?
- Which recoverability guarantees are feature-owned?

## Existing owners and references

- [Error Content](../../foundations/content/patterns/errors.md)
- [Notifications](../../design-system/patterns/notifications.md)

When a reviewed source already owns a rule, update that source instead of duplicating it here. Only promote this scaffold after the owner approves genuinely reusable decisions.
