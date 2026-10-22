---
id: design-system.component.side-navigation
collection: design-system
type: component
title: Side Navigation
summary: Draft design contract for persistent destination navigation with expanded and compact rail presentation, two-level disclosure and a non-modal compact Flyout.
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
  - design-system.accessibility.keyboard-navigation
  - design-system.accessibility.focus-management
  - design-system.accessibility.screen-reader-semantics
  - design-system.accessibility.structure-and-navigation
---

# Side Navigation

> **Draft / owner review pending (HOS-52).** This document records a live Figma design candidate and a proposed interaction/accessibility contract. It is not a released public API, does not claim implemented Storybook behavior, and does not supersede the independently reviewed accessibility foundations.

## Purpose and ownership

Side Navigation presents persistent product destinations and nested destinations, normally within the logical **Start Pane** of the App Shell (the right-hand edge in RTL).

- **App Shell / Start Pane** owns placement, space allocation, logical boundaries, the collapse affordance's placement, the compact/expanded layout state, and responsive composition.
- **Side Navigation** owns the contents, navigation item presentation, active destination, and inline disclosure or compact-rail Flyout composition.
- **Drawer** is a separate temporary/overlay component. Reusing the same navigation content in Drawer on a narrow viewport does not turn Side Navigation into a Drawer variant.
- **Menu** remains the action/command surface; persistent destination navigation is not an ARIA menu or application menubar.

Side Pane is a **layout region**, not a separate published Side Pane component.

## Canonical design evidence

| Figma source | Node |
|---|---|
| Side Navigation Component Set | [24631:180](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24631-180) |
| Side Navigation Item Component Set | [24643:1407](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24643-1407) |
| Presentation and integration examples | [24664:42762](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24664-42762) |
| Interaction and accessibility examples | [24782:697](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24782-697) |

These node IDs describe **editable design evidence**, not a verified runtime package/Storybook component.

## Anatomy and Figma authoring

**Side Navigation** includes a native \`Items\` Slot. Its design-time axes are:

| Axis | Values | Guidance |
|---|---|---|
| \`Compact\` | \`False / True\` | Expanded icon + label, or icon-only rail |
| \`Size\` | \`Small / Medium / Large\` | One uniform Size for every interactive Item in a single navigation |

A Side Navigation can combine Item types, but **must not mix interactive Item sizes** within one navigation. Group headings and dividers are non-interactive and can have their own intrinsic heights. Slot content manually inserted in Figma must obey the same Size; the Slot does not enforce this automatically.

**Side Navigation Item** uses:

| Axis / property | Design-time values | Notes |
|---|---|---|
| \`Type\` | \`Link / Submenu / Divider / Group\` | Divider and Group are non-interactive |
| \`Compact\` | \`False / True\` | Level 2 does not have a separate compact-rail item |
| \`Level\` | \`Level 1 / Level 2\` | Level 2 is for expanded Link destinations |
| \`Size\` | \`Small / Medium / Large\` | Inherited by authoring convention from Navigation |
| \`State\` | \`Default / Hover / Active / Selected / Selected Hover / Disabled\` | Type-specific combinations, not a complete Cartesian product |
| \`Expanded\` | \`False / True\` | Only expanded-view Submenu; changes its direct Chevron down/up. This is a Figma Variant axis, **not a native Boolean** |
| \`Label\` | Text | Visible in expanded view; source for icon-only accessible name |
| \`Leading icon\` / \`Show leading icon\` | Swap / Boolean | Level 1 default has an icon |
| \`Show Level 2 icon\` | Boolean | Level 2 default is text-only; optional icon when needed |
| \`End content\` / \`Show end content\` | Slot / Boolean | Non-interactive supplemental Tag, count or status; logical end before Chevron |
| \`Show focus\` | Boolean | Independent of Selected, to represent Selected + Focus |

Use \`Tag / Extra Small / Neutral\` for a simple sample count; do not create a competing Counter component. A Link should not nest an independently clickable button within its End content.

## Design sizes and responsive relationships

Current **Figma candidate**, pending owner approval, not a required shipped runtime size:

| Side Navigation | Width |
|---|---:|
| \`Compact=False\` | 256px |
| \`Compact=True\` | 64px |

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
| Default | transparent | \`fg/secondary\` | \`fg/secondary\` |
| Hover | \`surface/transparent-hover\` | \`fg/secondary\` | \`fg/secondary\` |
| Active | \`surface/transparent-active\` | \`fg/secondary\` | \`fg/secondary\` |
| Selected/current | \`surface/selected\` | \`fg/primary\` | \`fg/primary\` |
| Selected Hover | \`surface/selected-hover\` | \`fg/primary\` | \`fg/primary\` |
| Disabled | transparent | \`fg/disabled\` | \`fg/disabled\` |

\`focus/default\` is a distinct, visible focus treatment and may coexist with Selected. Follow the reviewed Focus Management foundation for the external 2px ring and 1px gap rather than inventing a component-specific Accent border.

**Unresolved design option:** Selected destinations might use a filled rather than an outlined icon in the future. This is **TBD**, not a variant or automatic substitution in the current source.

## Interaction proposal for owner review

Use ordinary **disclosure navigation**, with a native navigation landmark and nested lists, instead of adopting an ARIA \`menu\`/\`menubar\` or \`tree\` composite role. This keeps Link navigation and the Submenu's disclosure action distinct.

### Expanded view

- \`Link\` navigates to a real destination; the current page link exposes \`aria-current="page"\` as appropriate.
- \`Submenu\` is an actual button, not a link with a hidden secondary click target. Enter and Space toggle its nested list; \`aria-expanded\` tracks the real disclosure state and \`aria-controls\` may identify the controlled list.
- Collapsed inline children are absent from the keyboard/tab sequence and unavailable as actionable accessibility-tree controls.
- The design is intentionally limited to two navigation levels in this candidate. A third level requires an explicit owner decision.
- \`Group\` and \`Divider\` are not focusable.
- A current leaf destination and its expanded ancestor have different semantic meanings; do not mechanically announce the parent as another current page.

### Compact rail

- The rail is icon-only, but each Link and Submenu trigger still has a meaningful accessible name derived from its Label. A Tooltip is optional supporting guidance and **does not** replace the accessible name.
- A leaf Link remains a destination. A Submenu trigger opens an **anchored, non-modal navigation Flyout** into the available adjacent content side (left of the Start rail in RTL).
- Flyout opens by click/tap, Enter or Space, **not only Hover**. Optional pointer hover may supplement—not replace—those mechanisms.
- Flyout shows the submenu's text label and its nested links. Focus may move into the Flyout when activation/interaction requires it, but a hover preview must never steal keyboard focus.
- Escape closes an open Flyout and returns focus to its rail trigger. Clicking outside or moving focus out dismisses the Flyout; do not arbitrarily force focus back for ordinary focus exit.
- A Flyout is not a modal Dialog: no backdrop and no blanket focus trap. Handle viewport collision, clipping, overlay layering and scroll continuity in the owning composition, with implementation testing.
- Compact state/width is controlled by the App Shell. Trigger placement, persistence across pages and the narrow-viewport Drawer handoff are **not** decided by this Item document.

### Keyboard and semantics

| Input | Expected behavior |
|---|---|
| Tab / Shift+Tab | Visits visible Link and disclosure Button stops in logical DOM order |
| Enter on Link | Native navigation |
| Enter / Space on Submenu Button | Toggle inline submenu or rail Flyout |
| Escape with Flyout open | Dismiss Flyout and return focus to the trigger |
| Arrow / Home / End | Not required for v1; optional enhancement only if consistently implemented and tested |

Follow [Keyboard Navigation](../../accessibility/keyboard-navigation.md), [Focus Management](../../accessibility/focus-management.md), [Screen Reader Semantics](../../accessibility/screen-reader-semantics.md) and [Structure and Navigation](../../accessibility/structure-and-navigation.md). Keep DOM order meaningful in RTL and responsive transitions. Do not silently move focus on receipt of focus alone.

## Content guidance

Labels should identify destinations in concise, stable language. Truncate only when necessary and preserve the full accessible name; a Tooltip can supplement a truncated label. Use non-interactive End content for a concise count or status without competing with the Submenu Chevron. Avoid ambiguous “click to navigate or expand” hybrid targets until a separate interaction model is approved.

## Verification checklist and open gaps

**Figma observed:** Source variant axes and RTL item alignment; the candidate Surface/Spacing/Radius/Foreground tokens; independent Selected and Focus visuals; inline two-level example and icon-only rail; example anchored Flyout composition. The Flyout shown in Figma is an **illustrative layout**, not verified prototype behavior.

**Must be tested in Code/Storybook before Ready for Dev or release:**

- [ ] keyboard activation, Tab order, Escape/return-focus behavior, hidden-item focus exclusion;
- [ ] screen reader navigation landmark, accessible name, current page, expanded state and list hierarchy;
- [ ] pointer/touch trigger usability, outside dismissal, safe hover behavior and pointer-content persistence;
- [ ] RTL/LTR, zoom, narrow viewports, clipping and collision positioning of Flyout;
- [ ] App Shell toggle placement, compact state persistence and responsive Drawer handoff;
- [ ] effective target sizes and focus ring contrast across Product/Appearance themes;
- [ ] existing runtime component mappings, package API and Storybook stories (none verified here).

**Open design decisions:** Filled icon on Selected (TBD); whether a compact Flyout should support click-to-pin (not included in this candidate); collision and scroll specifications; any third navigation level; exact runtime width breakpoints/resize behavior. Review these separately rather than silently treating the Figma candidate as a released contract.

## Related evidence

- [Responsive Layout](../../foundations/visual/responsive-layout/guideline.md) — layout regions and responsive strategy.
- [Menu](menu.md) — action/command menu, not persistent destination navigation.
- [Drawer](drawer.md) — independent temporary side surface; currently unverified.
- [W3C APG disclosure navigation example](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/) — reference for native links and buttons without menu semantics.
