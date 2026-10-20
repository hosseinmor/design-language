---
id: design-system.experience-rule.action-hierarchy
collection: design-system
type: experience-rule
title: Action Hierarchy
summary: Every action group should have one clear visual leader.
knowledge_state: unverified
document_maturity: draft
related: []
---

# Action Hierarchy

## Principle

Every action group should have one clear visual leader.

Only one action in a group may use the strongest visual presence:

- Brand
- Primary
- Danger Filled

All other actions must be at least one level lower.

## Recommended Combinations

| Situation | Combination |
|---|---|
| Brand conversion CTA with exit or supporting information | Brand + Ghost |
| Brand conversion CTA with an independent alternative | Brand + Tertiary |
| Operational action with Cancel | Primary + Ghost |
| Operational action with a valid alternative | Primary + Tertiary |
| Two important operational paths with clear hierarchy | Primary + Secondary |
| Final destructive confirmation with Cancel | Danger Filled + Ghost |

## Limited Combinations

Brand + Secondary and Primary + Secondary are allowed, but require caution because two filled Buttons may compete visually.

Brand and Primary must not appear as equal competing actions in the same action group.

## Three Actions

Keep an action group to two Buttons whenever possible.

When three actions are necessary:

- Main action → Brand, Primary, or Danger Filled
- Supporting action → Tertiary or Secondary
- Exit or third action → Ghost, visually separated from the first two

Example:

```text
[Submit request] [Save draft]                    Cancel
```

## Brand Is Not Generic Primary

Brand is reserved for approved product conversions and product-defining entry points. It is not another name for the most important Button on a page.

Everyday operational work such as Save, Confirm, Continue, Change status, or Add candidate normally uses Primary or a lower Neutral treatment even when it is the most important current action.

Low Brand frequency in dense operational UI such as Cando ATS is expected.

## Context Convention

In dense tool-oriented interfaces such as ATS, Tertiary is commonly used for independent neutral actions.

In editorial and consumer interfaces, Secondary is more common for medium-emphasis standalone actions.

The nature of the control still takes priority:

- Dropdown, filter, toolbar → Tertiary
- Medium-emphasis standalone action → Secondary
- Exit or low-emphasis operation → Ghost

## Scope

This document owns hierarchy across action groups.

Preset meaning and token mapping remain in `../../design-system/components/button.md`.

Placement inside specific patterns belongs in:

- `../../design-system/patterns/multi-step-flow.md`
- `../../design-system/patterns/confirmation.md`
- `../../design-system/patterns/destructive-actions.md`
