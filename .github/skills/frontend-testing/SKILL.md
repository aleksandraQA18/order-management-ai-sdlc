---
name: frontend-testing
description: Implement focused frontend unit and component tests for approved behavior, reusing existing coverage and following the QA Quality Contract.
argument-hint: "[Story]"
---

# Frontend Testing

Use this skill when implementing or updating frontend unit and component tests.

## Inputs

Use:

- approved Acceptance Criteria;
- approved QA Quality Contract;
- QA verification targets;
- existing frontend tests;
- changed frontend implementation;
- repository test conventions.

QA defines what requires verification.

The FE Developer determines how appropriate frontend unit/component tests provide that verification.

## Test Selection

Before adding a test:

1. inspect existing relevant tests;
2. determine whether sufficient coverage already exists;
3. identify the behavior or risk that requires coverage;
4. select unit or component level when appropriate;
5. update existing tests when that is clearer than creating duplicates.

Do not create tests solely to increase test count.

## Unit Tests

Use unit tests for isolated frontend logic such as:

- pure functions;
- transformations;
- validation logic;
- deterministic state logic;
- other behavior that can be verified without rendering a component.

Keep unit tests focused and independent.

## Component Tests

Use component tests for behavior that depends on rendering and user interaction, such as:

- rendering important states;
- user interactions;
- validation feedback;
- conditional UI behavior;
- loading and error states;
- callbacks and observable component behavior.

Prefer testing behavior visible at the component boundary rather than implementation details.

## Assertions

Assertions should verify meaningful outcomes.

Prefer:

- visible behavior;
- emitted events;
- state exposed through the UI;
- user-observable results;
- important contract boundaries.

Avoid assertions that merely mirror internal implementation structure.

Do not weaken assertions to make tests pass.

## Test Data

Use focused, representative data.

Where a requirement contains meaningful boundaries or invalid classes, cover the relevant partitions without creating redundant cases.

Keep test data understandable and close to the behavior being verified.

## Mocks and Stubs

Mock external dependencies when required to isolate the frontend behavior under test.

Avoid excessive mocking that makes tests verify mocks rather than application behavior.

Do not use mocks to bypass a verification target that requires a higher test level.

## Determinism

Tests should be:

- deterministic;
- isolated where applicable;
- repeatable;
- independent from execution order;
- free from unnecessary timing assumptions.

Do not hide instability with arbitrary retries or excessive timeouts.

## Existing Coverage

When implementation changes existing behavior:

- identify affected tests;
- update tests when behavior intentionally changed;
- preserve valid regression coverage;
- remove obsolete tests only when their behavior is no longer valid and the change is within approved scope.

Do not delete failing tests simply because the implementation currently fails them.

## Test Level Boundary

Frontend unit/component tests do not replace:

- API tests;
- integration tests;
- E2E tests;
- manual verification;

when those are required by the QA Quality Contract.

## Evidence

Record:

- tests added or updated;
- command used to run them;
- result;
- relevant limitations.

Never claim test execution without actual execution.

## Boundary

This skill defines how FE unit/component tests are implemented.

It does not define:

- the overall QA strategy;
- required regression scope;
- API/integration/E2E test implementation;
- business requirements;
- system architecture.
