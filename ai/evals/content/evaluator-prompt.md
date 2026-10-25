# Content semantic evaluator prompt — v1

Evaluate exactly one JobVision content case against the supplied Design Language
policy context from the repository commit named in the task.

## Boundaries

- Judge only the supplied case.
- Apply only rules present in the supplied policy context.
- Do not infer product behavior, lifecycle, permissions, runtime support, or
  recoverability from the copy alone.
- Treat Product Knowledge as the owner of product facts.
- Treat the fixture's expected answer as hidden evaluation data; it must never
  be included in the model input.
- A missing product fact is a gap, not permission to invent one.

## Output

Return one JSON object and no surrounding prose:

```json
{
  "case_id": "suite::case",
  "valid": false,
  "violations": ["RULE-001"],
  "rationale": "Concise evidence-based explanation.",
  "corrected_example": {
    "label": "Corrected content"
  },
  "unsupported_product_or_runtime_claim": false
}
```

Requirements:

- Copy `case_id` exactly from the task.
- `valid` is true only when no checked rule is violated.
- `violations` contains rule identifiers only and has no duplicates.
- `rationale` is required for every case.
- `corrected_example` is required when invalid and must be `null` when valid.
- Set `unsupported_product_or_runtime_claim` to true when the evaluated answer
  invents or overstates a product/runtime fact not established by the supplied
  context.
