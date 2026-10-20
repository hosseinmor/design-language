---
id: design-system.foundation.color
collection: design-system
type: foundation
title: Color
summary: Design principles for using color, visual emphasis, perception, and accessibility; detailed token contracts live in tokens/color.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.token.architecture
  - design-system.token.semantic-tokens
  - design-system.token.component-tokens
  - design-system.accessibility.color-and-contrast
  - design-system.reference.source-of-truth
last_reviewed: '2026-09-14'
---

# Color

## Design intent

Color establishes visual hierarchy, helps people distinguish interactive surfaces and communicates Product identity and feedback. Use color purposefully: an element should gain visual emphasis because of its function, not because an arbitrary hue is available.

## Visual principles

- Start with the neutral surface hierarchy; apply chromatic emphasis only where it clarifies interaction, Product identity, assistance, or feedback.
- Prefer consistent emphasis within a workflow. Multiple saturated competing surfaces reduce scannability.
- Do not treat matching hues as matching meaning: a Brand action, a selected control, an AI feature, and an error may require different semantic roles.
- Use typography, shape, layout and language along with color. Do not make color the only perceivable carrier of state.
- Choose elevation and contrast in context: actual foreground/background and control state pairs matter more than isolated swatches.

## Accessibility

WCAG 2.2 AA is the baseline. Validate actual rendered pairings and focus indicators in supported appearance and product contexts; see [Color and Contrast](../../accessibility/color-and-contrast.md) for normative acceptance criteria. This foundation intentionally does not reproduce contrast thresholds or token-value tables.

## Where color contracts live

- [Color Token Architecture](../../design-system/tokens/color/architecture.md) — ownership and layering.
- [Color Semantics](../../design-system/tokens/color/semantics.md) — official role meanings (Surface, Foreground, Line, Brand, Accent, Magic, Danger, Support).
- [Color Token Usage](../../design-system/tokens/color/usage.md) — selecting and composing tokens for states and components.
- [Color Token Mappings](../../design-system/tokens/color/aliases.md) — documented Figma mapping snapshot; Figma remains the exact editable source.
- [Color Component Tokens](../../design-system/tokens/color/component-tokens.md) — approved component-owned exceptions.
- [Theme Context](../../product-expression/brands/theme-context.md) — Product vs Theme selection and Appearance.

## AI routing

For a design-principle question, start here. For a specific token name, role, alias or implementation question, go directly to its owning document above. Do not load this Foundation and the entire Color catalog by default.
