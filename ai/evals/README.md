# Semantic evals

These cases test whether AI-produced guidance follows stable Design Language
rules. They are not browser tests, Storybook stories, or product runtime data.

Product-specific scenarios belong with Product Knowledge or the Product
Development Harness unless they test a reusable Design Language contract.

**Execution status:** These YAML cases are curated evaluation **fixtures**. They are not currently run end-to-end against an AI model by `.github/workflows/knowledge-quality.yml`. Existing `tooling/validators/check_content_*.py` scripts enforce related deterministic content rules, but that is **not** the same as scoring generated AI answers against this case suite. Record any future evaluator, model/configuration, date, score and failing cases separately, after the runner is implemented and reviewed; do not invent a pass rate.
