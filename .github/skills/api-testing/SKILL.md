---
name: api-testing
description: Design and review REST API verification for business behavior, contracts, validation, errors, state transitions and data isolation.
argument-hint: "[endpoint or API Story]"
---

# API Testing

Verify:
- status code,
- response body/schema,
- business rules,
- validation,
- error behavior,
- observable persistence effects,
- state transitions,
- data isolation.

Prefer API verification over E2E when UI adds no meaningful verification.

Avoid implementation-internal assertions and duplicate E2E coverage.
