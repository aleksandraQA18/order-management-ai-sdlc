---
name: backend-testing
description: Add focused backend unit tests for approved Verification Targets when unit-level evidence is appropriate.
argument-hint: "[Story and QA Quality Contract]"
---

# Backend Testing

Add only backend unit tests that provide useful evidence for approved QA Verification Targets.

## Selection

Use unit tests for isolated:
- business rules;
- validation;
- transformations;
- deterministic calculations;
- domain/service behavior.

Do not use unit tests as substitutes for API, integration, or E2E verification.

Do not create tests only to increase count or coverage.

## Design

Prefer observable outcomes, meaningful assertions, focused data, deterministic execution, and existing fixtures/helpers.

Avoid implementation-detail assertions unless they protect meaningful behavior.

## Mocking

Mock only boundaries that must be isolated.

Do not mock the behavior being verified. Avoid excessive mocking that makes tests validate mocks rather than application behavior.

## Existing Tests

Update relevant tests when behavior changes. Preserve valid regression coverage.

Do not delete or weaken a failing test merely because implementation currently fails it.

## Validation

Run relevant backend tests/checks and report failures honestly. Do not use arbitrary retries or excessive timeouts to hide instability.

## Output

Report:
- tests added/updated;
- Verification Targets covered;
- checks/results;
- remaining gaps or `OPEN` issues.
