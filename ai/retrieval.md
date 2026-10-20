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

## Maturity-aware retrieval and evidence

The generated Manifest's `status` is a **coarse document-level index signal**, not a claim that every sentence in a draft is unreviewed or that a reviewed design is implemented in code. After locating a relevant document, read its frontmatter (`knowledge_state`, `document_maturity`, `design_status`, `last_reviewed`) and its explicit open gaps before using individual decisions.

- **`scaffold` + `unverified`**: a reserved topic and routing aid only. A scope, question or reference is *not* an approved design behavior. Follow linked canonical sources for current decisions.
- **`draft`**: the document may contain established, Figma-reviewed design decisions alongside proposals and unresolved implementation details. Do **not** discard all of its content merely because Manifest says `draft`; identify which claims are supported by owner review, verified source references, explicit decisions and current live sources. Mark unresolved claims as pending.
- **`reviewed` / `final`**: a reviewed design-side contract within its declared scope. This does **not** prove runtime implementation, testing or Product eligibility; verify those with their owners.
- A file can be `knowledge_state: verified` but `document_maturity: draft`: evidence for some decisions exists, while other work is unfinished. Do not upgrade the whole file to final or downgrade every statement to conjecture.
- Preserve each answer's provenance and scope. If a draft statement conflicts with the owning current contract or verified live source, flag the conflict; do not silently pick by status alone.

The currently indexed Manifest does not carry each of these frontmatter fields. Read the source document metadata when maturity affects a decision; do not infer `scaffold` solely from Manifest `status: draft`.

## Ownership boundaries

A usage pattern does not override a component API or visual specification; a component does not override shared interaction foundations, Accessibility or Product Knowledge. When sources disagree on exact implemented names or runtime behavior, inspect registered live code/Figma sources and report discrepancies rather than guessing.
