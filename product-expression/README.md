# Product expression

The shared Design System is the default. This section records *intentional, reviewed* Product-level visual/usage differences without copying Theme color values, Figma authoring inventories, component APIs, or Product business rules.

## Find the decision owner

| Question | Document | Maturity |
|---|---|---|
| Product identity vs installed Theme, current intended application mapping, Foundation participation | [Theme Context](brands/theme-context.md) | Reviewed **design-side architecture**, not verified runtime package |
| When Brand may be used in a shared Button hierarchy | [Brand Variants](brands/brand-variants.md) | Draft; conversion candidates are **not approved Product lists** |
| Reviewed Product deviation from a shared Design Language rule | [Product Overrides](brands/product-overrides.md) | Scaffold / TBD; no approved override registered in this document |
| Approved expressive experience modes | [Experiences](experiences/README.md) | Reserved; no mode approved yet |

## Source boundaries

- Semantic Color names and meaning → [Color Semantics](../design-system/tokens/color/semantics.md).
- Exact currently editable Theme/Figma values and variables → [Figma Reference](../integrations/figma.md) and live Figma.
- Generated Theme packages, Code API and deployment → registered Karbon source; [Frontend Token Contract](../integrations/frontend-token-contract.md) and [Theme Initialization](../integrations/theme-initialization.md) are design-side contracts.
- Product-specific permissions, business rules and feature journey → Product Knowledge / Product Walkthrough.

Do not treat a Draft or Scaffold as blanket design approval. See [AI retrieval maturity rules](../ai/retrieval.md).
