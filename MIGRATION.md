# Initial migration record

## Source

- Repository: `hosseinmor/product-knowledge`
- Branch: `main`
- Cutoff commit: `6411fcf0656da7f42d41876ee0116a2f02afbd81`
- Migration date: 2026-10-20

Only reusable Design Language material was copied. The source repository was
not modified.

## Intentionally not migrated

- `shared/design-system/handoffs/`: dated development delivery packages
- `shared/design-system/audits/`: dated Figma and token audit snapshots
- `shared/content/contexts/`: product/audience contracts coupled to Product Knowledge
- the two matching product-context eval suites
- `shared/product-standards/`: empty or routing-only Product Knowledge scaffolds
- `ai/` PRD, research, and design-start workflows owned by the development harness
- Jira/PRD templates
- Product Knowledge source registries and their validators
- the previous generated manifest

Durable decisions referenced by the excluded handoffs and audits remain in the
canonical component, token, integration, and accessibility documents migrated
to this repository.

## Migrated with a new role

- generic content evals moved to `ai/evals/content/`;
- the reusable Figma token-audit recipe moved to `tooling/figma/`;
- authoring templates moved to `governance/document-templates/`;
- cross-component experience rules moved to `foundations/interaction/`.
