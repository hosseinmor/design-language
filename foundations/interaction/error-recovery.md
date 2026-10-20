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

## Principle

Reusable guidance for helping users recover after an operation fails, without inventing product retry/rollback behavior.

> **TBD:** This is the intended domain, not an approved new shared interaction rule.

## Rules

> TBD — Only add owner-reviewed, reusable interaction decisions here. Follow the referenced current sources meanwhile.

## Exceptions

> TBD — Record only approved shared exceptions, not undocumented product-specific behavior.

## Component Implications

> TBD — Existing component contracts remain authoritative for their own anatomy, states and interactions.

## Product Implications

> TBD — Product eligibility, business state and permissions remain in Product Knowledge.

## Accessibility

> TBD — Normative requirements belong to Accessibility documents; link relevant decisions rather than copying them.

## Examples

> TBD — Add validated cross-product examples when approved. Do not invent examples solely to fill this section.

## Open Questions

- When should retry appear inline versus in a surrounding flow?
- What does the consuming surface preserve when an error occurs?
- Which recoverability guarantees are feature-owned?

## Related Documents

- [Error Content](../../foundations/content/patterns/errors.md)
- [Notifications](../../design-system/patterns/notifications.md)

When a reviewed source already owns a rule, update that source rather than duplicating it here. Promote this scaffold only after reusable decisions are approved.
