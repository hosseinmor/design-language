---
id: design-system.experience-rule.contextual-guidance
collection: design-system
type: experience-rule
title: Contextual Guidance
summary: Choose Tooltip, Toggletip, Popover, Coachmark, or Tour based on user intent, initiator, and interaction complexity.
knowledge_state: verified
document_maturity: draft
owner: Design System team
last_reviewed: 2026-09-19
related:
  - design-system.component.tooltip
  - design-system.component.toggletip
  - design-system.component.popover
  - design-system.component.coachmark
  - design-system.pattern.tour
---

# Contextual Guidance

## Purpose

This rule defines how to choose between the Design System's contextual floating guidance and interaction patterns.

It owns **component selection and boundaries**.

Individual component documents own anatomy, visual styling, detailed accessibility, and Figma API.

## Selection Model

Use two questions first:

1. **Who initiates the surface?**
   - the user implicitly through hover/focus;
   - the user explicitly through activation;
   - the product proactively through lifecycle/context.

2. **What is the user's intent?**
   - understand a brief label;
   - learn more;
   - do a small task;
   - discover/onboard;
   - follow an ordered sequence.

## Canonical Roles

| Pattern | Primary intent | Initiator | Trigger | Interactive content | Typical persistence |
|---|---|---|---|---|---|
| Tooltip | Explain briefly | User, implicit | Hover / keyboard focus | No | Ephemeral |
| Toggletip | Learn more | User, explicit | Click / tap / Enter / Space | At most one simple learn-more action | Until dismissed |
| Popover | Do a small contextual task | User, explicit | Click / tap / keyboard activation | Yes | Until task/dismissal |
| Coachmark | Introduce / onboard | Product / lifecycle | Contextual or first-use trigger | One or two guidance actions | Until dismissed/advanced |
| Tour | Guide through ordered concepts | Product or manual start | Tour start | Coachmark navigation | Across multiple steps |

## Decision Rule

Use the smallest pattern that satisfies the intent.

```text
Is the product proactively introducing something?
├─ No
│  ├─ Is the user only getting a brief passive explanation?
│  │  └─ Tooltip
│  ├─ Did the user explicitly ask for contextual explanation?
│  │  └─ Toggletip
│  └─ Does the user need to perform a small contextual task?
│     └─ Popover
└─ Yes
   ├─ Is one contextual introduction enough?
   │  └─ Coachmark
   └─ Are multiple ordered steps necessary?
      └─ Tour
```

Do not choose based only on visual size or the fact that every pattern can look like a floating box.

## Tooltip

Use Tooltip for brief, passive, supplementary information.

Examples:

- visible label for an Icon Button;
- short clarification of a compact control;
- concise nonessential definition.

Tooltip must remain non-interactive.

If the user needs to intentionally request the information on touch, move to Toggletip.

## Toggletip

Use Toggletip when the user explicitly asks to understand something nearby.

Typical trigger:

- info/help Icon Button.

Toggletip may contain:

- optional Title;
- Body;
- one simple learn-more action.

It must not become a mini settings/task surface.

When the content requires several controls or completion of work, move to Popover.

## Popover

Use Popover for a small contextual task or interaction.

Examples:

- compact filter;
- small settings form;
- task-specific controls;
- contextual composition that does not have stronger dedicated semantics.

Popover is generic composition infrastructure.

Before using generic Popover, check whether the content is actually a dedicated Menu, Select, Date Picker, or another specific component.

## Coachmark

Use Coachmark when the **product**, not the user, initiates contextual education.

Examples:

- introducing a newly available feature;
- explaining a meaningful first-use concept;
- calling attention to a changed workflow.

A Coachmark should teach one concept.

Do not use Coachmark repeatedly for ordinary help that the user could request through Toggletip.

Do not use proactive guidance to compensate for unclear persistent UI.

## Tour

Tour is not another visual surface.

Tour is the orchestration of multiple Coachmark steps.

Use Tour only when:

- concepts are meaningfully ordered;
- one Coachmark cannot communicate the necessary guidance;
- each step can remain focused on one target/concept.

Avoid Tours that simply enumerate unrelated features.

## Trigger Boundary

### Hover / Focus

Hover/focus belongs to Tooltip.

Do not open Popover, Toggletip, or Coachmark as ordinary hover surfaces.

### Explicit activation

Click/tap/keyboard activation may open:

- Toggletip for explanation;
- Popover for a task.

The difference is the **intent**, not the trigger.

### Product lifecycle

First-use/contextual proactive triggers belong to:

- Coachmark;
- Tour.

Do not make Tooltip appear automatically as feature-announcement UI.

## Interactive Content Boundary

| Content | Use |
|---|---|
| Text only | Tooltip, Toggletip, or Coachmark depending on initiator |
| Text + one learn-more action | Toggletip |
| Buttons for guidance progression | Coachmark / Tour |
| Input, Checkbox, Select-like control, task CTA | Popover or dedicated component |
| Multiple task controls | Popover or larger surface |
| Long documentation | Persistent help / documentation, not these floating patterns |

## Essential Information

None of these patterns should be the only source of critical information when the user could miss the surface.

Do not hide:

- validation requirements;
- errors;
- mandatory instructions;
- irreversible consequences;
- legal/policy content;
- core state required to finish a task

inside a Tooltip or transient guidance surface.

Use persistent UI when the information must remain available.

## Touch Boundary

Tooltip is not a touch discovery mechanism.

If touch users must be able to request contextual explanation, use Toggletip.

Popover and Coachmark/Tour may support touch when their content and target relationship remain usable in the viewport.

## RTL

All five patterns use logical Start/End semantics.

For anchored floating components:

### Top / Bottom

- Start = right in RTL;
- End = left in RTL.

### Left / Right

- Start = top;
- End = bottom.

Runtime implementations must use logical positioning semantics where possible rather than duplicating physical RTL/LTR variants.

## Visual Family

The components intentionally do not share one identical surface treatment.

### Tooltip

- inverse surface;
- no border;
- no shadow;
- radius 6.

### Toggletip / Popover / Coachmark

- `surface/raised`;
- no border;
- `Shadow/Floating`;
- radius 12.

This distinction helps communicate ephemeral passive labeling vs persistent contextual surface behavior.

## Arrow Policy

Arrow usage is intentionally different across the family:

| Pattern | Arrow policy |
|---|---|
| Tooltip | No arrow |
| Toggletip | Required / always shown |
| Popover | Optional; default `False` |
| Coachmark | Optional property; default `True` |
| Tour | Follows each Coachmark step |

Use an arrow when visual pointing materially clarifies the anchor/target relationship. Do not add one merely to make all floating surfaces visually consistent.

Tooltip is intentionally simplified and relies on proximity/placement rather than a caret. Popover is task-oriented and normally does the same. Toggletip and Coachmark retain stronger anchored pointing because their explanation/guidance is tied to a specific trigger or target.

## Anchor Offset

Anchored contextual surfaces use a default **2px gap** from their trigger or target.

Measure the gap from the visually closest part of the floating surface:

- **No arrow** — 2px from the Surface edge to the trigger/target edge.
- **With arrow** — 2px from the arrow tip to the trigger/target edge.

This applies to Tooltip, Toggletip, Popover, and Coachmark. Tour inherits the rule from each Coachmark step.

The 2px value is the preferred design/runtime offset before collision handling. Runtime may reposition or flip the surface to keep it inside the viewport, but should preserve the 2px anchor gap whenever geometry allows.

Do not add extra arbitrary spacing merely because a component has `Shadow/Floating`; the shadow may visually extend into the gap, but placement geometry is based on the Surface/arrow bounds, not the shadow blur.

## Floating Shadow Rule

`Shadow/Floating` is the shared separation recipe for raised floating surfaces.

It contains:

- a subtle `0 0 0 1px` outline-like first layer;
- two soft elevation layers.

This first layer is intentional so white floating surfaces remain distinguishable on white page backgrounds. It is part of the Floating effect, not a separate component border.

Toggletip, Popover, and Coachmark therefore use `Shadow/Floating` with **no additional explicit border by default**.

## Accessibility Boundary

Every pattern must preserve the semantics of its trigger and purpose.

- Tooltip does not replace accessible naming.
- Toggletip and Popover triggers expose popup state/relationship when applicable.
- Popover content remains keyboard operable and non-modal by default.
- Coachmark/Tour controls remain keyboard operable and dismissible.
- `Escape` provides dismissal for open contextual surfaces where applicable.
- Focus must not be lost after dismissal.

Exact runtime focus algorithms belong to each component/pattern implementation.

## Ownership

This document owns:

- which contextual pattern to choose;
- boundaries between the five patterns;
- trigger/intent taxonomy;
- shared RTL selection semantics.

Component docs own:

- Figma API;
- anatomy;
- visual contract;
- component-specific behavior and accessibility.

Tour owns:

- step sequencing;
- progress;
- next/back;
- exit;
- lifecycle/persistence of the sequence.

## Related

- `../../design-system/components/tooltip.md`
- `../../design-system/components/toggletip.md`
- `../../design-system/components/popover.md`
- `../../design-system/components/coachmark.md`
- `../../design-system/patterns/tour.md`
- `action-hierarchy.md`
- `../../accessibility/focus-management.md`
