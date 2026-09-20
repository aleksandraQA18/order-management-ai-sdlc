# STORY-MS-001 — Course Product Catalog Entry

# Business Analysis

## Story Core

**As a** QA Academy platform administrator  
**I want** to store and manage course catalog entries with a name, description, category, and price  
**So that** learners can discover and purchase relevant QA education offerings

## Acceptance Criteria (max 3)

AC-01: A course/product record with name, description, category, and price can be created and retrieved by the system  
AC-02: Product price must be a positive decimal value in PLN currency with appropriate precision  
AC-03: Product records must not include inventory or stock-status fields; availability is managed through purchase and course access logic rather than quantity

### UI Design Artifact

Required: NO

### OPEN ISSUES

## Missing Information

- [OPEN] ---

## Ambiguity

- [OPEN] ---

---

# System Analysis

## Implementation Map

| Component           | Required change                                                                                        | Developer | Dependencies                        |
| ------------------- | ------------------------------------------------------------------------------------------------------ | --------- | ----------------------------------- |
| Product persistence | Add storage for product data: `id` (UUID), name, description, category, price (decimal)                | BE        | Existing database/persistence layer |
| Product API         | POST `/api/products` to create; GET `/api/products/{id}` to retrieve by UUID                           | BE        | Product persistence                 |
| Product validation  | Enforce: positive PLN price (2 decimal places); reject unexpected inventory fields                     | BE        | Product API, persistence            |
| Availability model  | No quantity or `stock_status` field in the product contract; course access is handled by purchase flow | BE        | Purchase/access logic               |

## Architecture Impact

**Status:** `CHANGE_REQUIRED`

This change removes stale inventory semantics and brings the backend in line with the QA Academy course marketplace concept. No new architectural pattern is required.

## Material Decisions

- **Product ID Strategy:** UUID (universally unique identifier)
- **Product Retrieval:** `GET /api/products/{id}` where `{id}` is a UUID
- **Price Precision:** 2 decimal places (standard for PLN currency, e.g., 9,99 PLN)
- **Product Contract:** course catalogue metadata only; no inventory quantity or stock-status field

## Risks

- None identified for the current approved scope, provided the stale inventory fields are not reintroduced.

---

## QA Analysis

### BDD Scenarios

Not required — regular verification scenarios are sufficient.

### Automation Tests

| Status | Scenario                                              | Level             |
| ------ | ----------------------------------------------------- | ----------------- |
| New    | Create product with valid course metadata             | API               |
| New    | Reject zero or negative price                         | API               |
| New    | Accept valid PLN price with required precision        | API / Integration |
| New    | Reject unexpected inventory fields such as `quantity` | API               |
| New    | Retrieve created product by UUID                      | API               |
| New    | Return not-found for unknown product                  | API               |
| New    | Validate required product data                        | API               |
| New    | Verify persisted product data                         | Integration       |

### Manual Tests

Not required.

Automated API and integration tests provide sufficient deterministic evidence for this Story.

### Test Strategy

API-first, automation-first.

- API tests verify product creation, retrieval, validation, and course metadata behavior.
- Integration tests verify persistence and data integrity.
- E2E is not required because no UI is in scope.
- Manual testing is not required unless exploratory testing reveals an issue that cannot be adequately verified through automation.

### Regression

Focused regression of existing backend/API tests affected by the Product functionality.

No broad E2E or full application regression is required for this Story.

### Quality Contract

The Story is verified when:

- all material behaviors from the Acceptance Criteria have automated evidence;
- relevant existing tests are reused, extended, or updated where necessary;
- API tests pass;
- required integration tests pass;
- relevant regression tests pass;
- no material QA gaps remain unresolved.
