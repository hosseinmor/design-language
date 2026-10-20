---
id: design-system.pattern.multi-step-flow
collection: design-system
type: pattern
title: Multi-Step Flow
summary: 'Default combination:'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Multi-Step Flow

## Intermediate Steps

Default combination:

- Forward action → Primary
- Back action → Ghost

Example:

```text
[Continue]  Back
```

Do not use Brand for every forward action. Intermediate progression is normally an operational action and remains Primary.

## Final Step

The final Button label must describe the result rather than repeat “Continue.”

Examples:

- Submit request
- Create job
- Send for approval
- Pay
- Submit resume

Preset selection:

- Operational result → Primary
- Approved product conversion / product-defining result → Brand
- Destructive result → Danger Filled

Being the final step does not automatically make an action Brand. Brand is only used when the result belongs to the approved product conversion/product-moment contract.

## Back, Cancel, Close, and Exit

| Action | Meaning |
|---|---|
| Back | Move to the previous step without leaving the flow |
| Cancel | Cancel the current operation |
| Close | Close the current surface |
| Exit | Leave the entire flow |

When Close or Exit causes data loss, show a confirmation. Button styling alone is not sufficient to communicate the risk.

## RTL Placement

- Place the forward or main action on the right side of the action group.
- Place Back, Cancel, or an alternative after it, toward the left.
- A third or exit action may be separated from the main group.

## Mobile

- The main action may become full width.
- Place the secondary action below it.
- Preserve visual hierarchy after stacking.

## Submission State

When the current step is submitting:

- The triggered Button enters Loading.
- Repeated submission is blocked.
- Availability of Back, Cancel, Exit and competing actions during submission is **flow-specific**. Product Knowledge or the approved feature flow must determine whether they remain available, require a safety confirmation, or are temporarily unavailable; do not globally disable them based on this draft pattern.

## Ownership and open decisions

This pattern owns generic step navigation and action composition, not feature-specific permissions, submission cancellation support, or navigation policy. Exact runtime transitions and eligibility remain Product Knowledge/code-owned.

## Related Documents

- `../components/button.md`
- `../../foundations/interaction/action-hierarchy.md`
- `confirmation.md`
