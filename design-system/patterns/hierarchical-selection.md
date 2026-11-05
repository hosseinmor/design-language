---
id: design-system.pattern.hierarchical-selection
collection: design-system
type: pattern
title: Hierarchical Selection
summary: Choosing values from a tree-shaped option set where any node is selectable; control choice, exact vs inclusive scope, and composition edge cases. Rendering and interaction are owned by Select › Hierarchical options.
knowledge_state: verified
document_maturity: reviewed
related:
  - design-system.component.select
  - design-system.component.tree-view
  - design-system.pattern.search-and-filtering
  - design-system.accessibility.forms
---

# Hierarchical Selection

> **Reviewed 2026-11-05.** Decisions come from the ATS Branch (شعبه) review, an interactive prototype and a Figma review, and are built in the canonical Select sources. Runtime behavior is not yet tested in Sandbox.

This pattern owns **which control to use and what a selection means**. How hierarchical options are drawn and behave (indent and guides, indicator position, structure-preserving search, cascade states, trigger display, focus) is owned by [Select › Hierarchical options](../components/select.md#hierarchical-options). Do not restate those rules here.

## Problem and Use

Some option sets form a tree in which **parent nodes are real, selectable values**, not just category labels. Examples are an organization's branches, where a parent branch owns jobs and requests of its own, or regions that contain sub-regions.

Use this pattern when:

- options have a parent/child relationship the user needs in order to understand or tell options apart, **and**
- any node, not only leaves, can be a committed value.

Do **not** use it when:

- parents are only labels: use Select with **Option Group Headers**;
- the hierarchy has no bearing on the choice: use a flat Select;
- parent and child must be chosen independently in a multiple selection: the data is being treated as flat, so use a flat Multiple;
- the task is to **manage** the structure (add, move, rename nodes): that belongs to [Tree View](../components/tree-view.md) on a management surface, not to a form field.

## Structure / Flow

### Choosing the control

| Situation | Control | Notes |
|---|---|---|
| Parents are category labels only | Select + Option Group Header | Existing Select contract |
| One node, any node selectable | **Select / Single, hierarchical options** | Default for form fields and single-scope filters |
| Several nodes, a parent implies its descendants | **Select / Multiple, hierarchical options (cascade)** | Default for multi-scope filters |
| Several nodes chosen independently of hierarchy | Flat Select / Multiple | Independent hierarchical multi-select is not supported in v1 |
| Managing the structure itself | Tree View | Scaffold, not approved |
| Only leaves selectable, many levels | Drill-down panel, if ever approved | Unsuitable when parents are selectable: hides siblings and needs a separate "select this level" row |

Collapsible trees inside a form field are not used: an always-expanded list with structure-preserving search replaces expand/collapse, and each row keeps a single select target.

### Data model (shared with Select and future Tree View)

- Each option has a stable `id`, a `label`, and `parentId` or a derived `level` (0 = root).
- Options are presented in **depth-first tree order**: each parent is followed immediately by its descendants. Sibling order comes from the data provider.
- Identity is always the `id`. Labels may repeat under different parents.
- A tree may have more than one root.

## Rules and States

### Exact vs inclusive scope

The consumer **must** choose the meaning explicitly; it is never inferred from the data.

1. **Exact** (typical for form fields): the committed value is exactly the selected node. Example: the branch a job belongs to.
2. **Inclusive** (typical for single-scope filters): the committed value is one node, interpreted as the node and all its descendants. The scope is made visible in the trigger and stated once in the field helper (see Select); it is **not** repeated on rows. Scope size, such as "7 branches in scope", belongs in the filtered result.
3. **Cascade** (Multiple): choosing a parent selects its subtree, and a parent with a partly selected subtree is indeterminate. Because the parent is a value in its own right, removing one child leaves the parent selected. Cascade is the only hierarchical Multiple mode in v1.

### Composition edge cases

| Case | Behavior |
|---|---|
| Hierarchy feature not enabled for the account | Hide the field; do not show a single-option Select |
| Exactly one option available to the user | Auto-commit it and render the field Read only |
| Context provides a sensible default (e.g. the user's own node) | Pre-select it; the user can change it within their available subtree |
| Dependent fields (options filtered by this value) | When this value changes, reset dependent values that are no longer valid and tell the user briefly |
| Value locked after a lifecycle event | Render Read only with the parent shown, per the Select trigger rule |

Which of these apply, and to which feature, is Product-owned (see Live References).

## Components

- **[Select](../components/select.md)** Single and Multiple with hierarchical options: owns rendering, search, cascade states, trigger display and focus.
- **[Breadcrumb](../components/breadcrumb.md)**: owns the `/` path separator reused by Select.
- **[Tree View](../components/tree-view.md)** (scaffold): structure management. Not a form-field replacement.

## Accessibility

Composition-level requirements only; component mechanics are in Select.

- Do not switch the popup to `role="tree"` only to show hierarchy: an always-expanded indented list remains a listbox.
- Hierarchy must be available non-visually (full ancestor path per option), and inclusive scope must be part of the trigger's accessible value.
- Auto-committed Read only fields stay focusable and announce their value.

## Variations and Gaps

- **Collapsible hierarchy inside Select**: excluded from v1. Reconsider only with data showing trees where an expanded list plus structure-preserving search fails.
- **Independent hierarchical multi-select**: excluded from v1 (use flat Multiple).
- **Flat + path search**: a documented Select alternative for constrained width; its clearest layout is still open.
- **Long result lists in structure-preserving search**: many deep matches bring many context rows. Watch this in testing with large organizations.
- ***Proposed* values**: visual level cap, and any size threshold for choosing the flat alternative.
- **Open questions:** how common repeated labels and multiple roots are in current datasets; final Content wording for the inclusive qualifier and the helper.

## Live References

- Figma: Select page › `03 · Anatomy & composition` (`_Option / Indent`, Option with Indent and Indeterminate) and `02 · Playground › Playground / Hierarchical options`.
- Storybook / Code: TBD.
- Related Product Knowledge: ATS Organization Structure, Branch tree and HasBranch (`ats/organization/0_overview`); Operator access to role branch and descendants, OP-20 (`ats/operator/rule-access`); Hiring Request branch filter (inclusive) and branch immutability (`ats/hiring-request/rule-access`, `ats/hiring-request/entity-workflow`).
