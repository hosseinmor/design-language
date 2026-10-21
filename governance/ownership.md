---
id: design-system.governance.ownership
collection: design-system
type: governance
title: Ownership
summary: Defines ownership and review responsibility for shared Design System knowledge, including the accessibility corpus.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-21'
related:
- design-system.governance.documentation-maintenance
- design-system.governance.change-process
- design-system.accessibility.conformance-and-policy
---

# Ownership

## Purpose

Keep canonical Design System knowledge reviewable and maintainable without tying repository structure to team structure.

## Roles

### Design System team

The Design System team is the canonical owner of shared Design System foundations, tokens, components, patterns, governance, and accessibility guidance unless a document explicitly names another owner.

For the operational accessibility corpus, the Design System team owns standards interpretation, cross-document consistency, routing integrity, and approval of canonical changes.

### Product and feature owners

Product teams own product-specific composition, flow policy, business rules, copy, and implementation decisions that use the Design System. A product flow such as Apply + Screening Questions requires a Product/Pattern owner; specialized accessibility documents do not become the owner of product-specific behavior.

### Contributors and reviewers

Designers, engineers, QA, AI agents, and accessibility reviewers may propose changes and evidence. Canonical approval remains with the named owner.

## Process

- All documents with `collection: design-system` or `collection: design-language` inherit `Design System team` as their **maintaining steward**, regardless of `document_maturity`, `knowledge_state`, Manifest `status`, or design handoff status. An explicit document `owner` takes precedence.
- The 18 operational documents under `accessibility/` inherit `Design System team` regardless of maturity, unless they explicitly name another approved owner.
- The generated Manifest **MUST** resolve an effective owner for these shared collections. Other collections (for example, `content` and product-owned knowledge) keep their own stewardship rules or explicit owners, rather than inheriting the Design System default.
- **Stewardship is not approval.** A Draft or Scaffold retains its maturity, outstanding owner decisions, review gates and unresolved implementation facts. A recorded owner never certifies publication, design signoff, or a runtime release.
- A normative change may still require Product, engineering or accessibility co-review. The shared steward does not replace domain-specific approval.
- Explicit alternative owners must be reviewed and recorded. Changing stewardship defaults or overrides requires an owner-reviewed pull request.

## Review Requirements

Owner review is required when a change:
- changes normative Design System behavior;
- changes accessibility requirement levels or standards interpretation;
- changes component/pattern maturity used by AI retrieval;
- changes routing, ownership, deprecation, or release policy.

## Definition of Done

A canonical Design System knowledge change is ownership-ready when:
- the owning document or collection default is clear;
- the manifest resolves the effective owner where required;
- unresolved decisions remain explicit;
- repository validation passes;
- required domain-specific regression gates pass.
