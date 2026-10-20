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

The documents marked `scaffold` are reserved TBD subjects, not approved implementation or usage contracts. Prefer a reviewed component or pattern before using a scaffold as evidence. Examples: [Loading](loading-and-progress.md), [Notifications](notifications.md), [Tour](tour.md).
