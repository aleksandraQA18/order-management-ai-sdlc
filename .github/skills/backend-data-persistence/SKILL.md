---
name: backend-data-persistence
description: Implement approved database and persistence changes, including focused Alembic migrations and data-integrity validation.
argument-hint: "[Story]"
---

# Backend Data Persistence

Use only when the Story changes models, schema, migrations, repositories/data access, relationships, constraints, or persistence behavior.

## Flow

1. Read approved System Analysis and Implementation Map.
2. Inspect current SQLAlchemy models, migrations, and data-access patterns.
3. Identify required schema, relationship, constraint, and compatibility changes.
4. Make the smallest safe persistence change.
5. Create/update the established Alembic migration when required.
6. Run relevant migration/database validation.
7. Review migration and data-safety impact.

## Data Model

Change only requirements supported by the Story/SA analysis.

Consider relevant:
- types and nullability;
- defaults;
- keys and relationships;
- uniqueness/indexes;
- constraints.

Do not add constraints/defaults that change approved behavior without approval.

## Migrations

- Use the existing Alembic workflow.
- Keep migrations focused.
- Preserve migration history/order.
- Do not rewrite existing migrations.
- Avoid destructive operations unless explicitly approved.
- Consider compatibility with existing data.

Report `OPEN` if safe migration strategy is unclear or data loss may occur.

## Integrity

Protect approved invariants and relationships. Consider only relevant risks such as duplicates, invalid references, nulls, orphaned records, existing data, and transaction boundaries.

A successful migration does not prove application behavior is correct.

## Output

Report:
- model/persistence changes;
- migration changes;
- validation/results;
- compatibility concerns;
- `OPEN` issues or deviations.
