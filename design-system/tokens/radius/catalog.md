---
id: design-system.token.radius.catalog
collection: design-system
type: token
title: Radius Token Catalog
summary: Reviewed approved radius tokens, design values, Figma variables, and code names.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.foundation.radius
---

# Radius Token Catalog

This catalog owns the numeric radius scale and its token identifiers. Figma owns editable variables; code owns the runtime adapter.

## Canonical scale

| Token | Figma variable | Value | Typical use | Tailwind-facing name |
|---|---|---:|---|---|
| None | `0px · None` | 0px | Square edges and explicit no-radius cases | `rounded-none` |
| Small | `3px · Small` | 3px | Compact detail geometry when a component spec explicitly needs less rounding than Medium | `rounded-small` |
| Medium | `6px · Medium` | 6px | Standard controls and compact surfaces such as Button, Input, Select, Search, Tooltip and Menu Item | `rounded-medium` |
| Large | `12px · Large` | 12px | Card, Menu shell, Popover, Toggletip, Coachmark, Modal and other independent/floating surfaces | `rounded-large` |
| Full | `Full` | 9999px / fully rounded behavior | Tag, Chip, Avatar, Toggle track, circular/pill controls | `rounded-full` |

`Full` is a shape behavior, not the next step in the numeric scale.
