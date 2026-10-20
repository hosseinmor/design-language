# Design Language repository instructions

## Purpose

This repository is the canonical decision layer for the shared JobVision and
Cando design language. Prefer repository evidence over assumptions.

## Source boundaries

- Keep reusable visual, content, interaction, accessibility, component,
  pattern, and product-expression rules here.
- Keep product concepts, business rules, permissions, states, and feature flows
  in Product Knowledge.
- Keep exact runtime APIs, defaults, rendered behavior, executable examples,
  and implementation tests in Karbon code and Storybook.
- Keep editable visual construction, component properties, and variables in
  Figma.
- Keep end-to-end product-development orchestration in the Product Development
  Harness. This repository owns only its two domain-local playbooks.

Do not turn temporary handoffs, dated audits, migration logs, issue notes, or
generated reports into canonical guidance. If a temporary artifact contains a
durable decision, update the owning canonical document and leave the artifact
outside the indexed corpus.

## Working rules

- Start at `ai/router.md` for task routing and `ai/retrieval.md` for retrieval
  behavior.
- Change the smallest owning document; do not duplicate the same rule across
  sources.
- Preserve stable document IDs. Use `registry/aliases.yaml` when an old lookup
  name must continue resolving.
- Do not hand-edit `registry/manifest.generated.json` or
  `registry/graph.generated.json`; regenerate them with
  `python tooling/generate_manifest.py generate`.
- Run repository validators after moving or changing indexed guidance.
- Treat `assets/` as canonical only when the asset has an owner and a documented
  source. Do not store screenshots or temporary exports there.
- An MCP server, if introduced, is an adapter over the registry and live
  sources; it must not become a second knowledge source.
