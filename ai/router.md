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
| Directionality / RTL–LTR layout inheritance, logical placement and mirroring | `foundations/interaction/directionality.md` | Draft awaiting owner review; verify Localization, Accessibility, live Figma and owning components |
| Accessibility requirement | `accessibility/router.md` | Runtime accessibility tests |
| Component design choice, usage or contract | `design-system/components/` | Figma for current visual source; Karbon/Storybook for verified runtime |
| Multi-component composition and behavior (Loading, Confirmation, Notifications, Tour and other patterns) | `design-system/patterns/` | Owning components, Product Knowledge for feature policy, Karbon for runtime |
| Product ↔ Theme relationship, Brand usage, or reviewed Product exception | `product-expression/brands/` | Color contracts, Figma for editable values, owning Product Knowledge for conversions |
| Expressive experience variation | `product-expression/experiences/` | Approved shared usage and Product source; currently TBD |
| Design-to-code component identity or implementation parity | `integrations/component-mapping-index.md` | Relevant mapping evidence, registered code package and Storybook build |
| Source-of-truth dispute or documentation ownership | `integrations/source-of-truth.md` | Owning Design Language, Figma, Karbon or Product source |
| Modifying a reusable Design Language decision | `playbooks/evolve-the-system/` | `governance/change-process.md` and owning live evidence |
| Contribution, approval, maturity, owner or documentation maintenance | `governance/` | `governance/ownership.md`, `governance/change-process.md`, `governance/documentation-maintenance.md` |
| Release, component deprecation or compatibility migration | `governance/` | Follow only reviewed policies; release/deprecation specifics are currently TBD |
| Applying the system | `playbooks/apply-the-system/` | Product Knowledge and live sources |

**Retrieval rule:** This table names discovery locations, not a request to load each directory. For a known topic, open the **smallest owning document** directly; use [Retrieval Contract](retrieval.md) for maturity and source evidence. A directory route may contain draft/scaffold documents: it does not certify them as approved.

Never answer product permissions, lifecycle, eligibility, or business-rule
questions from this repository.
