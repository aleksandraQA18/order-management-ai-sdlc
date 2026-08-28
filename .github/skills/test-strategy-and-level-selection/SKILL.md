---
name: test-strategy-and-level-selection
description: Evaluate whether behaviors are verified at appropriate test levels using risk, feedback speed, stability, scope and the Test Pyramid as a heuristic rather than a rigid rule.
argument-hint: "[Behavior / Test Suite]"
---

# Test Strategy and Level Selection

## Purpose

Help determine the most appropriate level for verifying a behavior.

The objective is not to maximize lower-level tests.

The objective is to obtain reliable confidence at an appropriate cost and feedback speed.

## Test Levels

### Unit

Use for isolated logic and small deterministic behaviors.

Typical examples:

- calculations;
- domain rules;
- transformations;
- validation logic.

### Component

Use when behavior is best verified within a component boundary without requiring the complete system.

### API

Use for:

- API behavior;
- request/response contracts;
- service-level validation;
- business behavior exposed through an API.

### Integration

Use when confidence depends on interaction between meaningful system components.

Examples:

- service + database;
- service + external adapter;
- multiple internal components interacting.

### E2E

Use for critical user journeys and behavior that genuinely depends on the integrated system.

Do not use E2E simply because it is capable of testing the behavior.

## Test Pyramid

Treat the Test Pyramid as a heuristic:

- many focused lower-level tests;
- fewer broader integration tests;
- a smaller set of valuable E2E tests.

Do not enforce a fixed numerical ratio.

A critical integration behavior may legitimately require higher-level coverage.

## Selection Questions

For each behavior ask:

1. What risk are we trying to control?
2. What is the smallest test level that can provide meaningful confidence?
3. Does a higher-level test provide additional confidence?
4. Is the higher-level test duplicating lower-level coverage?
5. What is the expected feedback speed?
6. How stable is the test at this level?
7. How easy is failure diagnosis?
8. Does the behavior depend on real integration?
9. Is the behavior part of a critical user journey?

## Avoiding Redundancy

Multiple test levels can be appropriate when they verify different risks.

Example:

- unit test verifies a pricing rule;
- API test verifies the service exposes the correct result;
- E2E verifies that a user can complete the critical purchase flow.

Do not flag these as duplicates automatically.

Conversely, if several E2E tests repeat the same business rule already thoroughly verified at lower levels without adding meaningful system confidence, consider whether the suite is unnecessarily expensive and fragile.

## Testability

Consider whether the chosen level makes the test:

- deterministic;
- isolated enough;
- fast enough;
- diagnosable;
- maintainable.

A theoretically correct test at an inappropriate level may still create poor quality economics.

## Risk-Based Exceptions

Higher-level tests may be justified when:

- the failure mode exists only across component boundaries;
- configuration or integration is part of the risk;
- the behavior is a critical user journey;
- lower-level tests cannot provide equivalent confidence.

Lower-level tests may be insufficient when the risk specifically concerns integration.

## Review Output

When recommending a different test level, explain:

- current level;
- recommended level;
- risk being protected;
- confidence gained or lost;
- stability/feedback implications;
- whether the existing test should remain as additional coverage.

Do not recommend moving a test solely to conform to the pyramid.
