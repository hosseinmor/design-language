# Content foundation

This directory contains reusable language decisions for JobVision and Cando:

```text
content-guidelines.md     Human entry point and routing
product-voice.*           Shared voice and machine-readable contract
localization.*            Persian, RTL, formatting, and localization rules
terminology/              Shared semantic lexicon
components/               Copy contracts for reusable UI components
patterns/                 Reusable message and interaction-language patterns
```

Semantic regression cases live under `ai/evals/content/`. Product- and
audience-specific business terminology stays in Product Knowledge; it is loaded
at use time and is not mirrored here.

## Source boundary

```text
Product Knowledge
→ What a product concept means and how it behaves

Content foundation
→ How shared interface concepts are named and communicated

Karbon / Storybook
→ Exact runtime behavior and rendered implementation
```

## Validation

```bash
python tooling/validators/check_content_terminology.py
python tooling/validators/check_content_localization.py
python tooling/validators/check_content_components.py
python tooling/validators/check_content_patterns.py
python tooling/generate_manifest.py check
```
