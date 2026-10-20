---
id: design-system.foundation.responsive-layout-examples
document_type: design-system
collection: design-system
type: foundation
title: Responsive Layout Examples
summary: Template and rules for documenting validated product-specific responsive layout examples.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.responsive-layout
---

# Responsive Layout Examples

> Status: Scaffold — no product example has been validated and added yet.

This directory is reserved for reviewed examples from real product behavior. Examples are non-normative evidence: they must not redefine Foundation rules or present Figma-only behavior as implemented behavior.

## Suggested files

```text
list-detail.md
operational-workspace.md
settings-form.md
```

Create an example only when it adds reusable evidence beyond the general guideline.

## Example template

```md
---
id: design-system.example.{example-id}
document_type: design-system
collection: design-system
type: foundation
title: {Example title}
summary: {One-sentence summary of the responsive decision}
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
---

# {Example title}

## Context

- Product:
- Product area:
- User task:
- Evidence source:
- Implementation status:

## Compact behavior

Describe the page or component behavior below the relevant threshold.

## Expanded behavior

Describe the behavior above the relevant threshold.

## Trigger

- Type: viewport breakpoint | container query | local condition
- Threshold:
- Reason:

## Information priority

- Always visible:
- Moved behind disclosure:
- Hidden:
- Reordered:

## Interaction continuity

- Focus behavior:
- Keyboard behavior:
- Back-navigation behavior:
- Scroll and selection preservation:

## Exceptions and unresolved decisions

- Unknown:
- Assumption:
- Exception:
```

## Review requirements

Before an example becomes reviewed:

- confirm whether it reflects production, an approved design, or only a proposal;
- identify the relevant product owner or Design System owner;
- verify behavior at both sides of the threshold;
- verify RTL and content expansion;
- document known deviations from the shared responsive specification.
