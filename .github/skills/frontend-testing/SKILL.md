---
name: frontend-testing
description: Add focused frontend unit or component tests for approved Verification Targets when frontend-level verification provides the right evidence.
argument-hint: "[Story and QA Quality Contract]"
---

# Frontend Testing

Implement only frontend tests that provide useful evidence for approved QA Verification Targets.

## Inputs

Use:

- approved QA Quality Contract;
- approved Acceptance Criteria;
- affected frontend behavior;
- existing frontend test patterns.

## Test Selection

Add a frontend test when the target is frontend behavior that is best verified at unit/component level.

Do not duplicate behavior better verified by:

- API tests;
- integration tests;
- E2E tests.

Do not create tests only to increase coverage or test count.

## Test Design

Prefer:

- observable behavior;
- meaningful assertions;
- deterministic tests;
- focused scenarios;
- existing project test utilities and patterns.

Avoid implementation-detail assertions unless they are necessary to protect a meaningful behavior.

## Mocking

Mock only the boundary needed to isolate the behavior under test.

Do not mock the behavior that the selected test level is intended to verify.

Prefer realistic fixtures and existing test helpers.

## Scope

- Do not change production behavior to make a test pass.
- Do not weaken assertions.
- Do not add unrelated refactoring.
- Do not create frontend tests for backend/infrastructure behavior.

## Validation

Run relevant frontend tests and checks.

Report failures honestly.

## Output

Report briefly:

- tests added/updated;
- Verification Targets covered;
- checks run and result;
- remaining coverage gaps or `OPEN` issues.

Do not add unrelated analysis.
