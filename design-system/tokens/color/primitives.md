---
id: design-system.token.primitive-tokens
collection: design-system
type: token
title: Primitive Tokens
summary: Documents the provisional Color Primitive inventory; exact palette scales are not yet validated.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Primitive Tokens

> Status: draft
> Value status: partial — final opaque 50–950 scales remain open

## Color

Primitive color scales are named by hue/value rather than semantic meaning. In the target runtime architecture, Primitive Color is Theme-local implementation detail rather than a shared Product-facing contract.

Current opaque families:

```text
palette/neutral/*
palette/blue/*
palette/yellow/*
palette/red/*
palette/purple/*
palette/green/*
palette/emerald/*
palette/orange/*
```

Product-specific public Primitive families remain prohibited. A Theme may define the local Primitive values it needs, but Product code must not depend on Theme-local Primitive identities. Product identity is expressed through shared Semantic roles whose values are supplied by the selected Theme.

Current brand color anchors:

```text
JobVision blue  → #0053FF
Cando yellow    → #FFC400
```

These anchors do not yet define a numbered scale step. The final 50–950 opaque values remain an open decision and will be built as a separate palette pass.

The `green/*` versus `emerald/*` inventory also remains open until that pass; do not remove either family from implementation solely from this draft.

A Theme-local Primitive palette may feed multiple Semantic or Component roles. For example, one Blue ramp may feed Brand semantics, Accent, Link, Info, and categorical Blue without merging those meanings.

### Alpha primitives

Alpha primitives store direct RGBA values and support transparent interaction, overlay, and loading treatments:

| Primitive variable | Direct value |
|---|---|
| `color/black-alpha/4` | `rgba(0, 0, 0, 0.04)` |
| `color/black-alpha/8` | `rgba(0, 0, 0, 0.08)` |
| `color/black-alpha/40` | `rgba(0, 0, 0, 0.40)` |
| `color/white-alpha/8` | `rgba(255, 255, 255, 0.08)` |
| `color/white-alpha/12` | `rgba(255, 255, 255, 0.12)` |

See `aliases.md` for Appearance-specific alias targets and unresolved mappings.

