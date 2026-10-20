# Patterns

Patterns describe how components work together to solve recurring interaction
problems. They own reusable composition and behavior, while Product Knowledge
owns feature-specific policy, permissions, states, and flows.

## Pattern boundaries

- Interaction Foundations own **cross-component choice and behavior principles**.
- Patterns own **how multiple components combine** to solve a recurring task.
- Components own anatomy, their meaningful states, accessibility details and visual contracts.
- Content System owns text, labels and messages; Accessibility owns normative requirements.
- Product Knowledge owns product eligibility, persistence/business policy and feature-specific lifecycle.

The documents marked `scaffold` are reserved TBD subjects, not approved implementation or usage contracts. Use a current owning source instead: [Loading and Progress](loading-and-progress.md) is reviewed/final; [Notifications](notifications.md) and [Tour](tour.md) remain drafts with established decisions and explicit gaps. Read [maturity-aware AI retrieval](../../ai/retrieval.md) rather than treating all drafts as either approved or invalid.
