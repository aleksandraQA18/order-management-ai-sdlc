---
name: bdd-scenarios
description: Create implementation-independent BDD scenarios for complex business behavior when concrete examples improve shared understanding.
argument-hint: "[Story]"
---

# BDD Scenarios

Create BDD scenarios only when requested by QA Analysis or when the Story clearly benefits from example-based behavioral specification.

## Purpose

BDD scenarios are primarily:
- a shared communication language;
- concrete examples of expected business behavior;
- a bridge between requirements and testable behavior.

They are not automatically an automation specification.

## When to Use

Use BDD when the Story contains:
- multiple business rules;
- meaningful exceptions;
- decision paths;
- interactions between business conditions;
- behavior that is easier to understand through examples.

Do not use BDD for simple CRUD or straightforward validation when ordinary verification scenarios communicate the behavior clearly.

## Scenario Design

Use concrete business examples with:

- Given — relevant starting state;
- When — meaningful business action;
- Then — observable expected behavior.

Keep scenarios implementation-independent.

Do not include API paths, request payload structures, HTTP status codes, classes, methods, database types, or framework details unless the project explicitly uses executable BDD.

Avoid duplicating nearly identical scenarios. Prefer representative examples that cover distinct business rules and outcomes.

## Output

Return only the BDD scenarios and a brief note when an important ambiguity prevents a scenario from being defined accurately.
