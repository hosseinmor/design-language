---
id: design-system.token.usage-rules
collection: design-system
type: token
title: Token Usage Rules
summary: '> Status: draft'
knowledge_state: unverified
document_maturity: draft
related: []
---

# Token Usage Rules

> Status: draft

## Allowed usage

- Components consume Semantic Color tokens by default; use an approved Component Color token only for its documented owner component.
- Treat Product and Appearance as independent Theme dimensions.
- Use Semantic `surface/*` for general UI backgrounds, including the root page/workspace.
- The approved Tag component uses its own `tag/*` Color family by exception.
- Test supported Product × Appearance combinations for accessibility.
- A shared Primitive value does not merge semantic meaning. Choose tokens by role, not by visual color.

The current logical Theme values are:

```text
Product    → JobVision | Cando
Appearance → Light | Dark
```

These logical dimensions do not prescribe the final Figma collection/mode implementation.

## Surface selection

- Ordinary root page, in-flow container, card, panel, or structural sheet → `surface/default`
- Passive lower-emphasis supporting or grouping region → `surface/muted`
- Region behind the local default surface, such as recessed workspace structure or chrome → `surface/inset`
- Surface visually elevated above its immediate parent, such as a menu, popover, dropdown, floating panel, or appropriate dialog → `surface/raised`
- High-contrast inverted region → `surface/inverse`
- Visible neutral interactive treatment with medium emphasis → `surface/neutral-muted`
- High-emphasis neutral operational action → `surface/neutral-emphasis`
- Transparent-at-rest interaction → `surface/transparent-hover/active`
- Transparent interaction on inverse surface → `surface/transparent-inverse-hover/active`
- Persistent selected row/item/container → `surface/selected`; add `surface/selected-hover` only if the selected container remains interactive
- Approved Brand conversion or product-defining moment → `surface/brand*`
- General chromatic interaction/affordance → matching `surface/accent-*`, `fg/accent`, or `line/accent`
- AI-assisted/generated treatment → matching Magic roles
- Destructive action or destructive-intent callout → matching Danger roles
- Validation or system feedback → matching Support muted surface, foreground, and line roles
- Disabled filled control → `surface/disabled + fg/disabled`

`surface/raised` expresses the Color role of an elevated layer. For a temporary floating surface that needs visible depth, pair it with the approved `Shadow/Floating` recipe. Do not add shadow merely because a surface uses `surface/raised`; scrim-backed Modal/Dialog surfaces and in-flow surfaces follow the Elevation Foundation rules.

Do not use structural `surface/muted` as an interactive control background. Use `surface/neutral-muted` instead.

## Foreground hierarchy

Choose neutral foregrounds by information role, not by how light you want the text to look.

```text
fg/primary
→ essential/default readable content

fg/secondary
→ supporting readable content that contributes to understanding

fg/tertiary
→ auxiliary low-priority metadata that may recede during scanning
```

Examples:

```text
Job title / candidate name / input value
→ fg/primary

Company / location / field label / helper text
→ fg/secondary

Timestamp / passive count / character counter
→ fg/tertiary
```

Do not use `fg/tertiary` as a generic “make this lighter” option.

Use `fg/placeholder` only for placeholder-like input content and `fg/disabled` for unavailable content/control styling.

## Line hierarchy

```text
line/muted
→ subtle structural separation

line/default
→ normal control/container boundary

line/emphasis
→ stronger neutral interactive boundary
```

A Text Input is a canonical stress-test example:

```text
Rest border  → line/default
Hover border → line/emphasis
Focus        → line/emphasis + focus/default ring
Error border → line/error
Disabled     → line/disabled
```

Operation-progress lines share one contract: neutral unfilled path → `line/default`; active arc/segment (including 100%) → `line/accent`; complete settled Success/Error → `line/success` / `line/error`. This applies to Progress Circle and Progress Bar without changing their existing token scopes. It does not turn status text or icons into line roles. `line/inverse` remains restricted to an inverse surface.

Focus remains a separate semantic layer; `line/emphasis` does not replace `focus/default`. This Color document owns token-role selection only. Shared Focus visibility, geometry, state composition, and runtime/Figma treatment are owned by `accessibility/focus-management.md`.

## Brand versus Accent

Use Brand when the reason for color is Product identity or an approved key product/conversion moment.

Use Accent when the reason for color is general interaction or chromatic affordance.

Examples:

```text
Brand Button at approved conversion
→ surface/brand

Cando link
→ link/default

Selected line Tab indicator
→ line/accent

Saved bookmark
→ fg/accent

Operational Primary Button
→ surface/neutral-emphasis
```

Do not use Brand merely to make an operational action more prominent.

### Accent Muted versus Info

Use Accent Muted for a tonal **interactive/actionable** emphasis, such as:

- Applied Filter Chip
- Selected tonal chip/control
- Actionable or promotional banner where the user is invited to act

Use Support Info for a passive informational/system message.

Both may resolve from Blue primitives; the semantic distinction is the purpose of the UI.

## Selection

Selection is a component state, not a full global Color family.

Use Accent for a chromatic selected/current/checked cue when the component anatomy calls for one:

```text
selected line Tab → fg/primary + line/accent
checked checkbox  → surface/accent-emphasis + fg/on-color
saved bookmark    → fg/accent
applied filter    → surface/accent-muted* + appropriate fg/line
```

Use the dedicated neutral selected-container surface for persistent selected containers:

```text
selected row/item → surface/selected
```

Use `surface/selected-hover` only when that selected row/item/container remains interactive while selected, for example a selected menu/list/tree/navigation item.

Do **not** add selected-hover styling to a current Tab merely because Hover exists on unselected Tabs. If the selected Tab has no meaningful interaction, it has no Hover state.

Strong current/exclusive choices such as pill Tabs or Segmented Controls may use an existing Neutral Emphasis treatment when the component anatomy communicates selection clearly.

Do not invent `fg/selected`, `line/selected`, selected emphasis, inverse, disabled, or active families without a repeated cross-component need.

## Magic

Magic is reserved for AI-assisted, AI-generated, or explicitly magical product capability.

Canonical roles include:

```text
surface/magic-muted
→ subtle AI card, section, chip, or container

surface/magic-emphasis*
→ strong interactive AI action / entry point

fg/magic
→ AI icon, label, or inline emphasis

line/magic
→ AI outline/indicator when required by anatomy
```

Do not use Magic merely as a decorative purple treatment and do not substitute it for Brand, Accent, Selected, or Support meaning.

## Danger versus Error

Keep destructive intent separate from system/validation failure:

```text
Danger
→ destructive action or pre-action destructive warning

Error
→ validation failure or system/problem state
```

Examples:

```text
“This action permanently deletes the job.”
→ surface/danger-muted + Danger roles

“Saving failed. Try again.”
→ surface/error-muted + Error roles
```

Danger is not a standard Notification severity alongside Info / Success / Warning / Error.

## Links

Default Link is the recognizable chromatic navigation treatment:

```text
link/default
link/hover
```

Use the neutral Subtle Link only when context already makes clickability clear:

```text
link/subtle
link/subtle-hover
```

Typical Subtle contexts include dense ATS UI, navigation, metadata, and “View all” patterns. Do not use Subtle as the normal inline body-copy Link unless another persistent affordance such as underline preserves recognition.

Use the single inverse Link family on `surface/inverse`:

```text
link/inverse
link/inverse-hover
```

Link Focus uses shared Focus semantics rather than Link-specific focus tokens:

```text
Default / Subtle Link → focus/default
Inverse Link          → focus/inverse
```

Do not use `link/visited` unless a future reviewed product pattern establishes a persistent visited-state need.

## Disabled

Disabled suppresses tone by default.

```text
Brand filled disabled
Primary disabled
Secondary disabled
Danger Filled disabled
→ surface/disabled + fg/disabled
```

Outline disabled treatments use `fg/disabled + line/disabled`; transparent disabled treatments use `fg/disabled`.

Do not create tone-specific disabled colors merely to preserve the original tone. Disabled has no hover or active state.

Read-only is not Disabled. Do not use `fg/disabled` merely because a field cannot be edited; read-only behavior and visual treatment belong to the component/form-field contract.

## Support and notifications

Standard system-feedback severities are:

```text
Info
Success
Warning
Error
```

A baseline inline-notification treatment may use:

```text
surface/{severity}-muted
fg/{severity}      # status icon/content
line/{severity}    # only if the anatomy includes a semantic border
fg/primary         # title/main text
fg/secondary       # description
```

Only muted Support surfaces are approved globally. Do not generate strong Support surface matrices without a repeated use case.

### Support on inverse surfaces

The inverse Support foreground roles are intentionally narrow:

```text
fg/info-inverse
fg/success-inverse
fg/warning-inverse
fg/error-inverse
```

Use them for colored Support content on `surface/inverse`, specifically patterns such as an inverse Toast:

```text
Toast container → surface/inverse
Toast text      → fg/on-inverse
Status icon     → fg/{severity}-inverse
Action Link     → link/inverse
```

Their existence does not justify Support inverse surfaces or inverse line families.

## Utility roles

Approved utility Color roles are:

```text
overlay/default
skeleton/base
skeleton/shimmer
```

The proposed `highlight/default` and `highlight/inverse` roles are removed. A future text/search highlighting pattern must establish a concrete shared use case before Highlight semantics are added.

## Prohibited usage

- Do not consume Primitive or Brand variables directly from ordinary component implementations.
- Do not encode Product or Appearance names into Semantic token names.
- Do not restore `canvas` or an Experience Color collection without a new demonstrated need.
- Do not use removed v3 names for new work: `surface/control*`, `surface/emphasis*`, `surface/brand-muted`, `fg/brand`, `line/brand`, expanded `surface/selected-*`, `fg/selected`, `line/selected`, `fg/on-color-disabled`, `link/emphasis*`, or `link/visited`.
- Do not restore `highlight/*` without a reviewed highlighting use case.
- Do not invent hover/active states for passive or disabled surfaces.
- Do not treat selected-hover as universal; only interactive selected containers receive it.
- Do not use Tag tokens as a generic palette for other components.

## Fallbacks

- Appearance mappings must resolve the active Brand input when Brand meaning is required.
- A Semantic role that does not vary by Product may alias a Primitive directly.
- If a proposed value fails accessibility, choose a contrast-safe approved mapping rather than binding a component to an arbitrary Primitive.
- If a future product needs a different Accent hue, add the minimum product-aware alias without changing the public Semantic role names.

## Migration history

Historical v3→v4 migrations are recorded in Git history. Follow the active semantic role definitions in [`semantics.md`](semantics.md), the current aliases in [`aliases.md`](aliases.md), and the system architecture in [`architecture.md`](architecture.md). Do not apply obsolete renaming instructions to current components.
