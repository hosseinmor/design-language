# Design Tokens

This directory organizes Design Language token contracts by foundation type. Each family has a stable documentation home, even when its catalog is not yet approved.

| Family | Token document | Design principles and usage |
|---|---|---|
| Color | [Color contracts](color/README.md) | [Color foundation](../../foundations/visual/color.md) |
| Typography | [Typography catalog](typography/catalog.md) | [Typography foundation](../../foundations/visual/typography.md) |
| Spacing | [Spacing catalog](spacing/catalog.md) | [Spacing foundation](../../foundations/visual/spacing.md) |
| Radius | [Radius catalog](radius/catalog.md) | [Radius foundation](../../foundations/visual/radius.md) |
| Elevation | [Elevation catalog](elevation/catalog.md) | [Elevation foundation](../../foundations/visual/elevation.md) |
| Motion | [Motion catalog — TBD](motion/catalog.md) | [Motion foundation — TBD](../../foundations/visual/motion.md) |
| Layout / Responsive | [Layout catalog](layout/catalog.md) | [Layout foundation](../../foundations/visual/layout.md) and [Responsive guideline](../../foundations/visual/responsive-layout/guideline.md) |

**Boundary:** The token document owns approved names/recipes; the Foundation owns design principles, guidance and accessibility applications. Figma owns live editable values and construction, while code/Storybook owns implemented behavior and generated artifacts. Do not manually mirror live values in multiple documents.

For Theme-package runtime contracts, see [Frontend Token Contract](../../integrations/frontend-token-contract.md). For Product↔Theme selection, see [Theme Context](../../product-expression/brands/theme-context.md).

Human-facing README files are not indexed by the current AI manifest generator. Use [AI Router](../../ai/router.md) for machine retrieval.
