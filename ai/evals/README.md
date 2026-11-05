# Semantic evals

These cases test whether AI-produced guidance follows stable Design Language
rules. They are not browser tests, Storybook stories, or product runtime data.

Product-specific scenarios belong with Product Knowledge or the Product
Development Harness unless they test a reusable Design Language contract.

**Execution status:** The YAML cases are curated evaluation **fixtures**. The repository now contains a report-only harness that validates fixtures, prepares answer-free model tasks, validates evaluator responses, and produces JSON/Markdown score reports. It does not call a model, store credentials, or run a semantic model evaluation in CI. Therefore no model pass rate exists until a reviewed model adapter executes the prepared tasks and its responses are scored. Existing deterministic content validators remain separate from semantic scoring.

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

## Report-only workflow

Validate every fixture deterministically:

```bash
python tooling/evals/run_content_semantic_eval.py validate
```

Prepare tasks for a reviewed model adapter. Expected answers are deliberately
excluded from this JSONL file:

```bash
python tooling/evals/run_content_semantic_eval.py prepare \
  --repository-commit <commit-sha> \
  --output /tmp/content-semantic-tasks.jsonl
```

Run each task with the policy context from the exact commit and
[`evaluator-prompt.md`](content/evaluator-prompt.md), then save one response
object per line. Score the responses:

```bash
python tooling/evals/run_content_semantic_eval.py score \
  --responses /tmp/content-semantic-responses.jsonl \
  --repository-commit <commit-sha> \
  --model <model-name> \
  --model-version <model-version> \
  --decoding-config-json '{"temperature": 0}' \
  --report-json /tmp/content-semantic-report.json \
  --report-markdown /tmp/content-semantic-report.md
```

Use `--allow-partial` only for an explicitly labelled pilot. Semantic
mismatches never make this command fail: the report is non-blocking. Invalid
fixtures, malformed responses, duplicate case IDs, or incomplete coverage
without `--allow-partial` are execution failures and return a non-zero status.

The model adapter is intentionally outside this first version. Adding one
requires an explicit model/configuration decision, secret handling outside the
repository, and content-owner review. CI runs fixture validation and unit tests,
not model inference.
