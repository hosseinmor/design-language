# Evolve the system

Use this playbook when a reusable rule, token, component, pattern, or expression
needs to change.

1. Identify the owning canonical document and the live source that proves the
   change.
2. Decide whether the change is shared, a product-expression variation, or
   product-specific behavior that belongs in Product Knowledge.
3. Update design intent and acceptance criteria here; update Figma and Karbon in
   their owning repositories.
4. Add or update semantic evals and deterministic validators when the contract
   can be checked mechanically.
5. Regenerate the registry, run validation, and record migration/deprecation
   only when consumers need it.

Temporary implementation handoffs and dated audit reports remain in the work
tracking system or delivery PR, not in the canonical corpus.
