---
id: design-system.ui-template.component-template
collection: design-system
type: ui-template
title: Component Name
summary: Minimum decision-contract template for a reusable Design System component.
knowledge_state: canonical
document_maturity: reviewed
related: []
---

# Component Name

## Purpose

What problem does this component solve?

## Use / Avoid

When should it be used, and what nearby component/pattern should be used instead when it is not appropriate?

## Choices

Document only meaningful designer-facing variants, sizes, or decision rules. Do not copy generated Figma/API property tables.

## Behavior and States

Document non-obvious interaction/state behavior. Native/default behavior can be referenced rather than re-specified.

## Composition and Content

Document constraints that affect how the component is composed or understood. Omit when there is nothing component-specific.

## Accessibility

Document only the component-specific accessibility contract. Reference shared Accessibility guidance for general rules. Composite/custom widgets need the full keyboard/focus/semantic contract; simple native controls can stay compact.

## Known Gaps

List unresolved, unsupported, or intentionally deferred behavior. Omit when none exist.

## Live References

- Figma:
- Storybook / Code:

### Optional sections

Add only when they materially affect decisions:
- Anatomy
- Product Variations
- Token Exceptions
- Migration Notes (temporary; remove after migration is no longer operationally relevant)
