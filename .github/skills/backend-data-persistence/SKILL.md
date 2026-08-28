---
name: backend-data-persistence
description: Implement approved backend data-model and persistence changes while preserving data integrity, migration safety and existing persistence conventions.
argument-hint: "[Story]"
---

# Backend Data Persistence

Use this skill when a Story requires backend data-model, schema or persistence changes.

Implement data and persistence changes defined by the approved System Analyst
analysis.

Do not introduce unrelated schema changes or data-model redesign.

If implementation requires an unexpected database or persistence change,
stop and request human review.

## Inputs

Use:

- approved Story;
- approved Acceptance Criteria;
- approved System Analyst analysis;
- approved Implementation Map;
- existing data model;
- existing migrations;
- persistence/repository code;
- database configuration;
- repository conventions.

The approved System Analyst analysis is the source of intended data behavior.

## Scope

Implement only persistence changes assigned to `BE`.

Do not introduce unrelated schema redesign, cleanup or optimization.

If the required data change is not represented in the Implementation Map:

- stop;
- record the issue as `OPEN`;
- request human review.

## Existing Persistence

Before changing persistence:

1. inspect the current model/schema;
2. inspect related migrations;
3. inspect repository/data-access patterns;
4. identify existing constraints and relationships;
5. identify compatibility implications.

Prefer established repository patterns over introducing a new persistence approach.

## Data Model

When changing the data model, verify relevant:

- fields;
- types;
- nullability;
- defaults;
- primary keys;
- foreign keys;
- uniqueness;
- indexes;
- relationships;
- constraints.

Do not add constraints or defaults solely for convenience if they change approved behavior.

## Migrations

When migrations are part of the repository workflow:

- use the established migration mechanism;
- keep migrations focused;
- preserve migration ordering;
- avoid destructive operations unless explicitly approved;
- consider existing data compatibility;
- do not silently rewrite existing migration history.

If a migration could cause data loss or materially affect existing data and this was not explicitly approved, stop and request human review.

## Data Integrity

Preserve approved invariants and relationships.

Consider:

- invalid references;
- duplicate records;
- null values;
- orphaned data;
- existing records;
- transaction boundaries where relevant.

Do not introduce behavior that can silently corrupt or discard data.

## Backward Compatibility

Consider whether existing application behavior and existing data remain compatible after the change.

If compatibility requires an unapproved architectural or migration strategy, record the issue as `OPEN`.

## Testing Boundary

The BE Developer may add unit tests for persistence-related logic when appropriate.

This does not replace:

- database integration tests;
- API tests;
- end-to-end tests;
- manual data verification;

when required by the QA Quality Contract.

Those tests remain outside this skill.

## Evidence

Record:

- persistence changes;
- migration changes;
- relevant checks;
- unit tests;
- compatibility considerations;
- limitations or deviations.

Never claim a migration or database check succeeded unless it actually ran.

## Boundary

This skill defines implementation of approved backend data/persistence changes.

It does not define:

- business requirements;
- system architecture;
- database platform selection;
- API test implementation;
- integration/E2E test implementation;
- deployment strategy.
