---
id: design-system.governance.ownership
collection: design-system
type: governance
title: Ownership
summary: Defines ownership and review responsibility for shared Design System knowledge, including the accessibility corpus.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-03'
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

- Canonical/reviewed Design System documents **MUST** resolve to an effective owner in the generated Manifest, through an explicit `owner` or the reviewed shared-collection default below.
- The 18 operational documents in `accessibility/` inherit `Design System team` as their collection owner unless a document explicitly names another approved owner, **regardless of their maturity**.
- Other **reviewed** documents with `collection: design-system` or `collection: design-language` inherit `Design System team` stewardship **only when no explicit `owner` is recorded**. This matches the existing shared-system responsibility above and lets the Manifest expose an effective owner for reviewed contracts.
- Unreviewed documents outside Accessibility **do not receive an inferred owner** from this rule; a draft's actual reviewer/approver remains to be established. A missing owner there is a tracked maintenance gap, not permission for AI to approve its proposals.
- The retrieval manifest **MUST** resolve the effective inherited owner. An inherited owner identifies **stewardship**, not evidence that each sentence was newly reviewed, approved for runtime, or assigned to a named individual.
- Individual documents MAY repeat their inherited owner in frontmatter when useful. Any explicit alternative must be reviewed and recorded; explicit ownership takes precedence over the default.
- Changing collection stewardship or introducing a document-specific override is a governance change and requires owner review through a branch and pull request.

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
