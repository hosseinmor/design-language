---
id: design-system.product-variation.brand-variants
collection: design-system
type: product-variation
title: Brand Variants
summary: Draft cross-product Brand action usage guidance, separation from Accent, and the need for explicit Product approval of conversion entry points.
knowledge_state: unverified
document_maturity: draft
related:
  - design-system.product-variation.theme-context
  - design-system.token.semantic-tokens
  - design-system.token.usage-rules
  - button
---

# Brand Variants

> **Draft scope:** Shared Brand-selection intent is documented here, but the **Product-specific list of approved conversion actions is not registered** in this Design Language document. The candidate examples below are not approvals.

## Product Brand Button meaning

Brand Button adopts the selected Theme's **Semantic Brand roles** while preserving **one shared usage rule**. Its role is Product identity or an explicitly approved key conversion/product-defining entry point, **not** a synonym for the most important action on a page.

For example, a Product's everyday `Save`, `Continue`, and routine ATS operations normally follow the Neutral operational hierarchy, even if they are the primary action in their immediate task. The same action label can have different placement/importance in a genuinely distinct, reviewed entry flow.

The [Button component](../../design-system/components/button.md) owns the actual available Button Styles, hierarchy, variants, and component-level behavior. Do not define a second set of Styles here.

## Brand versus Accent

**Brand** expresses Product identity and specifically approved conversion moments; **Accent** expresses general chromatic interaction or affordance. A Theme may resolve both through a common color family without merging their meaning.

The [Color Semantics](../../design-system/tokens/color/semantics.md) and [Color Usage](../../design-system/tokens/color/usage.md) documents own role names and restrictions, including the absence of a generic Accent Button Style. Current Color/Brand alias mappings must be checked against Figma rather than repeated as a second hue/value catalog here.

A Brand background requires the appropriate independently resolved `fg/on-brand` foreground with sufficient contrast. Exact per-Theme values and their validation belong to Color/Figma and Accessibility; this document does not certify Light/Dark contrast or Primitive mappings.

## Product conversion candidates — **not an approved list**

Possible categories to evaluate with their Product owner include:

- Resume submission
- Sign-up
- Key job-creation entry point
- Package purchase or upgrade
- Demo request
- Entry to a core Product journey

These examples do **not** make Brand mandatory or approved at every occurrence. A major campaign/entry placement may qualify where a routine operational toolbar action does not. Record approval in the owning Product Knowledge or an explicitly reviewed Product-specific variation record; do not infer it from this list.

## Cando usage

Cando can legitimately have very few Brand-colored Buttons inside its operational ATS workflows. Brand usage is not a quota; the Product's Theme still carries its visual identity outside Brand Button frequency.

## Review boundary

- A Product-specific Brand usage decision needs an identified owner, task context and reason for a conversion/identity exception.
- A different value for `surface/brand` is a Theme mapping, **not** a Product Override.
- Do not create general Brand Subtle/Outline/Ghost or Accent Button presets solely to expand the Brand family; new component API Styles require an explicit shared Button review.
- Product permissions and feature eligibility live in Product Knowledge, not here.

**Open:** Confirm each Product's actual approved Brand Button placements and links to feature owners. No current live Figma or Karbon parity verification is implied.
