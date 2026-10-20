---
id: design-system.governance.change-process
collection: design-system
type: governance
title: Change Process
summary: Defines the branch, review, validation, and maturity rules for canonical Design System knowledge changes.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-03'
related:
- design-system.governance.ownership
- design-system.governance.documentation-maintenance
- design-system.accessibility.testing
---

# Change Process

## Purpose

Apply Design System knowledge changes through a small, reviewable path while preserving canonical `main`, retrieval integrity, and explicit owner decisions.

## Roles

- Contributor: proposes the smallest change supported by reviewed evidence or an approved decision.
- Named owner: reviews the owning behavior and metadata.
- Reviewer/QA: validates implementation or accessibility evidence when the change requires it.

## Process

1. Read current `main` and the owning Design System documents.
2. Classify the change as one or more of:
   - documentation clarification;
   - behavior/contract change;
   - foundation/token change;
   - component/pattern maturity change;
   - accessibility standards/routing change;
   - governance/deprecation/release change.
3. Keep unresolved behavior explicit instead of silently filling gaps.
4. Create a dedicated branch; never write directly to `main`.
5. Change only the smallest affected document set.
6. Regenerate `manifest.generated.json` when indexed documents change.
7. Run `python tooling/generate_manifest.py check`.
8. Run any domain-specific deterministic and manual regression gates triggered by the change.
9. Open a pull request and obtain the required owner review before merge.

## Accessibility Change Gate

When a change affects:
- `accessibility/**`;
- accessibility routing from `ai/router.md`;
- accessibility ownership/maintenance policy;
- a component or pattern whose maturity may allow AI to stop specialized accessibility retrieval;

run:

```bash
python tooling/validators/check_accessibility_knowledge.py
```

and apply the relevant manual checks in `accessibility/testing.md`.

The deterministic script validates structural invariants; it does not replace component, flow, keyboard, screen-reader, or complete-process testing.

## Maturity Changes

Do not promote a Component/Pattern to a maturity state used as an accessibility retrieval stop signal merely because the file is complete-looking.

Before such promotion:
- its relevant accessibility contract must be defined;
- blocking known accessibility gaps must be resolved or the contract must remain fail-open;
- required tests/evidence must be recorded;
- the named owner must review the promotion.

## Review Requirements

Owner review is required for normative behavior, maturity/routing, standards interpretation, governance, and deprecation changes.

## Definition of Done

A change is ready for merge when:
- scope is limited to owning documents;
- metadata and ownership are accurate;
- generated manifest state is current;
- repository checks pass;
- triggered accessibility/domain gates pass;
- known gaps remain visible;
- the pull request has the required owner approval.
