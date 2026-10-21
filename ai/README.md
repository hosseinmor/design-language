# AI access

- `router.md` chooses the owning knowledge area.
- `retrieval.md` defines minimum-context retrieval and source boundaries.
- `evals/` contains semantic regression cases, not product runtime fixtures.

AI should use the generated Registry **as a lookup index**, not load its full JSON files into the prompt by default. Read the smallest owning document and only necessary `related` references; live-source registration and evidence come from their actual owners. Do not treat audit reports, handoffs, chat history, eval fixtures or generated summaries as sources of truth.

The `evals/` fixtures are **not currently executed as an AI semantic evaluation suite in CI**. Existing CI validates registry freshness, links, the component mapping index and the named deterministic accessibility/content contracts; green CI is not a claim that AI answered every semantic case correctly.
