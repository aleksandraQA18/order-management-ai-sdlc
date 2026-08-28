---
name: backend-testing
description: Implement focused backend unit tests for approved behavior, reusing existing coverage and following the QA Quality Contract.
argument-hint: "[Story]"
---

# Backend Testing

Use this skill when implementing or updating backend unit tests.

## Inputs

Use:

- approved Acceptance Criteria;
- approved QA Quality Contract;
- QA verification targets;
- existing backend tests;
- changed backend implementation;
- repository test conventions.

QA defines what requires verification.

The BE Developer determines how appropriate backend unit tests provide that verification.

## Test Selection

Before adding a test:

1. inspect existing relevant tests;
2. determine whether sufficient coverage already exists;
3. identify the behavior or risk that requires coverage;
4. select unit level when appropriate;
5. update existing tests when clearer than creating duplicates.

Do not create tests solely to increase test count.

## Unit Tests

Use unit tests for isolated backend logic such as:

- business rules;
- validation;
- transformations;
- deterministic calculations;
- domain logic;
- service behavior that can be isolated from external systems.

Keep tests focused and independent.

## Assertions

Assertions should verify meaningful outcomes.

Prefer:

- returned values;
- state exposed by the unit boundary;
- business rule outcomes;
- expected exceptions/errors;
- meaningful side effects.

Avoid assertions that merely mirror implementation structure.

Do not weaken assertions to make tests pass.

## Test Data

Use focused, representative data.

Where requirements contain meaningful boundaries or invalid classes, cover relevant partitions without unnecessary duplication.

Keep test data understandable and close to the behavior being verified.

## Mocks and Stubs

Mock or stub external dependencies when required to isolate the unit under test.

Avoid excessive mocking that makes tests verify mocks rather than application behavior.

Do not mock the behavior that the unit test is supposed to verify.

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

## Test-Level Boundary

Backend unit tests do not replace:

- API tests;
- integration tests;
- E2E tests;
- manual verification;

when those are required by the QA Quality Contract.

API, integration and E2E test implementation is outside this skill.

## Evidence

Record:

- tests added or updated;
- command used to run them;
- result;
- relevant limitations.

Never claim test execution without actual execution.

## Boundary

This skill defines how BE unit tests are implemented.

It does not define:

- overall QA strategy;
- API/integration/E2E test implementation;
- regression strategy;
- business requirements;
- system architecture.
