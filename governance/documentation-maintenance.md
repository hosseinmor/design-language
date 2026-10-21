---
id: design-system.governance.documentation-maintenance
collection: design-system
type: governance
title: Documentation Maintenance
summary: Defines maintenance triggers, review expectations, and validation for canonical Design System documentation.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-21'
related:
- design-system.governance.ownership
- design-system.governance.change-process
- design-system.accessibility.testing
---

# Documentation Maintenance

## Purpose

Keep canonical Design System knowledge aligned with approved behavior, current standards, and AI retrieval without creating a separate release-handoff system.

## Roles

- The named document owner approves canonical changes.
- Contributors provide implementation evidence, product evidence, standards evidence, or reviewed design decisions.
- AI may identify drift, propose scoped edits, and run deterministic checks, but it does not invent missing owner decisions.

## Maintenance Triggers

Review the smallest affected document set when:
- approved component or pattern behavior changes;
- a token/foundation contract changes;
- standards guidance materially changes;
- an implementation exposes a contradiction or known accessibility gap;
- AI retrieval routes to stale, missing, or conflicting guidance;
- a document is promoted to a maturity state that changes downstream retrieval behavior.

Do not rewrite unrelated Design System documents merely because one document is being reviewed.

## Process

1. Reconcile the proposed change against current `main`.
2. Preserve unresolved behavior as an explicit gap instead of guessing.
3. Apply approved changes on a dedicated branch and pull request.
4. Update `last_reviewed` when normative or operational content receives owner review.
5. Regenerate the Manifest **and Graph** with `python tooling/generate_manifest.py generate` when indexed documents, metadata, aliases, or relationships change. Regenerate the component-mapping index with `python tooling/generate_component_mapping_index.py generate` when the mapping evidence layout changes.
6. Run `python tooling/generate_manifest.py check`, `python tooling/generate_component_mapping_index.py check`, `python tooling/validate_links.py`, `python tooling/validators/check_ai_governance.py` and its negative-case unit tests before merge.
7. When the change affects the accessibility corpus, accessibility routing, or an accessibility-relevant component/pattern contract, run `python tooling/validators/check_accessibility_knowledge.py` and the applicable manual regression gate in `accessibility/testing.md`.
8. Do not mark semantic eval fixtures as passing unless a real evaluator ran; do not conflate GitHub checks with Figma, Storybook, assistive-technology or production verification.

## Accessibility Corpus Maintenance

The operational accessibility corpus is canonical Design System knowledge. Audit reports, stress-test artifacts, scorecards, project prompts, and review evidence remain outside ordinary Product Design retrieval unless a separate evidence area explicitly says otherwise.

A draft/scaffold component may continue to rely on fail-open accessibility routing. Promoting a component or pattern so that AI can stop at its local contract requires the relevant accessibility behavior to be defined, reviewed, and free of blocking known gaps.

## Review Requirements

Owner review is required before changing:
- normative Design System behavior;
- accessibility requirement levels or standards interpretation;
- component/pattern maturity used as an AI retrieval stop signal;
- routing or ownership policy.

## Definition of Done

A documentation change is maintenance-ready when:
- the smallest owning documents were changed;
- ownership and maturity metadata are accurate;
- related IDs resolve;
- generated Manifest/Graph and relevant secondary indexes are current;
- required deterministic and manual regression gates pass;
- known gaps and untested behavior remain explicit.
