---
id: design-system.governance.deprecation
collection: design-system
type: governance
title: Deprecation
summary: TBD shared Design Language deprecation and alias migration policy; do not infer automatic Figma or Karbon compatibility.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.governance.ownership
  - design-system.governance.change-process
  - design-system.component.modal
  - design-system.reference.source-of-truth
---

# Deprecation

> **TBD / Unverified.** This is a reserved Governance topic, not an approved process. Use the linked reviewed policies for currently effective requirements. Each related document retains its own maturity and evidence boundary.

## Purpose

Reserve policy for retiring or renaming shared components, tokens, patterns and document contracts. This is **not** an approved sunset schedule or a guarantee of backward compatibility.

## Roles

Current [Ownership](ownership.md) requires Design System owner review for normative changes; Figma publication/library identity and Karbon runtime releases are owned by their respective live sources. **TBD:** migration-specific owners and required external approvals.

## Process

**TBD:** support windows, alias lifetime, migration notice, deprecation phases, and removal gates. Preserve stable knowledge IDs when moving documents; existing [Change Process](change-process.md) and [Source of Truth](../integrations/source-of-truth.md) rules apply. The [Modal legacy alias](../design-system/components/modal.md) is **one documented component-specific migration fact**, not evidence of a universal lifecycle rule.

## Review Requirements

Use the existing reviewed [Change Process](change-process.md) for any actual shared contract change. **TBD:** criteria for approving a global deprecation timetable and validating migrated consumers across Figma/Code.

## Definition of Done

**TBD:** deprecation exit/retirement criteria. Do not claim that unverified runtime consumers, library keys or aliases have been migrated without source evidence.

## Open Decisions

- Confirm whether the scope needs a standalone policy beyond the reviewed owning documents.
- Record explicit Design System owner approval before promoting this scaffold.
- Resolve dependencies on Figma/Karbon with live-source evidence **at the final reconciliation stage**, not assumptions in this document.
