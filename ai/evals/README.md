# Semantic evals

These cases test whether AI-produced guidance follows stable Design Language
rules. They are not browser tests, Storybook stories, or product runtime data.

Product-specific scenarios belong with Product Knowledge or the Product
Development Harness unless they test a reusable Design Language contract.

**Execution status:** These YAML cases are curated evaluation **fixtures**. They are not currently run end-to-end against an AI model by `.github/workflows/knowledge-quality.yml`. Existing `tooling/validators/check_content_*.py` scripts enforce related deterministic content rules, but that is **not** the same as scoring generated AI answers against this case suite. Record any future evaluator, model/configuration, date, score and failing cases separately, after the runner is implemented and reviewed; do not invent a pass rate.

## Evaluator contract

A future semantic runner must evaluate each fixture independently against the
exact Design Language commit under test. For every case it must return
machine-readable output containing:

- the case identifier;
- `valid` or `invalid`;
- detected rule violations;
- a concise rationale; and
- a corrected example when the case is invalid.

The report must record repository commit, model and version, prompt/evaluator
version, decoding configuration, execution date, and every failing case. Report
rule-level precision and recall, false-positive rate on valid cases, and the
rate of unsupported product or runtime claims.

Start in report-only mode. A score must not block merging until the content
owner approves the evaluator, representative pilot set, thresholds, and
acceptable variance. Deterministic validators remain required even after the
semantic runner exists.
