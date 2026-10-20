---
id: design-system.product-variation.brand-variants
collection: design-system
type: product-variation
title: Brand Variants
summary: Brand Button uses the active product brand while preserving one shared usage rule.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Brand Variants

## Brand Button

Brand Button uses the active product brand while preserving one shared usage rule.

```text
JobVision Brand Button
→ Jobvision surface/brand mapping
→ Blue

Cando Brand Button
→ Cando surface/brand mapping
→ Yellow
```

A Brand-colored Button is not justified merely because an action is important. Brand is reserved for approved product conversions and product-defining entry points.

Everyday operational actions use Neutral Button hierarchy even when they are the main action in the current context.

## Brand versus Accent

Brand and Accent are separate concepts in v4:

```text
Brand  → product identity + approved key conversion/product moments
Accent → general chromatic interaction/affordance
```

JobVision may map both to the same Blue Primitive family. Cando maps Brand to Yellow and Accent to Blue.

There is no generic Accent Button preset in v4.

## Foreground Override

`fg/on-brand` must resolve independently from the Brand background.

In Cando, foreground must preserve sufficient contrast on the yellow Brand surface. In JobVision, the corresponding Blue surface may require a light foreground.

Final mappings must be revalidated after the Primitive scales are built.

## Product Conversion Lists

Each product should maintain an approved list of Brand Button use cases.

Shared examples that may qualify include:

- Resume submission
- Sign-up
- Primary job-creation entry point
- Package purchase or upgrade
- Demo request
- Start of a defined key product journey

The same action may use different hierarchy by context. A major first-entry “Create job” moment may qualify as Brand, while a repeated “Create job” action in an ATS toolbar is normally operational and Neutral.

## Cando Frequency

Brand Button usage may be rare inside Cando ATS. This is expected. The product does not need persistent yellow Buttons to remain recognizably Cando; Brand color is not a quota.

## Unsupported General Presets

Do not introduce these merely because a product has a Brand color:

- Brand Subtle
- Brand Outline
- Brand Ghost as a general preset
- Generic Accent Button
