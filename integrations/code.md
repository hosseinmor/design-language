---
id: design-system.reference.code
collection: design-system
type: reference
title: Code Reference
summary: Operational boundary for Design System runtime code sources; the real repository/package is not yet registered in Design System Knowledge.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-13'
related:
  - design-system.reference.source-of-truth
  - design-system.reference.component-mapping
  - design-system.reference.storybook
---

# Code Reference

Code is the owning live source for **implemented runtime API and behavior** when a verified Design System implementation source is registered.

## Current registration status

> Runtime Design System source: **not yet registered in Design System Knowledge**.

The currently connected GitHub sources do not provide an identified JV Design System implementation repository/package that can be verified as the owning runtime source.

Do not substitute the internal Product Knowledge site, Figma component/property names, historical Carbon references, Tailwind guidance prose, or product application code for the missing runtime source.

## Facts the code source must own

Once registered, Code owns exact implemented facts such as:

- package/module name and import path;
- component selector/API name;
- props/inputs/outputs and types;
- defaults;
- supported states and variants;
- DOM/ARIA implementation;
- token consumption;
- runtime Product/Appearance wiring;
- release/version status;
- deprecated APIs;
- actual test/build integration.

Design System Knowledge should retain the durable contract and source pointer, not duplicate generated API tables.

## Required source registration

Frontend should provide or confirm:

```text
Repository
Package / library name
Default/release branch
Package entry point
Component source locations
Token canonical/source pipeline
Generated token outputs
Build/publish pipeline
Version/release strategy
Unit/integration/a11y test locations
Storybook relationship
```

After registration, update this document with links/pointers and keep exact APIs in the owning code source.

## AI rule while unregistered

Until the runtime source is registered:

- do not infer component prop names from Figma properties;
- do not infer defaults or supported runtime states from screenshots;
- do not claim a Figma variant exists in code;
- do not claim a component is shipped because it exists in Figma;
- use Design System Knowledge only for semantic/usage rules;
- state that exact runtime implementation is unverified when it materially affects the answer.

## Known gaps

- owning repository/package not registered;
- token build pipeline not registered;
- release/version source not registered;
- component API source not registered;
- implementation test locations not registered;
- Figma ↔ code mapping mechanism not registered.
