---
name: bdd-scenarios
description: Create concise business-readable BDD scenarios from approved requirements and QA verification targets, preserving traceability without prescribing implementation.
argument-hint: "[Story]"
---

# BDD Scenarios

Use this skill when the QA analysis identifies behavior that should be specified as BDD scenarios.

## Preconditions

Before creating BDD scenarios:

- the Story exists;
- BA analysis and Acceptance Criteria are approved;
- System Analyst analysis is approved;
- QA analysis is completed;
- verification targets are identified.

Do not create BDD scenarios from unapproved or ambiguous requirements.

## Purpose

BDD scenarios describe observable system behavior using examples.

They should:

- clarify expected behavior;
- be understandable by business and technical stakeholders;
- provide concrete examples;
- support traceability to Acceptance Criteria and risks;
- be independent of implementation details.

BDD scenarios are specifications, not automatically automated tests.

## Scenario Selection

Create scenarios only for behavior identified by QA as requiring scenario-level verification.

Prioritize:

- critical business behavior;
- important business rules;
- high-risk behavior;
- meaningful negative cases;
- relevant boundary conditions;
- important cross-component behavior.

Do not create scenarios simply to increase test count.

Do not create scenarios for behavior that is out of scope.

## Scenario Structure

Use the standard structure:

Feature: [business capability]

Scenario: [specific behavior]

Given [initial context]
And [additional context when needed]
When [action or event]
Then [observable outcome]
And [additional outcome when needed]

Use:

- `Given` for relevant preconditions;
- `When` for the action or event;
- `Then` for observable outcomes.

Keep scenarios focused on one behavior.

Avoid unnecessary steps.

## Business Language

Scenarios should use domain and business language.

Avoid:

- class names;
- function names;
- database implementation;
- framework details;
- internal variables;
- UI selectors;
- HTTP implementation details unless the API behavior itself is the subject of the scenario.

Describe what the user or system observes, not how the software achieves it.

## Traceability

Every scenario should be traceable to an Acceptance Criterion.

Where relevant, also identify the associated risk or verification target.

Use:

| Scenario | Acceptance Criteria | Risk / Verification Target |
|---|---|---|
| | | |

Do not create scenarios that cannot be connected to approved behavior.

## Scenario Types

Consider:

### Happy Path

The expected successful behavior.

### Negative

Relevant invalid, rejected, failed, or exceptional behavior.

### Boundary

Behavior at meaningful limits or thresholds.

Use boundary scenarios when the boundary represents a real business or system risk.

Do not create separate scenarios for every possible invalid value.

## Scenario Outline

Use a Scenario Outline only when multiple examples exercise the same behavior and the examples materially improve clarity.

Avoid Scenario Outlines when they make the scenario harder to understand.

Prefer explicit scenarios when the business behavior differs between examples.

## Scenario Quality

Each scenario should be:

- specific;
- observable;
- deterministic;
- independently understandable;
- concise;
- testable;
- traceable.

Avoid:

- vague outcomes such as "system works correctly";
- multiple unrelated actions;
- implementation details;
- duplicated scenarios;
- unnecessary setup;
- hidden assumptions.

## Expected Outcomes

`Then` steps must describe observable outcomes.

Prefer:

- the user sees a validation message;
- the order is created;
- the request is rejected;
- the status changes;
- the expected notification is produced.

Avoid implementation-oriented outcomes such as:

- a method is called;
- a database row is inserted;
- a class returns a value.

Unless the implementation itself is the approved subject of verification.

## Open Questions

If required information is missing or ambiguous:

- do not invent the expected behavior;
- mark the issue as `OPEN`;
- explain what decision is required.

Do not create a BDD scenario based on an unapproved assumption.

## Boundary

This skill defines:

- which approved behavior should be expressed as BDD examples;
- how the behavior is expressed;
- how scenarios remain traceable to requirements and risks.

It does not define:

- test automation implementation;
- test framework;
- step definitions;
- test data generation implementation;
- CI configuration.

Automation implementation belongs to the relevant Developer or dedicated test implementation activity.
