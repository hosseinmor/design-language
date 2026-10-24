---
id: design-system.component.date-input
collection: design-system
type: component
title: Date Input (legacy name)
summary: Backward-compatible redirect to the canonical Date Picker component in Calendar Off mode.
knowledge_state: canonical
document_maturity: draft
owner: Design System team
related:
  - design-system.component.date-picker
topics:
  - date-input
  - date-field
  - segmented-date
  - legacy
---

# Date Input — legacy compatibility name

**The canonical Karbon Design System component is now [Date Picker](date-picker.md).** It supports segmented manual date entry in **both** modes:

- **Calendar Off**: manual-only date entry; no Calendar button or popup.
- **Calendar On** (default): the same segmented editing experience with a separately operated Calendar button and popup.

Do **not** maintain or introduce a second public Date Input component. The former Date Input Figma master (`24779:839`) is preserved only in **Date & Time · Legacy compatibility sources** for existing instances. The public Date Picker master (`24703:8942`) is on the **Date Picker** page. Do not silently detach, rename, or swap legacy consumers without an explicit migration review.

Use the **[Date Picker contract](date-picker.md)** for Anatomy, Size/State, Calendar authoring and open behavior, Field Label, Focus effects, error and supporting slots, segmented editing, locale, RTL, accessibility and implementation acceptance. The former Date Input behavior maps to `Date Picker / Calendar=false`.

This is a **design consolidation decision** approved for HOS-49 on 2026-10-24. It is **not** evidence that a matching runtime Date Picker API already exists in Karbon/Storybook. Exact runtime property naming and migration steps remain implementation review items.
