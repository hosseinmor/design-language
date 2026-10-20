---
id: design-system.structure
collection: design-language
type: overview
title: Design Language Knowledge Structure
summary: Defines the human- and AI-readable architecture, ownership boundaries, and extension points of the Design Language repository.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.design-language
  - design-system.overview
  - design-system.reference.source-of-truth
---

# Design Language knowledge structure

The repository is organized by decision ownership, not by the tool that happens
to display the decision.

```text
overview/             Intent, scope, architecture
foundations/
  visual/             Visual primitives and models
  content/            Shared language and copy contracts
  interaction/        Cross-component behavior
accessibility/        Normative accessibility guidance
design-system/
  tokens/             Token contracts by family: color, typography, spacing, radius, elevation, motion
  components/         Reusable component decision contracts
  patterns/           Multi-component composition contracts
  templates/          Reusable UI/page templates when approved
product-expression/
  brands/             Approved brand and theme variations
  experiences/        Approved expressive modes when added
playbooks/
  evolve-the-system/  Change the language safely
  apply-the-system/   Use the language in product work
integrations/         Figma, Karbon, Storybook, and source boundaries
assets/               Owned reusable assets
governance/           Ownership and change policy
registry/             Aliases and generated retrieval indexes
ai/                   Routing, retrieval, and semantic evals
schemas/              Machine-readable contracts
tooling/              Validators and future adapters
tests/                Repository quality entry points
```

## Retrieval layers

```text
1. overview/design-language.md
   Global intent and default choices

2. Component or pattern contract
   The smallest reusable decision that answers the task

3. Relevant foundation or accessibility rule
   Loaded only when the contract does not fully answer the question

4. Live source
   Figma for construction, Karbon/Storybook for runtime, Product Knowledge for
   product behavior
```

## Extension rules

- Add a document only when it owns a durable decision.
- Preserve document IDs while paths evolve; register lookup aliases when needed.
- Keep machine-readable contracts next to their human guidance when they express
  the same rule. Keep cross-document AI evals under `ai/evals/`.
- Put adapters and validation code under `tooling/`; never embed runtime services
  in the knowledge corpus.
- A future MCP server reads the registry and queries live sources. It does not
  own or copy their truth.
- Temporary audits, handoffs, screenshots, and migration work stay outside the
  canonical corpus. Promote only their durable decisions into owning documents.
