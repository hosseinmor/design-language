---
id: design-system.pattern.tour
collection: design-system
type: pattern
title: Tour
summary: Tour orchestrates an ordered sequence of Coachmark steps for contextual onboarding or feature guidance.
knowledge_state: verified
document_maturity: draft
related:
  - design-system.component.coachmark
  - design-system.experience-rule.contextual-guidance
---

# Tour

## Purpose

Tour is a multi-step contextual guidance pattern built from the canonical Coachmark component.

Tour is **not** a separate floating visual component.

It owns sequencing, progress, navigation, targeting, lifecycle, persistence, and exit behavior across multiple Coachmark steps.

## When to Use

Use Tour when:

- multiple concepts must be introduced in a meaningful order;
- each concept is best explained next to a specific product target;
- a single Coachmark would be insufficient;
- users benefit from seeing progression through the guidance.

Typical uses:

- first-use walkthrough of a meaningful workflow;
- introduction of several related parts of a newly launched capability;
- optional contextual product education started automatically or manually.

## When Not to Use

Do not use Tour when:

- one Coachmark is sufficient;
- the steps are unrelated feature announcements;
- the content is essential to successfully complete the actual task and should instead be part of the task UI;
- the Tour would interrupt a high-frequency workflow without clear value;
- the experience can be learned through clear persistent UI;
- the sequence is so long that it becomes documentation.

Avoid turning Tour into a mandatory training gate.

## Building Block

Each visible step uses `Coachmark / Default`.

Tour must not create a second visual Coachmark implementation.

Tour controls the Coachmark properties for each step:

- target;
- Side / Align;
- Title;
- Description;
- Actions;
- Progress;
- Progress text;
- Dismiss;
- Arrow.

## Step Model

Each step should contain one primary teaching concept.

Conceptual model:

```text
Tour
- id
- eligibility
- steps[]
  - target
  - title
  - description
  - placement preference
  - action labels
- currentStep
- seen/completed state
```

Exact runtime schema is implementation-owned.

## Actions

### First step

A first step may use one primary action when Back is unnecessary.

Example:

```text
بعدی
```

### Middle steps

Middle steps normally use two actions:

- Primary / Next on the right in RTL;
- lower-emphasis / Previous to its left.

Example:

```text
[بعدی]  قبلی
```

### Final step

The final primary action should communicate completion.

Examples:

```text
تمام
متوجه شدم
شروع کار
```

Previous may remain available when moving backward is useful.

Do not use a generic `Next` label on the final step when the Tour is ending.

## Dismiss / Exit

Tours should normally be dismissible.

The Coachmark Dismiss control exits the **Tour session**, not merely the current step.

Do not close one step and silently advance to the next when the user intentionally dismisses the Tour.

If the product supports restarting the Tour later, expose that through an appropriate Help/Guidance entry point; do not make restart behavior part of Coachmark itself.

## Progress

For multi-step Tour, set `Progress=True` unless there is a deliberate reason not to expose sequence position.

Use a concise current/total format.

Example:

```text
۲ از ۴
```

Production Progress must be derived from Tour state.

Do not manually maintain inconsistent progress text per screen.

Static Figma flows and isolated Storybook stories may hard-code representative progress values for demonstration only. Such examples do not define the production state model.

## Targeting

Each step must have a meaningful target or a deliberate non-targeted presentation defined by the product pattern.

When the target is unavailable because of permissions, responsive layout, state, or feature eligibility:

- do not render an orphaned caret pointing to empty space;
- skip the step when the concept no longer applies; or
- adapt to a valid alternative target/presentation.

Target resolution belongs to runtime.

## Placement

Coachmark supplies Side and Align preferences.

Runtime collision handling may flip/reposition a step to remain visible.

RTL logical Start/End must be preserved.

The Tour must not require designers to author separate physical RTL/LTR step variants.

## Lifecycle and Eligibility

Tour initiation is product-owned.

Possible entry conditions include:

- first relevant use;
- first visit after a meaningful release;
- explicit user selection from Help;
- product-specific eligibility rules.

Avoid triggering solely because a page was opened if the guidance is not relevant at that moment.

### Persistence

Runtime should distinguish states such as:

- never started;
- started / interrupted;
- completed;
- dismissed.

The exact persistence policy is product-specific.

Do not encode these states as Coachmark visual variants.

## Focus and Keyboard

All Coachmark actions must be keyboard operable.

Tour must provide:

- keyboard access to Next / Previous / Finish;
- keyboard access to Dismiss;
- `Escape` exit where appropriate;
- sensible focus after step transitions;
- sensible focus restoration when Tour exits.

The default Tour is not a modal focus trap.

Exact focus movement between target and Coachmark must be validated in runtime accessibility testing.

## Spotlight / Backdrop

Spotlight, target highlighting, and backdrop behavior are Tour/runtime concerns.

They are intentionally not properties of the base Coachmark component.

If a spotlight is used:

- it must not hide essential context needed to understand the target;
- it must not make unrelated keyboard-focusable content confusingly reachable behind an apparently modal layer;
- modal vs non-modal behavior must be explicit.

No canonical spotlight visual contract is currently locked.

## Scrolling

When a target is outside the viewport, runtime may scroll the target into view before positioning the Coachmark.

Do not position a Coachmark against an off-screen target.

Scrolling must avoid disorienting jumps where possible and respect reduced-motion preferences.

## Responsive / Mobile

A Tour step may use the anchored Coachmark geometry only while:

- the target relationship remains understandable;
- Coachmark fits within the viewport;
- controls retain usable target sizes.

When those conditions fail, use a larger responsive guidance presentation rather than shrinking the Coachmark below its component contract.

The exact mobile alternate presentation remains product/runtime-owned.

## Analytics

Tour analytics may track:

- started;
- step viewed;
- next;
- previous;
- dismissed;
- completed.

Analytics must not become visual component properties.

Use analytics to evaluate whether the Tour improves successful feature discovery rather than optimizing solely for Tour completion.

## Content Guidelines

Each step should answer one focused question.

Prefer:

- short Title;
- one concise Description;
- clear Next/Finish action.

Avoid:

- several unrelated features in one step;
- long product documentation;
- internal implementation terminology;
- promotional copy without contextual value.

A Tour should be shorter than the product team initially wants.

## Accessibility QA

Verify:

- every step can be reached and completed with keyboard;
- Dismiss is available and has an accessible name;
- Escape behavior is consistent;
- Progress is understandable;
- target relationship is not conveyed only through the caret;
- focus is not lost between steps;
- focus is restored appropriately after exit;
- off-screen targets are handled safely;
- skipped/unavailable targets do not produce broken steps;
- reduced-motion preferences are respected when scrolling/repositioning.

## Figma Authoring

Do not create a `Tour` component set duplicating Coachmark visuals.

Represent Tour flows in product designs by placing instances of `Coachmark / Default` in their step contexts.

Use:

- `Actions=One` or `Two` as appropriate;
- `Progress=True`;
- correct `Progress text`;
- Side / Align preferences;
- Dismiss according to the product Tour policy.

The actual target, sequence, and state transitions belong to the product flow/design and runtime.

## Open Runtime Items

Runtime / Storybook source is currently unregistered.

Still to verify with implementation:

- exact Tour state API;
- persistence storage;
- target resolver;
- collision library/strategy;
- focus movement algorithm;
- scroll behavior;
- spotlight/backdrop implementation;
- analytics hooks;
- mobile alternate presentation.

These open implementation details do not change the component taxonomy.

## Related

- `../components/coachmark.md`
- `../components/tooltip.md`
- `../components/toggletip.md`
- `../components/popover.md`
- `../../foundations/interaction/contextual-guidance.md`
- `multi-step-flow.md`
- `../../accessibility/focus-management.md`
