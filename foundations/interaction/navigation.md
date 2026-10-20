---
id: design-system.experience-rule.navigation
collection: design-system
type: experience-rule
title: Navigation
summary: Semantics are independent from visual appearance.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Navigation

## Link Versus Button

Semantics are independent from visual appearance.

- An action that changes state or performs an operation uses a native Button.
- An action that navigates to another destination uses a native Link.

A Link may use Button visual styling while retaining Link semantics and accessibility behavior.

“Read more” and “View all” may appear as text links or Button-styled links depending on context. Their destination determines semantics; appearance does not.

## Flow Navigation Terms

Back, Cancel, Close, and Exit have different meanings. Their detailed behavior in multi-step flows is documented in `../../design-system/patterns/multi-step-flow.md`.

## Related Documents

- `../../design-system/components/button.md`
- `../../design-system/components/link.md`
- `../../design-system/patterns/multi-step-flow.md`
