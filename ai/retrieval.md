---
id: design-language.ai.retrieval
collection: design-language
type: ai-routing
title: Design Language Retrieval Contract
summary: Defines minimum-context retrieval, identity resolution, conflict handling, and future MCP behavior.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-language.ai.router
  - design-system.reference.source-of-truth
---

# Retrieval contract

1. Resolve aliases through `registry/aliases.yaml`.
2. Find candidate documents in `registry/manifest.generated.json`.
3. Load the smallest owning document and follow only relevant graph edges from
   `registry/graph.generated.json`.
4. Query live Figma, Karbon/Storybook, or Product Knowledge only for facts those
   sources own.
5. Preserve unknowns and conflicts; do not synthesize a false merged truth.

Default retrieval order:

```text
overview/design-language.md
→ component or pattern
→ unresolved foundation/accessibility rule
→ exact live-source fact
```

Future MCP tooling should expose registry lookup and live-source joins. It must
return provenance, verification state, and source timestamps, and must never
write generated observations back as canonical rules without review.
