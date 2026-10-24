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

Default retrieval order **for a broad new design question**:

```text
overview/design-language.md
→ component or pattern
→ unresolved foundation/accessibility rule
→ exact live-source fact
```

For a **specific, named component, governance document, token or pattern**, retrieve its exact document ID/path **directly**, without preloading the overview or the full Registry. The Manifest is an index, not a mandatory document payload: select candidates by ID/path/topic and read only the selected entries or fields. Follow only edges needed to answer the unresolved question (normally direct `related` links); avoid recursive graph traversal and avoid reading every neighboring document. When a large evidence registry has a narrow lookup index, use the index and ranged reads, not the entire evidence file.

## Existing-decision preservation

Retrieval is a **decision gate**, not only a context-loading optimization.

For Design System design, review, or documentation work, retrieve and reconcile the current internal contract **before** ideation or external benchmarking:

```text
owning Design Language decision on main
→ relevant live Figma construction
→ existing decisions + explicit TBDs + cross-source discrepancies
→ benchmark only unresolved questions or explicit change proposals
→ owner decision
→ Design Language / Figma reconciliation
```

The default assumption is that a mature system already contains decisions. Do not approach an existing component or pattern as a greenfield design problem unless the owning sources explicitly show that it is unowned or unresolved.

Before proposing or applying a change, classify it as exactly one of:

- **preserve** — keep an existing approved decision unchanged;
- **resolve** — answer an explicit TBD/open gap without contradicting approved decisions;
- **reconcile** — bring Figma and Design Language back into agreement without inventing a third contract;
- **change** — intentionally replace an existing decision through the governed change process.

Reviewed/final decisions are constraints during ordinary design work. A benchmark, common industry convention, product analogy, or model preference does not override them. Use external systems to inform unresolved questions or to provide evidence inside an explicit change proposal.

If a proposed direction conflicts with a current reviewed decision, stop treating it as routine design iteration: name the conflict and route it through `governance/change-process.md`.

Before modifying a live source, record the preservation set: which current decisions remain unchanged, which explicit gaps/conflicts are being addressed, and which source owns each affected fact.

If the required owning Design Language document or live Figma source cannot be accessed, do not substitute memory, conversation history, benchmark behavior, or generic best practice for a new system-level decision. Surface the missing evidence and keep the decision unresolved.

Chat history, Linear issues, audit documents, benchmark notes, screenshots, and migration artifacts may explain context or history, but they are not canonical decision sources. When they contain a durable approved decision, reconcile that decision into the owning Design Language document and live Figma source as applicable.

### Resolution and evidence rules

- Resolve a **known ID** first; apply `aliases.yaml` only when the input is an alias. Never construct a fake path, component API, or Storybook ID from a label.
- Distinguish a valid link from **verified identity parity**. A Design Language ID, Figma node and Code export belong to different evidence sources and do not join automatically.
- An absent runtime/Figma source is a **registration/verification gap**, not authority for a guess based on a generated summary.
- Cite the owning document and, for live facts, its source identity/revision or explicit verification date. A historical `last_reviewed` is not proof that a live source was rechecked today.
- The indexed `owner` can be an inherited stewardship default; owner presence does not certify any individual rule or operational shipment.
- Reuse a prior retrieved section in the same workflow if unchanged; keep token/context cost proportional to the actual decision.

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

The currently indexed Manifest does not carry each of these frontmatter fields or rule-level verification provenance. Read the source document metadata when maturity affects a decision; do not infer `scaffold` solely from Manifest `status: draft`.

## Ownership boundaries

A usage pattern does not override a component API or visual specification; a component does not override shared interaction foundations, Accessibility or Product Knowledge. When sources disagree on exact implemented names or runtime behavior, inspect registered live code/Figma sources and report discrepancies rather than guessing.
