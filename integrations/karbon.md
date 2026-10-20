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

## Documentation split

| Knowledge or evidence | Owning source |
|---|---|
| When to use/not use a component; design principles; visual/semantic decisions | Design Language |
| Shared normative accessibility requirements and UI-content guidelines | Design Language |
| Figma masters, variants, token bindings, presentation and visually editable assets | Figma |
| Actual runtime selectors, inputs/outputs, defaults, rendered states, keyboard/DOM/ARIA mechanics and supported overrides | Karbon code and its versioned technical documentation |
| Executable examples, test runs, a11y test configuration and measured coverage | Storybook plus associated code/CI |
| Product-specific state, permission, eligibility, persistence, workflow | Product Knowledge / Product Walkthrough |

The Karbon repository **may carry component technical documentation and accessibility implementation notes alongside source code and Storybook**. That is desirable: developers can maintain behavior, tests and reference stories in the same PR. Those technical documents must **link back** to the owning shared usage, content, semantic and normative accessibility contracts in Design Language instead of creating independently editable competing rules.

Do not require byte-for-byte duplication between repositories. Prefer stable document IDs, versioned links and narrow summaries. A mismatch is tracked as drift until reviewed.

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

1. **Identify owner and change class.** Is this a design/semantic decision, a Figma construction change, an implemented API/behavior change, or a Product-specific policy?
2. **Review the owner.** The Design System owner approves semantic/normative changes; Frontend approves executed runtime changes; Product owners approve feature policies.
3. **Link the counterpart work.** Where the change affects another live source, create or update the associated Figma/Karbon/Design Language task or PR and identify whether it is `planned`, `design-approved`, `runtime-implemented` or `verified-in-parity`.
4. **Record evidence.** For a component mapping, keep stable Design Language ID, Figma master key/node, code export/version/commit, Storybook story ID/build and verification date. `Unknown` is better than a guessed match.
5. **Check and reconcile.** Karbon CI should eventually compare registered mappings and expose API/story metadata. This is a **target capability**, not an existing validated automation. Figma audits and Storybook tests produce evidence; they do not auto-write canonical decisions.
6. **Close only after relevant verification.** A design-complete component need not be runtime-shipped, and a runnable story does not certify that semantic usage or accessibility obligations are met.

Changes should be coordinated within the same delivery workflow where possible; GitHub/other repositories do not offer one cross-repository atomic merge. A failed comparison opens work against the owning source and must never silently overwrite it.

An MCP adapter may later join the registry with Figma and Karbon data at query
time. It remains a transport layer, not a new source of truth.
