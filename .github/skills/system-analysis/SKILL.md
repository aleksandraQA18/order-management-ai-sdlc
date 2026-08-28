---
name: system-analysis
description: Analyze the current system, define affected components and system behavior, assess architecture, and create an implementation boundary without prescribing code-level implementation.
argument-hint: "[Story]"
---

# System Analysis

Use this skill when performing system-level analysis for the current Story.

## Analysis Flow

Follow this sequence:

1. Understand the approved business behavior.
2. Inspect the current system state.
3. Identify the affected system process or flow.
4. Identify affected components and their responsibilities.
5. Identify required system behavior changes.
6. Identify API and data impact where relevant.
7. Identify dependencies between affected components.
8. Assess architectural impact.
9. Identify risks, constraints and trade-offs.
10. Define the Implementation Map.
11. Identify documentation impact.
12. Identify unresolved questions and decisions.

## Current System State

Base the analysis on available evidence:

- Architecture Context;
- system and process documentation;
- source code;
- existing APIs;
- existing tests.

Use the evidence to distinguish current implementation from intended future behavior.

Clearly distinguish:

FACT:
...

INFERENCE:
...

PROPOSAL:
...

DECISION:
OPEN

Do not assume that existing implementation is automatically the desired behavior.

If implementation contradicts approved business requirements, identify the discrepancy and mark the required decision as `OPEN`.

## System Behavior

Describe the relevant system behavior, including:

- system flow;
- affected behavior;
- inputs and outputs;
- state changes;
- validation;
- error behavior;
- relevant dependencies.

Focus on observable system behavior and responsibilities rather than code-level implementation.

## Components

Identify application components affected by the Story.

For each component determine:

- why it is affected;
- what behavior must change;
- assess how the approved UI behavior maps to affected system components and APIs.
- whether the change is required or optional.

Do not include components based only on speculation.

Where possible, identify the responsible implementation area, such as:

- frontend application;
- backend service;
- API;
- persistence component;
- integration;
- shared component.

## Implementation Map

Create an Implementation Map that gives FE and BE Developers a clear implementation boundary.

Use:

| Component | Required change | Developer | Dependencies |
| --------- | --------------- | --------- | ------------ |
|           |                 | `FE / BE` |              |

The map must answer:

- WHAT needs to change;
- WHERE it changes;
- WHICH developer is responsible;
- WHAT dependencies affect the implementation.

The map must not prescribe:

- classes;
- functions;
- file structure;
- framework-specific implementation;
- detailed algorithms.

Those decisions belong to the relevant Developer unless explicitly defined by an approved requirement or decision.

If the affected component or responsible developer cannot be determined from available evidence, mark it as `OPEN`.

## Dependencies

Identify dependencies between affected components.

Consider:

- API contracts;
- data dependencies;
- service dependencies;
- frontend/backend dependencies;
- ordering constraints;
- shared components.

Only document dependencies supported by the analysis.

## API and Data Impact

Identify relevant impact on:

- API behavior;
- request/response data;
- validation;
- persistence;
- data relationships;
- state transitions.

Distinguish required changes from assumptions.

Do not invent API or data behavior that is not required.

## Architecture Impact

Determine whether the current architecture is sufficient.

Classify:

NO_CHANGE

CHANGE_REQUIRED

OPEN

When architectural change is required, describe:

- affected components;
- proposed direction;
- reasonable alternatives;
- risks;
- trade-offs.

The System Analyst may recommend an architectural solution.

The human makes the final architectural decision.

## Process Documentation

If the Story affects an existing process:

1. identify the affected process;
2. describe the relevant system flow;
3. identify affected components;
4. identify documentation impact.

Documentation must describe approved behavior.

Do not create or update process documentation to represent an unapproved decision.

## Risks and Trade-offs

Identify relevant system-level risks and constraints.

Consider:

- coupling;
- dependencies;
- data consistency;
- backward compatibility;
- scalability;
- maintainability;
- operational impact;
- impact on existing consumers.

Do not turn hypothetical concerns into requirements.

## Open Questions

Mark missing or ambiguous information as:

OPEN

For important decisions provide:

- question;
- why it matters;
- reasonable alternatives;
- recommendation.

Do not silently resolve the decision.

## Boundary

This skill defines:

WHAT changes

WHERE it changes

WHAT the system must do

WHAT is affected

WHAT dependencies matter

WHAT architectural impact exists

It does not define:

HOW the code is implemented

Implementation details belong to the relevant Developer.
