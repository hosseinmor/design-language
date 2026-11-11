---
id: design-system.pattern.list-detail
collection: design-system
type: pattern
title: List–Detail
summary: Draft reusable composition and navigation guidance for browsing a collection and inspecting one current item's detail across wide and narrow layouts.
knowledge_state: unverified
document_maturity: draft
design_status: in-progress
owner: Design System team
source_figma: https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24988-3948
source_node: 24988:3948
related:
  - design-system.foundation.responsive-layout
  - design-system.foundation.responsive-layout-spec
  - design-system.pattern.data-views
  - design-system.component.table
  - design-system.component.drawer
  - design-system.component.side-navigation
  - design-system.accessibility.focus-management
  - design-system.accessibility.structure-and-navigation
  - design-system.accessibility.responsive-and-zoom
  - design-system.accessibility.dynamic-content-and-feedback
topics: [list-detail, master-detail, split-view, drill-in, navigation, responsive]
---

# List–Detail

> **HOS-55 / DRAFT — owner review pending.** This document proposes a reusable cross-component pattern. The live Figma presentation contains **editable candidate compositions**, not a released List–Detail component or verified code behavior. Do not treat example dimensions, a selected-item treatment, mobile routing, or Drawer modality as an approved runtime API. All normative decisions below remain subject to owner review.

## Purpose

Let users explore a collection of entities while inspecting the details of one current entity without losing the collection context. This pattern owns the **relationship, composition and transition** between a **Collection region** and a **Detail region**. It does not own the visuals, semantics or lifecycle of the component used inside either region.

Typical contexts: reviewing a collection of job opportunities, candidates, requests or records; switching among items whose detailed content has a meaningful identity. Product-specific entities are examples, not part of the shared pattern contract.

### Use when

- One collection supports repeated navigation among individual entities.
- The detail represents an identifiable item, potentially linkable independently of the collection.
- Preserving filter, order, selection and scroll context helps users move through the set.
- There is a coherent transition from viewing both regions to one region when space is constrained.

### Avoid when

- Two columns merely hold unrelated page content.
- A row only reveals a short supplemental block: consider existing disclosure/row expansion.
- Users primarily compare many rows/columns: the owning Data View may be sufficient without a persistent Detail region.
- Detail is an isolated, lengthy workflow better served by a dedicated page.
- A temporary supplementary task is the main need: evaluate Drawer rather than making List–Detail a substitute.
- Multiple records are edited side by side or multi-selection is the primary task: these require separate composition rules.

## Anatomy and ownership

**Collection region**
- Optional collection title, result count, search/filter/tools area.
- Data View content, chosen by task: Structured List, Data Table or another appropriate canonical item composition.
- Optional pagination, infinite loading or collection footer.

**Detail region**
- Optional item-specific header and contextual actions.
- Selected item's information and independently owned controls.
- Optional related sections, loading feedback or recovery affordances.

**Cross-region relationship**
- An **active detail identity** maps exactly one current entity to its detail; the collection may have no active detail.
- Active detail is **not** equivalent to keyboard focus, pointer hover, a Checkbox selection set, or Data Table row expansion.
- Layout owns placement, not the internal styling of the participating components.

### Contract boundaries

| Owner | Responsible for | Not responsible for |
| --- | --- | --- |
| List–Detail Pattern | Cross-region composition, current-detail relationship, navigation continuity, responsive transformation, cross-region states and focus handoff | Individual row visual states, Drawer internals, product URLs |
| Data Views / Structured List / Data Table | Collection item anatomy, sorting, table columns, row actions, checkbox selection, individual keyboard contract | Detail region and navigation history |
| Responsive Layout / App Shell | Logical page regions, shared ranges, constraints, reserved shell space | Which business record opens |
| Drawer | Overlay/inline/floating surface behavior when independently approved | The List–Detail navigation model |
| Product | Entity identifiers, route shape, default selected item, filters, permissions, action eligibility and fallback policies | Reusable pattern semantics |

**Important source discrepancy (24 October 2026):** Figma currently contains Drawer display candidates including Overlay, Inline and Floating. The main-branch Drawer component document is still a scaffold with modality and focus details marked TBD. This Pattern does not certify or supersede it.

## Wide composition (proposal)

A List–Detail workspace is a **Split page**, as required by the reviewed Responsive Layout Foundation. Place Collection at logical **Start** and Detail in the remaining task area. In RTL, Collection therefore appears to the right of Detail. Within an existing App Shell, these regions may both be composed inside Main Content; the Detail is **not always** an App Shell End Pane or an Inline Drawer.

**Width and sizing**
- Determine usable content width **after** shell/navigation and region padding, not from viewport width alone.
- Give each region a content-driven minimum. One region may be a stable scan width while the other flexes; a column-heavy Data Table may instead need the wider region.
- Do not turn the demo widths in Figma into new tokens or universal component sizes. The reviewed ruler includes breakpoint/large = 1012px, but crossing it alone does not force Split View.
- A divider or gap expresses the region boundary; avoid inserting a second independent outer container or duplicating shell padding.
- Respect the existing Layout Token Catalog and shared responsive ranges; do not introduce a separate List–Detail breakpoint scale.

**Scrolling**
- Independent Collection and Detail scroll is appropriate for a full-height operational workspace when each region remains independently usable and can scroll with keyboard, touch and assistive technology.
- For document-like or short layouts, page-level scrolling may be more appropriate. Do not require two scroll containers universally.
- Collection tools and Detail header may be sticky where useful. Do not obscure focused controls; account for a sticky header in scroll/focus behavior.
- Long Detail content must not stretch or scroll the Collection unintentionally in an intended two-scroller layout.

**Initial/no-current-item policy**
- Pattern supports both an unselected placeholder and opening with an active detail.
- Whether the first item auto-opens on arrival is a **Product decision**, not a shared mandatory default. Never change keyboard focus simply because data loaded.

## Selection and navigation (proposal)

- **Activate explicitly:** the current detail changes on deliberate item activation (appropriate link/button activation), not on mere keyboard focus or hover.
- **Separate states:** active/current detail can coexist with focused and hovered states without overwriting the visible focus ring; checkbox selection remains independent.
- **Retain context:** switching details should preserve Collection filters, sort, pagination and scroll unless the product intentionally resets them.
- **Deep linking:** if a detail is a navigable entity, a direct link should resolve to the same entity regardless of wide/narrow presentation. Products define the exact URL, history-entry and permission model.
- **Browser back:** on a narrow drill-in, Back should restore the previous Collection context and preferably focus the invoking item if it still exists. On wide inline selection, exact browser-history handling is Product-owned and must be explicit.
- **Stale selection:** if the item is filtered out, deleted or inaccessible, do not silently present a contradictory current marker. Preserve the current detail only when a clear contextual relationship remains valid; otherwise provide an intentional no-selection/unavailable state and a way to recover.
- **Single current detail:** multi-record selection and batch actions are outside this pattern; Data Views and Bulk Actions own those contracts.

## State coordination

| Condition | Pattern-level guidance | Open Product decision |
| --- | --- | --- |
| Collection initially loading | Preserve an intelligible collection region; use established Loading/Skeleton patterns | Whether prior results remain visible |
| Detail loading after activation | Keep Collection context and indicate the pending Detail region; avoid blocking the whole page | Whether to cache prior detail |
| Empty collection / no matches | Show an appropriate empty or no-results state within Collection; do not invent a current item | Query reset/clear eligibility |
| Nonempty collection, no item active | Show an explicit neutral Detail placeholder or choose product-approved default detail | First-item auto-open policy |
| Detail unavailable/deleted | Identify the unavailable entity, clear contradictory visual current state, offer recovery | Eligibility, fallback item |
| Collection error | Offer recovery in Collection while keeping any valid Detail understandable | Stale results visibility |
| Detail error | Keep browsing usable and offer Detail retry/back action | Error and retry policy |
| Filter excludes current item | Reconcile current marker and Detail without surprising navigation | Retain or clear off-list item |
| Permission/availability changes | Follow product truth and provide coherent transition | Exact permission/business rules |

Reuse the owning Loading, Empty States, Error Content and Notifications guidance. These are **pattern states**, not variants added to Table, List or Drawer.

## Responsive transformation (proposal)

- Use the shared Responsive Layout ranges and fine-tune only when both region minima really fit. A container/content feasibility rule may be better than a viewport-only threshold.
- **Wide / sufficient space:** persistent Collection + Detail Split View, potentially with independent scrolling.
- **Constrained / narrow:** default candidate is **drill-in navigation**: Collection view → identifiable Detail view → return to Collection. A side-by-side table squeezed below a usable width is not an acceptable fallback.
- **Drawer as an alternative:** use only when Detail is temporary/contextual and the Drawer component's approved focus/modality, dismissal and placement contracts are appropriate. Narrow viewport alone does not mandate Drawer.
- Preserve active item, filters, sorting, scroll and user context during wide↔narrow transformation.
- Do not keep a hidden but focusable inactive pane in the tab sequence.
- Product decides navigation stack shape and whether an active deep link opens Detail directly in narrow mode.

## RTL and direction

- Use logical Start/End rather than hard-coded right/left names. RTL places Collection on the visual right for the default navigation-first composition.
- Mirror visual transition/back direction with layout direction without altering the logical meaning of navigation or the semantic reading order.
- Prefer a DOM/reading sequence consistent with the active task. Reflow must not create contradictory keyboard order.
- Do not create separate LTR/RTL Pattern variants; make the composition direction-aware and test mixed-direction labels and long Persian text.
- Any selection marker's exact edge and token treatment belongs to its owning collection-item component or a separately approved item-active contract, not an invented Pattern-level variation.

## Accessibility contract

Apply the reviewed Accessibility Core and specialized Focus Management, Structure/Navigation, Responsive/Zoom and Dynamic Feedback documents.

**MUST**
- Preserve keyboard-operable item activation, correct accessible names, meaningful current/selected relationship and visible focus independently of active-detail styling.
- Do not trigger major navigation just because an element receives focus.
- Keep Collection and Detail discernible as meaningful labelled regions when this aids orientation; use appropriate native elements/landmarks without unnecessary nested landmark proliferation.
- Avoid a focus loss when the currently focused item disappears, or when narrow navigation removes/replaces the previous view.
- Ensure hidden drill-in views are not exposed as interactive focus targets.
- Preserve meaningful reading order, zoom/reflow and RTL context; do not rely on color alone to signal current detail.

**SHOULD**
- On wide in-place detail updates, normally keep focus on the active Collection item and expose important status changes without repetitive announcement noise.
- On deliberate narrow drill-in, position focus at an appropriate new-view heading or first task target; when returning, restore focus to the invoker if possible.
- Label the current item in a way compatible with its actual semantics (navigation current, active description, or selection as appropriate). Do not invent a global ARIA grid/listbox role for all List–Detail compositions.
- Test independent scroll areas, sticky headers, detail updates, long Persian strings, and Back with keyboard and screen readers.

**Unverified:** exact keyboard/screen-reader runtime behavior and component-specific current-item semantics need implementation and assistive-technology evidence before release.

## Figma reference and reconciliation

**Live draft pattern page:** [List–Detail / HOS-55 Presentation](https://www.figma.com/design/rROD8ctH9UfPGAMrRrOzHe/-DS--Job-Vision-NEXT?node-id=24988-3948).

Examples currently included:
- Wide RTL / Structured List + Detail, using connected canonical Structured List instance.
- No-selection, loading and unavailable-detail state examples (conceptual compositions).
- Data Table + Detail using connected Data Table instance; its component remains a design pilot.
- Narrow Collection and Detail drill-in screens (connected source instance in Collection).
- Pattern vs Component vs Product ownership boundary.

**Known presentation limits:** sample text in the current Structured List source is generic; neither the current-item visual treatment nor real product-specific routing is finalized by these mockups. The examples are editable composition references, not executable prototypes or proof of Storybook parity.

### Review gates before adoption

1. Owner approves distinction between current detail and Data View selection.
2. Confirm whether canonical current-item presentation should be added to an owning Collection component, not to this Pattern.
3. Review usable Collection/Detail minima in at least one real JobVision application, and test the corresponding responsive transition.
4. Validate initial selection, stale selection and Back behavior with a Product owner.
5. Confirm Drawer compatibility only after its component contract has been reconciled.
6. Test keyboard, screen-reader, RTL, reflow and scroll behavior against a representative implementation.
7. Reconcile Figma visual decisions with this document; regenerate repository indexes and pass governance checks before merge.

## Implementation and governance status

This document is a **proposal**, not a released component, new runtime package, or completed accessibility certification. Product-specific rules and live Storybook code have not been validated. Follow [Change Process](../../governance/change-process.md), including generated registry and accessibility checks, before review approval and merge.
