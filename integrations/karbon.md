---
id: design-language.integration.karbon
collection: design-language
type: integration
title: Karbon Integration
summary: Defines how the Design Language repository relates to Karbon code and Storybook without duplicating runtime truth.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.reference.source-of-truth
  - design-system.reference.code
  - design-system.reference.storybook
---

# Karbon integration

Karbon code and its Storybook own runtime component APIs, defaults, rendered
states, framework behavior, executable examples, accessibility tests, and
release status. This repository owns the reusable intent and decision contract
that those implementations must satisfy.

## Registration contract

Each mapped component should eventually record:

- stable Design Language document ID;
- Figma component key or node identity;
- Karbon package/export identity;
- Storybook story ID or canonical URL;
- implementation and design maturity;
- last verified revision for each live source.

Until a mapping is verified, mark it unknown. Similar names or visuals are not
proof that Figma and runtime components are equivalent.

## Drift controls

- Contract changes update the owning Design Language document in the same body
  of work as the live-source change.
- Karbon CI should validate registered mappings and expose component metadata
  that can be compared with `registry/manifest.generated.json`.
- Figma audits and Storybook tests produce reports; reports do not become
  canonical knowledge.
- A failed comparison opens work against the owning source. It must not silently
  overwrite another source.
- Human review resolves semantic conflicts; automation detects drift and
  verifies identities.

An MCP adapter may later join the registry with Figma and Karbon data at query
time. It remains a transport layer, not a new source of truth.
