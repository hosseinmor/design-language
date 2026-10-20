---
id: design-system.component.modal
collection: design-system
type: component
title: Modal (legacy name)
summary: Backward-compatible redirect to the canonical Dialog component.
knowledge_state: canonical
document_maturity: reviewed
last_reviewed: 2026-10-17
related:
  - design-system.component.dialog
---

# Modal — legacy alias

**The canonical JobVision Design System component is now [Dialog](dialog.md).** Modal is the behavior (a blocking, inert background); Dialog is the component name. Do not implement or maintain two independent components.

The previous Modal Figma Component Set (node `4080:55366`, key `dbb168637e13405605604dd1ca479f298735c348`) remains archived/unchanged for existing consumers and migration. The **new, handoff-ready Figma Dialog** master is node `24036:267`. Do not silently swap or detach legacy consumers without migration review.

Use [Dialog](dialog.md) for anatomy, size/responsive behavior, Close, Escape and backdrop policy, focus, scroll, confirmation/alert semantics, accessibility and implementation acceptance. See the [component mapping registry](../../integrations/component-mapping.md) for verified Figma IDs and runtime gaps.
