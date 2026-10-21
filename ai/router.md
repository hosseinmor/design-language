---
id: design-language.ai.router
collection: design-language
type: ai-routing
title: Design Language AI Router
summary: Routes design-language questions to the smallest canonical knowledge area and the appropriate live source.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.design-language
  - design-system.reference.source-of-truth
---

# AI router

| Question | Start here | Verify exact facts in |
|---|---|---|
| Overall design intent | `overview/design-language.md` | Relevant canonical contract |
| Visual design principle | `foundations/visual/` | Figma for live construction |
| Token names, values or role selection | `design-system/tokens/{color,typography,spacing,radius,elevation,motion,layout}/` | Figma for editable values, Code/Storybook for runtime |
| Product language | `foundations/content/` | Product Knowledge for product truth |
| Interaction choice/principle shared across UI | `foundations/interaction/` | Owning component/pattern and Karbon |
| Accessibility requirement | `accessibility/router.md` | Runtime accessibility tests |
| Component design choice, usage or contract | `design-system/components/` | Figma for current visual source; Karbon/Storybook for verified runtime |
| Multi-component composition and behavior (Loading, Confirmation, Notifications, Tour and other patterns) | `design-system/patterns/` | Owning components, Product Knowledge for feature policy, Karbon for runtime |
| Brand or expressive variation | `product-expression/` | Figma variables and themes |
| Design-to-code component identity or implementation parity | `integrations/component-mapping-index.md` | Relevant mapping evidence, registered code package and Storybook build |
| Source-of-truth dispute or documentation ownership | `integrations/source-of-truth.md` | Owning Design Language, Figma, Karbon or Product source |
| Changing the system | `playbooks/evolve-the-system/` | Owning live sources |
| Applying the system | `playbooks/apply-the-system/` | Product Knowledge and live sources |

Never answer product permissions, lifecycle, eligibility, or business-rule
questions from this repository.
