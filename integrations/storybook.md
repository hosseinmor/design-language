---
id: design-system.reference.storybook
collection: design-system
type: reference
title: Storybook Reference
summary: Defines Storybook as the executable component reference when registered and records the current absence of a verified JV Design System Storybook source.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-09-13'
related:
  - design-system.reference.source-of-truth
  - design-system.reference.code
  - design-system.reference.component-mapping
---

# Storybook Reference

Storybook is the preferred live source for **runnable component examples and executable UI evidence** when a verified Design System Storybook is registered.

## Current registration status

> Verified JV Design System Storybook: **not yet registered in Design System Knowledge**.

No Storybook URL, deployment, story structure, or current coverage map is currently recorded as an owning source.

This is an integration gap, not permission to infer executable behavior from Figma or Markdown.

## What Storybook should own

When registered, Storybook should expose or link to:

- rendered component states/variants;
- realistic composition examples;
- interactive controls tied to actual component APIs;
- interaction tests;
- accessibility test results/configuration where available;
- responsive/theme scenarios where relevant;
- version/build identity corresponding to shipped code.

Storybook does not replace Design System Knowledge for semantic usage rules, and it does not replace Figma for editable visual construction.

## Required source registration

Frontend should provide or confirm:

```text
Storybook URL/deployment
Owning repository/package
Story naming/taxonomy
Build/version relationship to the package
Current component coverage
Interaction-test coverage
Accessibility-test coverage
Theme/Product switching support
Canonical story IDs or stable URLs for mapping
```

## AI rule while unregistered

Until Storybook is registered:

- do not describe a state as runnable merely because it exists in Figma;
- do not claim interaction/a11y tests exist without the test source;
- do not infer runtime defaults from component examples in documentation;
- use the Code source for exact API when available;
- report executable/runtime evidence as unavailable when it is required.

## Future mapping role

Once Storybook is registered, `component-mapping.md` should map each reviewed Design System component to a stable Storybook story or docs entry where possible.
