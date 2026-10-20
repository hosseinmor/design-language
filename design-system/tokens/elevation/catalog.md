---
id: design-system.token.elevation.catalog
collection: design-system
type: token
title: Elevation Token Catalog
summary: Approved Shadow/Floating and Shadow/Dragged recipes, including current Light values and Dark resolution notes.
knowledge_state: canonical
document_maturity: reviewed
related:
  - design-system.foundation.elevation
---

# Elevation Token Catalog

This document records the reviewed design recipe. Current editable Figma Effect Styles remain the source for exact live visual construction; frontend implementation must be verified in code.

## Shadow / Floating

```css
0 0 0 1px #d1d9e040,
0 6px 12px -3px #25292e0a,
0 6px 18px 0 #25292e1f
```

- Three-layer composite: first layer provides an outline-like boundary; the remaining two provide elevation.
- Dark uses the same layer geometry with Appearance-aware colors.
- Figma binds the effect colors to internal implementation variables, including private `shadow/floating/border`; these are not public Color tokens.

## Shadow / Dragged

```css
0 12px 16px 0 rgba(0,0,0,.08),
0 6px 8px 0 rgba(0,0,0,.04),
0 0 6px 0 rgba(0,0,0,.16)
```

- Dark keeps the same geometry and uses approximate layer opacities of 24%, 12%, and 48%; inspect current Figma for exact values.
