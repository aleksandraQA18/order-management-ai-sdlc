---
name: test-strategy-and-level-selection
description: Evaluate whether existing verification uses appropriate test levels based on risk, feedback speed, stability, scope and the Test Pyramid as a heuristic rather than a rigid rule.
argument-hint: "[Behavior / Test Suite]"
---

# Test Strategy and Level Selection

## Purpose

Review whether an existing verification approach uses an appropriate test level for the risk it is intended to control.

This skill is for reviewing test-level decisions already made during QA analysis or implementation.

It does not design the complete test strategy or generate new test cases.

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

## Review the Existing Decision

For each relevant behavior:

1. Identify the risk being protected.
2. Identify the current test level.
3. Determine whether that level provides meaningful confidence.
4. Check whether lower-level verification already provides equivalent confidence.
5. Determine whether the current higher-level test adds integration or journey confidence.
6. Consider feedback speed, stability and failure diagnosis.

Do not redesign the entire suite when the existing decision is adequate.

## Test Pyramid

Treat the Test Pyramid as a heuristic:

- many focused lower-level tests;
- fewer broader integration tests;
- a smaller set of valuable E2E tests.

Do not enforce a fixed numerical ratio.

A critical integration behavior may legitimately require higher-level coverage.

The pyramid is a guide for test economics and risk distribution, not a compliance target.

## Avoiding Redundancy

Multiple test levels can be appropriate when they verify different risks.

Example:

- unit test verifies a pricing rule;
- API test verifies the service exposes the correct result;
- E2E verifies that a user can complete the critical purchase flow.

Do not flag these as duplicates automatically.

Conversely, if several E2E tests repeat the same business rule already thoroughly verified at lower levels without adding meaningful system confidence, consider whether the suite is unnecessarily expensive and fragile.

## Testability

Consider whether the chosen level makes the existing test:

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

When challenging an existing test-level decision, explain:

- current level;
- recommended level, if a change is justified;
- risk being protected;
- evidence supporting the recommendation;
- confidence gained or lost;
- stability/feedback implications;
- whether the existing test should remain as additional coverage.

Do not recommend moving a test solely to conform to the pyramid.
