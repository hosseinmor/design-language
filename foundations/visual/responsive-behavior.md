---
id: design-system.foundation.responsive-behavior
collection: design-system
type: foundation
title: Responsive Behavior
summary: TBD routing for visual responsive adaptation that is not already covered by Responsive Layout, adaptive Patterns, or Interaction rules.
knowledge_state: unverified
document_maturity: scaffold
related:
  - design-system.foundation.responsive-layout
  - design-system.pattern.responsive-layout
  - design-system.experience-rule.responsive-interaction
---

# Responsive Behavior

> **TBD / Unverified.** This is a future scope placeholder, not a parallel responsive breakpoint or behavior specification. Existing approved guidance remains in the documents below.

## Breakpoints

Reviewed shared threshold **names and numeric values** belong to [Layout Tokens](../../design-system/tokens/layout/catalog.md). The [Responsive Layout Guideline](responsive-layout/guideline.md) owns their semantic range use. This scaffold must not create a second breakpoint table.

## Adaptation Rules

Adaptive composition examples and current draft decisions belong to [Responsive Layout Patterns](responsive-layout/patterns.md). Only add rules here if a distinct cross-foundation **visual behavior** need emerges after review.

## Component Behavior

Component-specific adaptive variants belong to each Component. Cross-component pointer, touch and keyboard interaction changes are reserved in [Responsive Interaction](../interaction/responsive-interaction.md) (also TBD).

## Content Priority

The current draft [Responsive Layout Patterns](responsive-layout/patterns.md) covers content priority and layout transformations. Product-specific hidden/moved information remains Product Knowledge-owned.

## Open decisions

- Is there a genuinely independent visual responsive behavior contract that is neither Layout nor Interaction nor a Pattern?
- If not, retire this placeholder in a separate, reviewed structural cleanup while retaining an ID alias for existing AI references.

