---
name: system-analysis
description: Analyze the current system, define affected components and system behavior, assess architecture, and create an implementation boundary without prescribing code-level implementation.
argument-hint: "[Story]"
---

# System Analysis

Use this skill when analyzing system behavior, processes, architecture impact
and implementation boundaries for the current Story.

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

Clearly distinguish the current implementation from intended future behavior.

Use the following classification:

FACT:
...

INFERENCE:
...

PROPOSAL:
...

DECISION:
OPEN

Do not assume that existing implementation is automatically the desired
behavior.

## System Behavior

Describe:

- relevant system flow;
- affected behavior;
- inputs and outputs;
- state changes;
- validation;
- error behavior;
- relevant dependencies.

Focus on system behavior rather than implementation details.

## Components

Identify all application components affected by the Story.

For each component determine:

- why it is affected;
- what behavior must change;
- whether the change is required or optional.

Do not include components based only on speculation.

## Implementation Map

Create an Implementation Map for the affected components.

Use the following structure:

| Component | Required change | Developer | Dependencies |
|---|---|---|---|
| | | `FE / BE` | |

The map defines what needs to change and where.

It must not prescribe:

- classes;
- functions;
- file structure;
- framework-specific implementation;
- detailed algorithms.

Those decisions belong to the relevant Developer unless explicitly defined
by an approved requirement or decision.

## Dependencies

Identify dependencies between affected components.

Examples include:

- API contracts;
- data dependencies;
- service dependencies;
- frontend/backend dependencies;
- ordering constraints.

Only document dependencies supported by the analysis.

## API and Data Impact

Identify relevant changes to:

- API behavior;
- request/response data;
- validation;
- persistence;
- data relationships;
- state transitions.

Do not invent API or data behavior that is not required.

## Architecture Impact

Determine whether the current architecture is sufficient.

Classify:

NO_CHANGE

CHANGE_REQUIRED

OPEN

When a change is required, describe:

- affected components;
- proposed direction;
- alternatives;
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

Do not create or update process documentation to represent an unapproved
decision.

## Risks and Trade-offs

Identify relevant technical and system-level risks.

Consider:

- coupling;
- dependencies;
- data consistency;
- backward compatibility;
- scalability;
- maintainability;
- operational impact.

Do not turn hypothetical concerns into requirements.

## Open Questions

Mark missing information as:

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

It does not define:

HOW the code is implemented

Implementation details belong to the relevant Developer.