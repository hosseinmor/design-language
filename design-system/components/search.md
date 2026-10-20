---
id: design-system.component.search
collection: design-system
type: component
title: Search
summary: Search captures a single-line query through an RTL-first search-specific control with a fixed search affordance and a contextual clear action.
knowledge_state: verified
document_maturity: draft
related:
- design-system.component.text-input
- design-system.accessibility.forms
- design-system.accessibility.component-authoring-contract
design_status: ready-for-dev
design_maturity: handoff-ready
---

# Search

## Purpose

Search captures a single-line query used to find, filter, or narrow content.

Search shares the Text Input control foundation for sizing, surface, border, focus, typography, and native text-editing behavior, but is a separate public component because it owns two search-specific affordances:

- a fixed Search icon at the leading edge;
- a contextual Clear action when a query exists.

Do not rebuild Search as an arbitrary Text Input with ad-hoc icons.

## When to Use

Use Search when the entered text is a query that filters or retrieves content, such as:

- searching a list or table;
- searching a directory or catalogue;
- filtering visible results by free text;
- searching within a page or product area.

## When Not to Use

Do not use Search when:

- the value is ordinary form data rather than a query → use Text Input;
- users choose from a known option set → use a selection component;
- the experience includes suggestions, autocomplete, command behavior, or a results popup with its own keyboard model → compose or define the relevant higher-level pattern;
- an icon-only control expands into a search box → use a separate expandable-search pattern rather than overloading base Search.

## Canonical Figma API

Component set: `Search`

Figma node: `22827:261` in `-DS--Job-Vision-NEXT`.

### Top-level properties

| Property | Values / behavior |
|---|---|
| `Size` | `Small`, `Medium`, `Large`; Medium is default |
| `State` | `Default`, `Hover`, `Focus`, `Disabled` |
| `Filled` | Boolean Figma-authoring switch; False shows Placeholder, True shows Query + Clear |
| `Placeholder` | Placeholder copy, preserved independently |
| `Query` | Search query copy, preserved independently |

`Filled` is a Figma authoring property only. Runtime presentation should derive from the actual query value.

## Anatomy

```text
Search
├── Clear action            ← trailing / left in RTL; query only
├── Content
│   ├── Placeholder
│   └── Query
└── Search icon             ← leading / right in RTL
```

The Search icon is fixed by the component and is not an arbitrary instance-swap slot.

The Clear action is also fixed by the component because it owns query-clearing semantics.

## Sizes and Geometry

| Size | Control height | Inline padding | Typography |
|---|---:|---:|---|
| Small | 32 px | 12 px | 14 / 20 |
| Medium | 40 px | 16 px | 14 / 20 |
| Large | 48 px | 16 px | 16 / 24 |

Shared geometry:

- Medium is default.
- Radius: 6 px.
- Search glyph: 16 px.
- Clear glyph: 16 px inside a 24 px action area.
- Gap between structural items: 8 px.
- Width is flexible.
- Placeholder and Query fill the available Content width in Figma and use single-line ending ellipsis when they overflow.
- Border and focus layers must not shift content.

### Legacy Expressive migration

Legacy Search exposed both `Large` and `Expressive` at 48 px.

Their geometry was equivalent; Expressive differed by using 16/24 text while Large used 14/20.

The canonical scale removes the duplicate name:

```text
legacy Expressive
→ canonical Large
→ 48 px + 16/24 typography
```

Legacy Large was only present in test-oriented usage during the HOS-16 audit. Canonical Large therefore adopts the established Expressive presentation used by real Header/Search instances.

## RTL and Directionality

Search is RTL-first for current JobVision/Cando products.

In RTL:

```text
left / trailing
Clear
← Query / Placeholder
← Search icon
right / leading
```

Rules:

- Search icon remains at the right/leading edge.
- Clear remains at the left/trailing edge.
- Small keeps 12 px inline edge spacing; Medium/Large keep 16 px.
- Placeholder and Query are right-aligned by default.
- Mixed Persian/English queries must remain usable without changing the semantic meaning of leading/trailing actions.

## State Model

### Default

- surface → `surface/default`
- line → `line/default`
- Query → `fg/primary`
- Placeholder → `fg/placeholder`
- Search icon → `fg/secondary`
- Clear action → `fg/secondary`

### Hover

- line → `line/emphasis`
- geometry remains unchanged.

### Focus

```text
Control line → line/emphasis, 1 px
Focus indicator → focus/default, 2px ring + 1px offset
```

The focus indicator does not alter layout.

### Disabled

```text
surface → surface/disabled
line → line/disabled
content → fg/disabled
Search icon → fg/disabled
Clear action → fg/disabled
```

A disabled Search is unavailable for editing and clearing.

## Filled and Clear Behavior

```text
Filled = False
→ Placeholder visible
→ Clear hidden
→ Query retained in Figma but not displayed

Filled = True
→ Query visible
→ Clear visible
→ Placeholder retained in Figma but not displayed
```

Runtime must derive this behavior from the actual query value.

Clear is an interactive action in runtime:

- it clears the current query;
- it requires an accessible name;
- it must be keyboard operable when exposed as a separate button/action;
- it must not be available when the Search control is disabled;
- clearing behavior must preserve predictable focus according to the consuming search experience.

The exact post-clear focus/result-update policy belongs to the consuming Product/Pattern.

## Behavior

- Preserve native single-line text editing.
- Do not add Active/Pressed as a Search field state.
- Do not use Skeleton as a Search state.
- Do not expose a separate visual Fill style; the canonical control remains border-based.
- Query presence is content state, not a Figma variant axis.
- In Figma, Placeholder and Query are single-line, fill the available Content width, and truncate with ending ellipsis. Runtime editing may preserve native horizontal scrolling behavior.
- Search submission timing is not owned by the visual component.
- Enter-to-submit, instant filtering, debounce, network behavior, result count, empty state, and loading behavior belong to the consuming search experience.
- Suggestions/autocomplete/results popup are not part of base Search.

## Expandable Search

Legacy Search included `Expandable` and `Expanded` axes, including an icon-only collapsed state.

HOS-16 usage audit found only two collapsed expandable instances, both in Data Table contexts.

Base Search therefore does not include these axes.

Treat icon-only → expanded-search behavior as a separate pattern/component if those Data Table usages remain required.

Do not multiply the base Search variant matrix for this behavior.

## Semantic Color Mapping

| Part / state | Semantic role |
|---|---|
| Query | `fg/primary` |
| Placeholder | `fg/placeholder` |
| Search icon | `fg/secondary` |
| Clear action | `fg/secondary` |
| Default surface | `surface/default` |
| Default line | `line/default` |
| Hover / Focus line | `line/emphasis` |
| Disabled surface | `surface/disabled` |
| Disabled line/content/actions | `fg/disabled` / disabled semantic roles |
| Focus indicator | `focus/default` |

Search does not require a Search-specific Color-token family.

## Accessibility

Search is a native-input-oriented component with a contextual interactive Clear action.

### Input semantics

Prefer a native single-line input. Use native search-input semantics where they match the product behavior.

The input requires a meaningful accessible name even when the visual design does not include a persistent visible label.

Placeholder is not a sufficient accessible name by itself.

Product/Pattern owns whether the surrounding experience is also exposed as a search form/landmark.

### Keyboard and focus

- Preserve native text-input keyboard editing and browser shortcuts.
- Keep normal keyboard focus visible.
- Clear must be keyboard operable if represented as a separate interactive control.
- Disabled Search must not expose an operable Clear action.

### Clear action

Clear requires an accessible name equivalent to the localized concept of “Clear search”.

Do not rely on the Close glyph alone to communicate its purpose.

### Result behavior

Search component accessibility does not by itself define:

- when results update;
- how result counts are announced;
- autocomplete/listbox semantics;
- loading announcements;
- no-results messaging.

Those belong to the consuming search pattern and must be documented there.

### QA scenarios

Test:

- Empty / Filled;
- Small / Medium / Large;
- Focus and Disabled;
- keyboard editing and clearing;
- long Persian query;
- mixed Persian/English query;
- zoom/text enlargement;
- horizontal resizing;
- accessible name without relying on Placeholder;
- Clear accessibility and focus behavior.

## Development Contract

The exact Angular/package API is not yet registered as a canonical runtime source.

Implementation should support concepts equivalent to:

```text
Search
- size: sm | md | lg
- query/value
- placeholder
- disabled
- accessible-name mechanism
- clear action
- native input attributes
- search/change/submit callbacks as required by the consuming product
```

Do not model Figma-only authoring concepts as required runtime API:

```text
Filled → derive from actual query
Hover  → CSS/platform state
Focus  → CSS/platform state
```

Do not infer debounce, Enter behavior, API calls, or result rendering from the component itself.

## QA Checklist

Verify:

- exactly 12 Size × State variants exist;
- Medium is default;
- heights are 32 / 40 / 48 px;
- inline padding is 12 / 16 / 16 px;
- Large uses 16/24 typography;
- Small/Medium use 14/20 typography;
- Search icon is right/leading in RTL;
- Clear is left/trailing in RTL;
- Clear appears only when Filled=true;
- Filled preserves Placeholder and Query independently;
- Small/Large property bindings work after cloning;
- Focus uses line/emphasis + the shared 2px `focus/default` ring with a 1px offset;
- Disabled uses disabled semantic roles;
- Placeholder and Query fill Content and use single-line ending ellipsis in Figma;
- horizontal resize preserves padding, order, border, and clipping;
- no Fill-style, Skeleton, Expandable, Expanded, or Expressive axis exists in canonical Search.

## Figma Reference

Canonical editable source:

- Figma file: `-DS--Job-Vision-NEXT`
- File key: `rROD8ctH9UfPGAMrRrOzHe`
- Page: `Search`
- Page node: `453:14562`
- Documentation frame: `22884:126873`
- Header: `22884:126874`
- Variant matrix: `22884:126881`
- Axes & properties: `22884:126882`
- Component set: `Search`
- Component set node: `22827:261`
- Playground: `22884:126912`
- Examples: `22828:290`

Legacy Outline/Fill sets, Expandable/Expanded variants, Expressive naming, Skeleton states, and scratch instances were removed from the canonical Figma page.

## Code / Storybook Reference

No runtime component package or Storybook source is currently registered as canonical for Search.

Do not infer implemented Angular API, DOM structure, clear-button implementation, debounce behavior, or query-submission semantics from Figma alone.

## Open Items

- register the canonical runtime/Storybook source when available;
- align exact Angular/Tailwind public API with Frontend;
- migrate legacy Expressive usage to canonical Large;
- decide the migration solution for the two legacy expandable Data Table instances;
- validate any autocomplete/suggestion pattern separately if needed.

These open items do not block the base Search visual and authoring contract.

## Related Documents

- `./text-input.md`
- `../../accessibility/forms.md`
- `../../accessibility/component-accessibility-authoring-contract.md`
- `../tokens/color/semantics.md`
- `../tokens/color/usage.md`
