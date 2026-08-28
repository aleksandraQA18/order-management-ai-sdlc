---
name: test-quality-and-flakiness
description: Evaluate automated test reliability, assertions, determinism, isolation, test data, synchronization, failure diagnosis and automation anti-patterns, with explicit handling of flaky-test risk.
argument-hint: "[Test Suite / Test]"
---

# Test Quality and Flakiness

## Purpose

Evaluate whether automated tests provide reliable and maintainable evidence.

A passing test is useful only when its result is trustworthy.

## Meaningful Assertions

Assertions should verify the intended behavior.

Avoid tests that:

- assert only that code executed;
- verify implementation details unnecessarily;
- use weak or overly broad assertions;
- pass even when the intended behavior is broken.

A test should fail when the behavior it protects is wrong.

## Determinism

Prefer tests whose outcome depends on controlled inputs and observable application behavior.

Watch for:

- current time;
- random values;
- network timing;
- thread scheduling;
- unordered collections;
- environment-specific behavior.

Where nondeterminism is required, control it or make the expected behavior explicit.

## Synchronization

Prefer waiting for observable conditions over arbitrary delays.

Risky patterns include:

- fixed sleeps;
- arbitrary retry counts;
- excessive timeouts;
- waiting for an implementation detail instead of application state.

Do not automatically classify every wait as a defect.

## Isolation

Tests should not depend unnecessarily on:

- previous tests;
- execution order;
- shared mutable data;
- leftover database state;
- global configuration;
- external test runs.

## Test Data

Prefer:

- explicit data;
- controlled setup;
- unique data when required;
- data that represents meaningful partitions.

Avoid dependence on uncontrolled shared fixtures.

## External Dependencies

Where external systems are part of the behavior being tested, use them deliberately.

Where they are not part of the risk, isolate them appropriately.

Do not introduce mocks simply to make tests easier if the real integration is what needs verification.

## Failure Diagnosis

A failed test should provide useful information about what went wrong.

Prefer:

- focused tests;
- clear assertions;
- meaningful test names;
- relevant failure messages;
- isolated setup.

Avoid large tests that verify many unrelated behaviors and produce ambiguous failures.

## Test Smells and Automation Anti-Patterns

Look for patterns that reduce trust, readability or maintainability, including:

- giant tests covering unrelated behaviors;
- duplicated setup or assertions without a clear reason;
- excessive conditional logic inside tests;
- assertions hidden in generic helpers;
- brittle selectors or incidental UI coupling;
- testing implementation details instead of observable behavior;
- excessive mocking that removes the integration risk being tested;
- overly generic test utilities that obscure intent;
- tests coupled through shared fixtures or global state;
- tests that are difficult to diagnose because failures are ambiguous.

A smell is not automatically a defect.

Report it when it creates a meaningful quality, reliability or maintenance risk.

## Flakiness Classification

Use three categories:

### Confirmed Flaky

There is repeated evidence that the same test passes and fails without a relevant product change.

### Flaky Risk

The implementation contains a credible instability mechanism, but repeated failure evidence is not available.

### Speculation

There is no sufficient evidence or credible mechanism.

Do not report speculation as a flaky-test finding.

## Flaky Test Remediation

Prefer fixing the source of nondeterminism.

Examples:

- replace fixed sleep with condition-based synchronization;
- control time;
- control randomness;
- isolate test data;
- remove order dependency;
- make asynchronous state observable;
- stabilize required external dependencies.

Do not hide flakiness through blind retries.

Retries may be appropriate only when the underlying transient failure model is understood and the retry policy is intentional.

## Review Rule

When identifying a flaky-test risk, explain:

1. what creates nondeterminism;
2. under what condition it can occur;
3. why CI/environment variation can expose it;
4. what evidence exists;
5. what change would make the test more deterministic.

When identifying a test smell, explain:

1. what pattern is present;
2. why it matters;
3. whether it is a defect, risk or learning note;
4. what improvement would address the underlying problem.
