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

## Color Semantics

```text
surface/magic-muted
→ subtle AI card, section, chip, or container

surface/magic-emphasis
surface/magic-emphasis-hover
surface/magic-emphasis-active
→ strong interactive AI action or entry point

fg/magic
→ AI icon, label, sparkle, or inline emphasis

line/magic
→ AI-specific outline/indicator when required by anatomy
```

The component's interaction model still determines which states exist. A passive AI container does not gain Hover or Active merely because Magic Emphasis has those state tokens available.

## Semantic Boundary

Magic means AI capability. It does not replace:

- Brand for product identity or approved conversion moments
- Accent for general chromatic interaction/affordance
- Selected for a component state
- Support for Info/Success/Warning/Error feedback

If an AI feature is also selected, disabled, focused, or in error, compose the relevant component/state semantics rather than using Magic to encode every state.

## Component Composition

Use shared Semantic Color tokens directly where the component anatomy can express the pattern. Do not create an `ai-card/*` or `ai-button/*` Color-token family solely to rename Magic roles.

Component-specific tokens require a stable AI component contract that cannot be represented by the existing Semantic vocabulary.

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

- `../tokens/semantic-tokens.md`
- `../tokens/usage-rules.md`
- `../tokens/jobvision-color-tokens-v4-surface-model.md`
