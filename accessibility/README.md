# Accessibility

This directory contains the operational accessibility knowledge for the JobVision/Cando Design System.

## Retrieval

For web design, frontend implementation, reusable component work, and accessibility review:

1. Load `core.md`.
2. Use `router.md` to select the smallest sufficient context.
3. A Component/Pattern guideline may encapsulate specialized mechanics only when its repository maturity metadata is reviewed/stable + canonical **and** the relevant accessibility behavior is actually defined with no known/open gap.
4. Otherwise continue to the relevant specialized accessibility documents.
5. Load `testing.md` when test/evidence scope is part of the task.

## Operational corpus

System-level:
- `core.md`
- `router.md`
- `conformance-and-policy.md`
- `component-accessibility-authoring-contract.md`

Specialized:
- `color-and-contrast.md`
- `focus-management.md`
- `keyboard-navigation.md`
- `screen-reader-semantics.md`
- `forms.md`
- `responsive-and-zoom.md`
- `pointer-touch-and-gestures.md`
- `dynamic-content-and-feedback.md`
- `motion.md`
- `content.md`
- `structure-and-navigation.md`
- `images-icons-and-media.md`
- `tables-and-data-visualization.md`
- `testing.md`

Stress tests, audit reports, reconciliation packages, and cold-audit evidence are validation inputs, not normal operational retrieval sources and are intentionally not stored as canonical accessibility knowledge here.

## Authority vs retrieval order

Rule ownership and task retrieval are intentionally different:

```text
Authority:
standards/conformance → Core → specialized owner → component/pattern contract → product composition → testing evidence

Retrieval:
task → Core → Router → mature component/pattern contract → unresolved specialized domains → Testing as needed
```
