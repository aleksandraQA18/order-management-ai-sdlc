---
name: bdd-scenarios
description: Create minimal business-readable BDD scenarios for selected Verification Targets when examples materially improve understanding.
argument-hint: "[Verification Target or Story]"
---

# BDD Scenarios

Use only for Verification Targets selected by QA Analysis.

## When to Use

Create scenarios only when they clarify:
- critical business behavior;
- high-risk business rules;
- meaningful negative behavior;
- important cross-component business flows.

Do not create BDD for every endpoint, technical check, database constraint, or simple validation.

If BDD adds no value, produce no scenarios.

## Scenario

```text
Feature: [business capability]

Scenario: [observable behavior]
Given [context]
And [additional context when needed]
When [business action/event]
Then [observable outcome]
And [additional outcome when needed]

Traceability:
AC: [AC-XX]
Risk: [R-XX]
Verification Target: [VT-XX]
```

## Rules

- Use business language and observable outcomes.
- Keep one primary behavior per scenario.
- Do not mention classes, functions, files, selectors, database internals, or test frameworks.
- Use Scenario Outline only when multiple examples materially improve clarity.
- Do not invent AC, Risk, or Verification Target identifiers.
- Do not redefine requirements or expand scope.
- Do not prescribe automation.
- Keep the scenario count minimal and justified.
