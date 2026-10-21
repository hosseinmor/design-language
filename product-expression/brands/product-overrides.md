---
id: design-system.product-variation.product-overrides
collection: design-system
type: product-variation
title: Product Overrides
summary: Unverified scaffold for recording reviewed deviations from shared Design Language rules by Product, without conflating Theme values or business policy.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.product-variation.theme-context
  - design-system.product-variation.brand-variants
  - design-system.reference.source-of-truth
---

# Product Overrides

> **TBD / Unverified.** No specific Product Override is established by this placeholder. **The criteria, recording fields and lifecycle process below are proposed for owner review, not approved governance policy.** Absence of a record here does not prove that a live Product has no exception.

## Override Criteria

**Proposed definition (TBD):** A Product Override would be a **reviewed, scoped deviation from an otherwise shared Design Language decision**, justified by a stable Product-specific need. The categories below should normally be routed to their existing owners instead of becoming Overrides:

- a Theme choosing different concrete values for the same shared token meaning;
- ordinary Product eligibility, permissions, user flow or business logic (owned by Product Knowledge);
- a component variation already supported by its shared canonical API;
- temporary Figma/runtime drift awaiting reconciliation;
- exploratory UI that has not been reviewed or approved.

**Proposed decision preference (TBD):** Where shared reuse is possible, update the owning shared rule or component/pattern rather than grant an exception. Final exception governance must be approved by the Design System owner.

## Approved Overrides

> **TBD:** No approved override records have been added **to this registry** yet. Do not invent an example or infer implementation approval from the heading.

**Proposed review record fields (TBD until owner-approved):**

| Field | Required evidence |
|---|---|
| Product and affected context | Product name, area/task and exact component or pattern |
| Rule being overridden | Stable Design Language document ID and precise shared decision |
| Reason and decision | Why shared behavior is insufficient and what changes |
| Ownership and approval | Named Design System and relevant Product owners, review link/date |
| Accessibility and content | Applicable normative checks and copy implications |
| Scope and lifecycle | Effective situations, expiry/review trigger, deprecation route |
| Live implementation | Figma/source identity and Karbon/Storybook version when confirmed; otherwise explicitly unverified |

**Proposed review requirement (TBD):** A deviation affecting shared component behavior should receive coordinated approval from the component's Design System owner and runtime implementation team.

## Product-Specific Exceptions

> **TBD:** This section will hold linked, narrowly scoped exceptions once approved. Do not reproduce Product Knowledge's permissions, workflows or lifecycle data here; link to their owning Product documents.

## Deprecation and Review

**Proposed lifecycle rule (TBD):** Reassess an approved exception when its Product scope, component contract, Theme relationship, accessibility requirements, or governing shared rule changes. Retire it once shared behavior is suitable again, preserving the reviewed rationale in change history.

## Related Documents

- [Theme Context](theme-context.md) — legitimate Theme value variation and Application/Theme relationship.
- [Brand Variants](brand-variants.md) — shared Brand selection rationale; Product-specific approvals remain to be collected.
- [Sources of Truth](../../integrations/source-of-truth.md) — authority and conflict resolution.
