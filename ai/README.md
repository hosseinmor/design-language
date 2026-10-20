# AI access

- `router.md` chooses the owning knowledge area.
- `retrieval.md` defines minimum-context retrieval and source boundaries.
- `evals/` contains semantic regression cases, not product runtime fixtures.

AI should read generated registry files and canonical documents. It should not
treat audit reports, handoffs, chat history, or generated summaries as sources
of truth.
