---
id: design-system.foundation.radius
collection: design-system
type: foundation
title: Radius
summary: Defines the canonical Small/Medium/Large radius scale shared by controls, surfaces, and fully rounded shapes.
knowledge_state: canonical
document_maturity: reviewed
owner: Design System team
last_reviewed: '2026-10-19'
related:
  - design-system.reference.tailwind
---

# Radius

## Model

Radius uses a deliberately small **size scale**. Component specs decide which approved size applies; the Foundation does not encode component anatomy into token names.

The canonical numeric scale is **3 → 6 → 12**. `None` and `Full` are boundary behaviors, not additional steps in that progression.

## Canonical scale

| Token | Figma variable | Value | Typical use | Tailwind-facing name |
|---|---|---:|---|---|
| None | `0px · None` | 0px | Square edges and explicit no-radius cases | `rounded-none` |
| Small | `3px · Small` | 3px | Compact detail geometry when a component spec explicitly needs less rounding than Medium | `rounded-small` |
| Medium | `6px · Medium` | 6px | Standard controls and compact surfaces such as Button, Input, Select, Search, Tooltip and Menu Item | `rounded-medium` |
| Large | `12px · Large` | 12px | Card, Menu shell, Popover, Toggletip, Coachmark, Modal and other independent/floating surfaces | `rounded-large` |
| Full | `Full` | 9999px / fully rounded behavior | Tag, Chip, Avatar, Toggle track, circular/pill controls | `rounded-full` |

`Full` is a shape behavior, not the next step in the numeric scale.

## Usage rules

- Use only `Small`, `Medium`, or `Large` for ordinary rounded geometry unless a component has an explicitly approved exception.
- `Medium` is the default radius for standard interactive controls.
- `Large` is the default for independent and floating surfaces, including Modal. A larger Modal does **not** receive a larger radius.
- `Small` is intentionally uncommon. Do not choose it merely to create another visual tier.
- Parent/child containment may use a larger approved radius on the parent than on nested controls. Example: a `Large` container may contain `Medium` items.
- Do not introduce a dedicated intermediate Group radius. Existing 8px Group usage migrates to `Large = 12px`.
- Do not use 20px as a shared Design System radius. Existing 20px large-surface usage migrates to `Large = 12px`.
- Use `Full` only when the component is intentionally pill-shaped or circular.
- Avoid raw/arbitrary radius values when an approved scale value expresses the intended geometry.

## Tailwind boundary

Product Tailwind may expose the approved scale names directly as `rounded-*` utilities. Tailwind's default radius values are not the Design System source of truth.

The Design System package itself does not depend on Tailwind; Product tooling consumes a generated, framework-agnostic radius artifact. Exact preset/config mechanics remain Frontend-owned.

## Migration

The previous role-based and intermediate Figma variables remain deprecated only to preserve legacy bindings during migration:

| Deprecated variable | Canonical replacement |
|---|---|
| `Deprecated · 6px Control` | `6px · Medium` |
| `Deprecated · 12px Surface` | `12px · Large` |
| `Deprecated · 8px Group` | `12px · Large` |
| `Deprecated · 20px Large surface` | `12px · Large` |
| `Deprecated · Legacy 12px` | `12px · Large` |

New or actively maintained components must bind to the canonical variables rather than the deprecated set.

As of 2026-10-19, the five deprecated Radius variables are marked `hiddenFromPublishing=true` and their scopes are empty in the live Figma source, to prevent new authoring selection. They were **not deleted**, renamed or numerically changed: existing bindings and published consumers remain intact pending migration. Confirm each legacy binding is replaced in its owning source component before considering removal. See [Figma Component Token Compliance](../../integrations/figma-token-compliance.md) and the 2026-10-19 audit.
