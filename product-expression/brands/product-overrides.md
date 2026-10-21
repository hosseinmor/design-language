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

> **TBD / Unverified.** No specific Product Override is established by this placeholder. Absence of a record here does not prove that a live Product has no exception.

## Override Criteria

A Product Override is a **reviewed, scoped deviation from an otherwise shared Design Language decision**, justified by a stable Product-specific need. Do not classify these as overrides:

- a Theme choosing different concrete values for the same shared token meaning;
- ordinary Product eligibility, permissions, user flow or business logic (owned by Product Knowledge);
- a component variation already supported by its shared canonical API;
- temporary Figma/runtime drift awaiting reconciliation;
- exploratory UI that has not been reviewed or approved.

When shared reuse is possible, prefer updating the owning shared rule or component/pattern instead of granting an exception.

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

A deviation affecting shared component behavior still requires coordinated review with the component's owner and runtime implementation team.

## Product-Specific Exceptions

> **TBD:** This section will hold linked, narrowly scoped exceptions once approved. Do not reproduce Product Knowledge's permissions, workflows or lifecycle data here; link to their owning Product documents.

## Deprecation and Review

**Proposed lifecycle rule (TBD):** Reassess an approved exception when its Product scope, component contract, Theme relationship, accessibility requirements, or governing shared rule changes. Retire it once shared behavior is suitable again, preserving the reviewed rationale in change history.

## Related Documents

- [Theme Context](theme-context.md) — legitimate Theme value variation and Application/Theme relationship.
- [Brand Variants](brand-variants.md) — shared Brand selection rationale; Product-specific approvals remain to be collected.
- [Sources of Truth](../../integrations/source-of-truth.md) — authority and conflict resolution.
