---
id: design-system.component.side-navigation
collection: design-system
type: component
title: Side Navigation
summary: Draft design contract for persistent destination navigation with expanded and compact rail presentation, two-level disclosure and temporary hover-expansion from the compact rail.
knowledge_state: unverified
document_maturity: draft
owner: Design System team
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24631-180
source_node: 24631:180
related:
  - design-system.foundation.responsive-layout
  - design-system.token.spacing.catalog
  - design-system.component.menu
  - design-system.component.drawer
  - design-system.component.app-shell
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.focus-management
  - design-system.accessibility.screen-reader-semantics
  - design-system.accessibility.structure-and-navigation
---

# Side Navigation

> **Draft / owner review pending (HOS-52).** This document records a live Figma design candidate and a proposed interaction/accessibility contract. It is not a released public API, does not claim implemented Storybook behavior, and does not supersede the independently reviewed accessibility foundations.

## Purpose and ownership

Side Navigation presents persistent product destinations and nested destinations, normally within the logical **Start Region** of the App Shell (the right-hand edge in RTL).

- **App Shell / Start Region** owns placement, space allocation, logical boundaries, the collapse affordance's placement, the compact/expanded layout state, and responsive composition.
- **Side Navigation** owns the contents, navigation item presentation, active destination, and inline disclosure and the compact-rail hover-expanded overlay composition.
- **Drawer** is a separate supplementary surface. On a narrow viewport, App Shell may present the existing Side Navigation itself as a temporary expanded panel; do not wrap it in Drawer or create a mobile Side Navigation variant.
- **Menu** remains the action/command surface; persistent destination navigation is not an ARIA menu or application menubar.

Side Pane is a **layout region**, not a separate published Side Pane component.

## Canonical design evidence

| Figma source | Node |
|---|---|
| Side Navigation Component Set | [24631:180](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24631-180) |
| Side Navigation Item Component Set | [24643:1407](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24643-1407) |
| Presentation and integration examples | [24664:42762](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24664-42762) |
| Hover-expanded and edge-case Playground (Section 02) | [24854:44261](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24854-44261) |

These node IDs describe **editable design evidence**, not a verified runtime package/Storybook component.

## Anatomy and Figma authoring

**Side Navigation** includes a native `Items` Slot. Its design-time axes are:

| Axis | Values | Guidance |
|---|---|---|
| `Compact` | `False / True` | Expanded icon + label, or icon-only rail |
| `Size` | `Small / Medium / Large` | One uniform Size for every interactive Item in a single navigation |

A Side Navigation can combine Item types, but **must not mix interactive Item sizes** within one navigation. Group headings and dividers are non-interactive and can have their own intrinsic heights. Slot content manually inserted in Figma must obey the same Size; the Slot does not enforce this automatically.

**Side Navigation Item** uses:

| Axis / property | Design-time values | Notes |
|---|---|---|
| `Type` | `Link / Submenu / Divider / Group` | Divider and Group are non-interactive |
| `Compact` | `False / True` | Level 2 does not have a separate compact-rail item |
| `Level` | `Level 1 / Level 2` | Level 2 is for expanded Link destinations |
| `Size` | `Small / Medium / Large` | Inherited by authoring convention from Navigation |
| `State` | `Default / Hover / Active / Selected / Selected Hover / Disabled` | Type-specific combinations, not a complete Cartesian product |
| `Expanded` | `False / True` | Only expanded-view Submenu; changes its direct Chevron down/up. This is a Figma Variant axis, **not a native Boolean** |
| `Label` | Text | Visible in expanded view; source for icon-only accessible name |
| `Leading icon` / `Show leading icon` | Swap / Boolean | Level 1 default has an icon |
| `Show Level 2 icon` | Boolean | Level 2 default is text-only; optional icon when needed |
| `End content` / `Show end content` | Slot / Boolean | Non-interactive supplemental Tag, count or status; logical end before Chevron |
| `Show focus` | Boolean | Independent of Selected, to represent Selected + Focus |

Use `Tag / Extra Small / Neutral` for a simple sample count; do not create a competing Counter component. A Link should not nest an independently clickable button within its End content.

## Design sizes and responsive relationships

Current **Figma candidate**, pending owner approval, not a required shipped runtime size:

| Side Navigation | Width |
|---|---:|
| `Compact=False` | 256px |
| `Compact=True` | 64px |

| Navigation Item Size | Expanded row height | Compact icon target height | Leading icon |
|---|---:|---:|---:|
| Small | 32px | 40px | 16px |
| Medium (design default) | 40px | 48px | 20px |
| Large | 48px | 48px | 20px |

These targets are authored visual dimensions. Minimum effective touch-target conformance and responsive feasibility still need implementation-specific testing. A global breakpoint should not be invented for this component: App Shell coordinates available space and the transition strategy under [Responsive Layout](../../foundations/visual/responsive-layout/guideline.md).

**RTL alignment:** When Level 2 is text-only, its label starts on the same vertical line as the Level 1 label. The current token-bound right padding is:

| Size | Level 1 | Level 2 | Label start from Item right edge |
|---|---:|---:|---:|
| Small | 8px | 32px | 32px |
| Medium | 12px | 40px | 40px |
| Large | 12px | 40px | 40px |

This alignment is achieved with the leading icon + gap for Level 1 and in-item padding for Level 2. It must not depend on a second padded parent wrapper. Logical positioning must mirror for LTR.

## Visual state contract (design candidate)

| State | Surface | Text | Icon |
|---|---|---|---|
| Default | transparent | `fg/secondary` | `fg/secondary` |
| Hover | `surface/transparent-hover` | `fg/secondary` | `fg/secondary` |
| Active | `surface/transparent-active` | `fg/secondary` | `fg/secondary` |
| Selected/current | `surface/selected` | `fg/primary` | `fg/primary` |
| Selected Hover | `surface/selected-hover` | `fg/primary` | `fg/primary` |
| Disabled | transparent | `fg/disabled` | `fg/disabled` |

`focus/default` is a distinct, visible focus treatment and may coexist with Selected. Follow the reviewed Focus Management foundation for the external 2px ring and 1px gap rather than inventing a component-specific Accent border.

**Unresolved design option:** Selected destinations might use a filled rather than an outlined icon in the future. This is **TBD**, not a variant or automatic substitution in the current source.

## Interaction proposal for owner review

Use ordinary **disclosure navigation**, with a native navigation landmark and nested lists, instead of adopting an ARIA `menu`/`menubar` or `tree` composite role. This keeps Link navigation and the Submenu's disclosure action distinct.

### Expanded view

- `Link` navigates to a real destination; the current page link exposes `aria-current="page"` as appropriate.
- `Submenu` is an actual button, not a link with a hidden secondary click target. Enter and Space toggle its nested list; `aria-expanded` tracks the real disclosure state and `aria-controls` may identify the controlled list.
- Collapsed inline children are absent from the keyboard/tab sequence and unavailable as actionable accessibility-tree controls.
- The design is intentionally limited to two navigation levels in this candidate. A third level requires an explicit owner decision.
- `Group` and `Divider` are not focusable.
- A current leaf destination and its expanded ancestor have different semantic meanings; do not mechanically announce the parent as another current page.

### Compact rail — Hover-expanded navigation

**Approved design direction for HOS-52; implementation remains unverified.** A compact Side Navigation is a **64px persistent rail**. On pointer hover over that rail, **the entire Navigation** appears temporarily at its normal **256px expanded width** as an anchored **non-modal overlay** on top of the adjacent Main Content (left of the Start rail in RTL). This is **not a submenu Flyout**. It is not a Modal/Drawer: no backdrop, focus trap, background inertness or Main Content resize. The Start region continues reserving only the original 64px.

This temporary expanded presentation uses the existing `Compact=False` design and ordinary inline submenus; **do not add Hover-expanded as a third Navigation variant or multiply Item variants**. The App Shell/composition controls the temporary overlay and its layering/overflow; navigation content stays the same source.

#### Current route and nested selection

- `Current destination` derives from the active product route. In Compact, the Level 1 ancestor of a current Level 2 destination has a **visual current-section cue**, because the actual leaf cannot be shown in the rail. This **does not** make the ancestor the current page and must not put `aria-current="page"` on the ancestor.
- On **every fresh temporary expansion**, automatically open the Level 1 group that contains the current destination. Show the actual Level 2 destination as `Selected` with `aria-current="page"`; its parent is `Expanded=True`, **not a second Selected destination**.
- If the current route is itself a top-level Link, select that Link; do not open an unrelated submenu by default.
- Users can open a different group or collapse the current group inside the temporary overlay. Keep at most **one inline group** open for v1.
- Temporary group changes are **not persisted**. After the entire preview closes, a new hover starts again from the current route's group. Route changes update the current destination and its default expanded ancestor.
- Persistent `Compact=False` navigation may have its own normal inline disclosure state; temporary preview changes **must not overwrite** that persistent choice.
- Do not create three extra Figma state axes for `Current route`, `Open group`, or `Temporary preview`. They are **behavioral concepts**, not additional public visual variants.

#### Activation, dismissal and non-hover access

- **Pointer:** entering the Compact Rail temporarily opens the whole panel, not just the hovered item's children. Keep it open while pointer moves across the full expanded panel, including its links and submenus. Close when pointer leaves the **whole panel** and no keyboard focus remains inside; minor entry/exit hysteresis may prevent flicker (exact timing is an implementation detail, not a global token).
- **Escape:** dismiss the temporary panel. Do not immediately reopen it while the pointer remains stationary on the trigger; permit reopening after a new pointer exit/re-entry or explicit activation. When keyboard focus moved into the panel, restore it to the originating control on Escape.
- **Keyboard and touch must not depend on hover:** the App Shell's persistent Expand/Collapse control provides access to the full Navigation. Explicit activation of a Compact Submenu control can also reveal the same temporary expanded panel and its relevant submenu; never make a nested destination hover-only.
- Clicking outside or moving focus outside may close the temporary panel. Do not steal focus on pointer hover; do not force focus restoration for ordinary focus exit.
- A Compact Link without children remains a real Link and navigates on activation.
- Keep a meaningful accessible name on every icon-only control; Tooltip is supplemental, not a substitute.
- Avoid clipping beneath the Main region, other scroll containers and the viewport. Check overlay stacking, pointer travel, zoom and RTL/LTR mirroring during runtime QA.

The App Shell owns the persistent Compact preference, collapse button location, usable Start width and any narrow-viewport temporary-navigation composition. No new Side Navigation variant or modal semantics are introduced by the hover preview.

### Keyboard and semantics

| Input | Expected behavior |
|---|---|
| Tab / Shift+Tab | Visits visible Link and disclosure Button stops in logical DOM order |
| Enter on Link | Native navigation |
| Enter / Space on Submenu Button | Toggle inline submenu when expanded; in Compact, explicitly reveal the temporary full panel and relevant group |
| Escape with temporary overlay open | Dismiss temporary expansion and restore focus when focus had entered it; avoid instant hover reopening |
| Arrow / Home / End | Not required for v1; optional enhancement only if consistently implemented and tested |

Follow [Keyboard Navigation](../../accessibility/keyboard-navigation.md), [Focus Management](../../accessibility/focus-management.md), [Screen Reader Semantics](../../accessibility/screen-reader-semantics.md) and [Structure and Navigation](../../accessibility/structure-and-navigation.md). Keep DOM order meaningful in RTL and responsive transitions. Do not silently move focus on receipt of focus alone.

## Content guidance

Labels should identify destinations in concise, stable language. In the fixed-height Side Navigation Item, text labels are visually **single-line with ending ellipsis** when too long; preserve the complete accessible name for assistive technology. A Tooltip may supplement a truncated label but does not replace its accessible name. Use non-interactive End content for a concise count or status without competing with the Submenu Chevron. Avoid ambiguous “click to navigate or expand” hybrid targets until a separate interaction model is approved.

## Verification checklist and open gaps

**Figma observed:** Original masters remain in the 2528px reviewed presentation, organized into Sections 00–04. Source-linked Playground coverage includes Expanded/Compact App Shell samples, uniform Small/Medium/Large density, Submenu + current Level 2, non-interactive Tag, Selected + Focus, Disabled, long-label ellipsis, and temporary full-width hover-expanded Navigation over unchanged Main Content. These are **illustrative designs**, not tested interactive prototypes.

**Must be tested in Code/Storybook before Ready for Dev or release:**

- [ ] keyboard activation, Tab order, Escape/return-focus behavior, hidden-item focus exclusion;
- [ ] screen reader navigation landmark, accessible name, current page, expanded state and list hierarchy;
- [ ] pointer hover-expansion of the entire rail, pointer-to-panel persistence, click/touch/keyboard alternatives, outside dismissal and Escape suppression of immediate reopening;
- [ ] RTL/LTR, zoom, narrow viewports, overlay clipping/stacking and collision handling for hover-expanded Navigation;
- [ ] App Shell toggle placement, compact state persistence and responsive temporary-navigation handoff;
- [ ] effective target sizes and focus ring contrast across Product/Appearance themes;
- [ ] existing runtime component mappings, package API and Storybook stories (none verified here).

**Open design decisions:** Filled icon on Selected (TBD); detailed overlay collision/scroll behavior and hover timing for implementation; any third navigation level; exact runtime responsive breakpoints/resize behavior. The temporary overlay is not a pinned third Navigation presentation. Review these separately rather than silently treating the Figma candidate as a released contract.

## Related evidence

- [Responsive Layout](../../foundations/visual/responsive-layout/guideline.md) — layout regions and responsive strategy.
- [Menu](menu.md) — action/command menu, not persistent destination navigation.
- [Drawer](drawer.md) — independent supplementary surface; currently unverified.
- [W3C APG disclosure navigation example](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) — reference for native links and buttons without menu semantics.
