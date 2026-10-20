---
id: design-system.pattern.ai-entry-points
collection: design-system
type: pattern
title: AI Entry Points
summary: AI-assisted and AI-generated experiences may use the shared Magic color semantics.
knowledge_state: unverified
document_maturity: draft
related: []
---

# AI Entry Points

## Problem

AI capability appears across more than one component anatomy. The interface needs a repeatable visual language that can identify AI-assisted or AI-generated experiences without turning every AI element into Brand, Accent, Selected, or Support feedback.

## When to Use

Use Magic when the UI is explicitly communicating an AI-assisted, AI-generated, or intentionally magical product capability.

Typical uses include:

- AI entry cards or sections
- AI chips/labels
- AI-specific icons or inline indicators
- Strong AI actions or entry points
- AI-specific outlines when the component anatomy needs a line

Do not use Magic merely as a decorative purple treatment.

## Color ownership

The [Color Semantics](../tokens/color/semantics.md) and [Color Usage](../tokens/color/usage.md) documents own Magic role names, token inventories and combinations. Do not maintain a second token catalog in this pattern.

An AI indicator must not override normal selection, focus, disabled or error behavior. A passive AI container does not become interactive merely by consuming Magic roles.

## Semantic Boundary

Magic means AI capability. It does not replace:

- Brand for product identity or approved conversion moments
- Accent for general chromatic interaction/affordance
- Selected for a component state
- Support for Info/Success/Warning/Error feedback

If an AI feature is also selected, disabled, focused, or in error, compose the relevant component/state semantics rather than using Magic to encode every state.

## Component Composition

A card/section, chip/label, icon/inline indicator, and action entry are **different compositions**. Reuse the appropriate canonical component and give the AI affordance an understandable visible or accessible label. Use shared Magic roles only where they convey AI meaning; selection and action hierarchy still come from the component's own interaction contract.

This document does not authorize a new `ai-card/*` or `ai-button/*` token family. If a repeated AI-specific interaction or composition cannot use existing components, propose a separate reviewed component/pattern contract.

## Accessibility

- Magic color must not be the only cue that an experience is AI-assisted when that distinction is important to understanding or trust.
- Preserve readable text contrast on Magic surfaces.
- Focus remains independent and uses the shared Focus roles.
- Disabled suppresses tone according to the component's normal Disabled contract.

## Product Examples

Current approved use-case categories include AI cards/sections, AI chips/labels, AI entry actions, and AI icons/indicators across JobVision and Cando experiences.

Exact product-level component mappings remain owned by the corresponding component/product documentation.

## Anti-Patterns

- Using Magic for any visually special CTA that is not AI-related
- Using Magic instead of Brand for product identity
- Using Magic instead of Accent for ordinary interaction
- Using Magic instead of Error/Warning/Info feedback
- Building a full component-specific Magic matrix when shared Semantic roles already resolve the anatomy

## Related Documents

- [Color Semantics](../tokens/color/semantics.md)
- [Color Usage](../tokens/color/usage.md)
- [Content for AI disclosure](../../foundations/content/patterns/ai-content-and-disclosure.md)
