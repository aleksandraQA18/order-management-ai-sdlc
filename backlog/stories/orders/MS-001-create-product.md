# STORY-MS-001 — Product Data Model and API

## Story

**As a** system/backend service

**I want** create and persist product data to the database

**So that** products can be discovered, purchased, and managed in the order management system

---

**CONTEXT:** This story defines the product data model and persistence layer for the MVP. Products are created via backend API (no management UI required). This enables the product catalog to be populated for customer browsing and purchasing.

## Story Status

**BA Status:** `APPROVED - Ready for System Analysis`

**System Analysis Status:** `COMPLETE - Ready for QA Analysis`

**QA Status:** `COMPLETE - Ready for Implementation`

**Human Decision:** Product creation is in MVP scope via API. No UI management system required for MVP. Products are created programmatically via backend API. Categories: pre-defined enum (string_instruments, keyboard_instruments, wind_instruments).

## Human Input

### Business Request

Create product model and save it to data base.

### Constraints

- product name: 250 characters, not null
- description: 500 characters
- in stock: true or false
- quantity: int, not null
- price: float, not null

### UI Design Artifact

Required: NO

Artifact:
`path/to/design.html`

### Initial Acceptance Criteria

| ID    | Initial Acceptance Criteria                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | A product with name, description, quantity, and price can be created via API and retrieved from database                      |
| AC-02 | Product name is required and must not exceed 250 characters                                                                   |
| AC-03 | Product description is optional and must not exceed 500 characters                                                            |
| AC-04 | Product quantity must be a non-negative integer                                                                               |
| AC-05 | Product price must be a positive decimal value in PLN currency                                                                |
| AC-06 | Product creation fails with validation error when required fields are missing                                                 |
| AC-07 | Product availability is derived from quantity: if quantity > 0, product is in stock; if quantity = 0, product is out of stock |
| AC-08 | Product must have a category assigned (required field, must be valid category name)                                           |

---

## BA Analysis

| Area                  | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Business rules        | **Product attributes:** Name (required, ≤250 chars), Description (optional, ≤500 chars), Category (required), Quantity in stock (required, non-negative integer), Price (required, positive decimal in PLN). Stock status is derived: if quantity > 0, product is in stock; if quantity = 0, out of stock. **Validation:** All required fields must be validated and provided before persistence. Field length constraints are business decisions (sufficient for musical instrument product information). Category enables filtering and organization of products in catalog. |
| Scope / Out of scope  | **IN SCOPE:** Product data model and persistence. Field validation and storage rules. Product creation via backend API. Product categorization (required field for filtering). **OUT OF SCOPE:** User interface for product creation/management. Product listing/discovery (separate feature). Admin authentication/authorization. Inventory management beyond initial stock quantity. Multi-currency support. Product approval/visibility workflow. Category management UI.                                                                                                   |
| Business dependencies | **Upstream:** None blocking. Product creation is independent. **Downstream:** Product listing and product details features depend on this data model. Product category enables filtering/navigation in future product listing feature. Checkout/cart features depend on product availability (stock quantity).                                                                                                                                                                                                                                                                 |
| Open questions        | **Q1:** What valid categories exist and how should they be defined? Answer: APPROVED—pre-defined enum: `string_instruments`, `keyboard_instruments`, `wind_instruments` (matching MVP product categories per product context).                                                                                                                                                                                                                                                                                                                                                 |
| Recommendation        | **READY FOR SYSTEM ANALYSIS.** Story is now bounded and clear. Proceed to System Analyst to define technical architecture, API contract, database schema, and implementation boundaries.                                                                                                                                                                                                                                                                                                                                                                                       |

---

## System Analyst Analysis

**Status:** `COMPLETE - Ready for QA Analysis and Implementation`

| Area                      | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System behavior / process | **Product Creation Flow:** Backend API receives product data (name, description, category, quantity, price) via HTTP POST request → validates all fields per business rules → persists to database → returns created product with ID. **Product Retrieval:** Product can be retrieved from database by ID or listed (separate feature). **Validation:** Required fields (name, category, quantity, price) are validated before persistence. Price must be positive decimal (PLN). Quantity must be non-negative integer. Name must not exceed 250 chars. Description (optional) must not exceed 500 chars if provided. Category must be provided and must be a valid category name.                                                                                                                  |
| Components affected       | **Backend API:** Add POST `/products` endpoint to accept product creation requests. Existing GET `/health` and `/ready` endpoints unaffected. **Database Models:** Add new `Product` SQLAlchemy model with fields: id (UUID, PK), name (String, required, ≤250), description (String, optional, ≤500), category (String, required), quantity (Integer, required, ≥0), price (Decimal/Float, required, >0), created_at (Timestamp), updated_at (Timestamp). **Database:** Add new `products` table via Alembic migration. **Validation:** Use Pydantic models for request validation and FastAPI/Pydantic built-in validators.                                                                                                                                                                        |
| Architecture impact       | `NO_CHANGE` — Product model added to existing monolith backend following current architecture patterns (SQLAlchemy ORM, FastAPI, Alembic migrations). No new services, no architectural boundary changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Data / API impact         | **New API Endpoint:** `POST /products` — accepts product data (name, description, category, quantity, price) and returns created product with id, timestamps. Request validation: required fields enforced, field lengths validated, price > 0, quantity ≥ 0, category must be valid. Error responses: 400 Bad Request with validation details if constraints violated. **Database Schema:** New `products` table with: id (UUID), name (VARCHAR 250), description (VARCHAR 500), category (VARCHAR), quantity (INTEGER), price (DECIMAL/NUMERIC), created_at (TIMESTAMP), updated_at (TIMESTAMP). **No breaking changes** to existing Order model or APIs.                                                                                                                                          |
| Risks / trade-offs        | **Risk 1 - Data Type for Price:** Float vs Decimal. **Recommendation:** Use Decimal/NUMERIC in PostgreSQL to avoid floating-point precision issues with currency. **Risk 2 - Stock Status Derivation:** Current design derives stock status from quantity only. No separate visibility/approval mechanism. **Mitigation:** Approved in BA—sufficient for MVP. **Risk 3 - Concurrent Stock Updates:** Multiple requests creating orders could race condition on quantity. **Mitigation:** Not in scope for MS-001 (inventory management is downstream feature). Use application-level or database-level locking if needed in future. **Risk 4 - Missing Timestamps:** No audit trail of product creation/updates. **Recommendation:** Add created_at/updated_at fields for operational observability. |
| Documentation impact      | `UPDATE_EXISTING` — Update backend API documentation (if separate from code) to include POST /products endpoint, request/response schema, validation rules, error codes. Consider adding API examples. Alembic migration file should include comments explaining schema rationale.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Open questions            | **Q1:** Should product have a category/type field for filtering (e.g., string instruments, keyboard)? Answer: IN_SCOPE for MS-001—required field to support future product listing filtering. **Q2:** Should product have stock_status boolean or derive from quantity? Answer: DECIDED—derive from quantity per BA Analysis. **Q3:** Who calls the POST /products endpoint in MVP? Answer: OPEN—backend service/system integration (no UI). Seed data loading or API integration to be defined separately. **Q4:** What valid categories exist and how are they defined/validated? Answer: APPROVED—predefined enum per D-07: `string_instruments`, `keyboard_instruments`, `wind_instruments`.                                                                                                     |
| Recommendation            | **READY FOR QA ANALYSIS.** Story is now fully specified with clear API contract, database schema, validation rules, and implementation boundaries. No architectural impact. BE Developer has sufficient context to implement. No blocking decisions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Implementation Map

| Component                 | Required change                                                                                                                                                                                                                                              | Developer | Dependencies                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | --------------------------------------------------------------------------------------- |
| Backend API (FastAPI)     | Add POST `/products` endpoint that accepts and validates product data (including category), returns created product with id and timestamps                                                                                                                   | `BE`      | SQLAlchemy Product model, Database connection, Pydantic validators, Category validation |
| SQLAlchemy Models         | Add Product model class with fields: id, name, description, category, quantity, price, created_at, updated_at. Include field validation constraints (length, positive values, category required).                                                            | `BE`      | Database schema via Alembic migration                                                   |
| Database Schema (Alembic) | Create new `products` table with schema matching Product model. Field constraints: name VARCHAR(250) NOT NULL, description VARCHAR(500), category VARCHAR NOT NULL, quantity INTEGER NOT NULL ≥ 0, price DECIMAL NOT NULL > 0, timestamps.                   | `BE`      | None (database migrations run as part of deployment)                                    |
| Pydantic Request Model    | Define request/response schemas for product creation (e.g., ProductCreate, ProductResponse). Include validation: name required/length, description optional/length, category required, quantity ≥ 0, price > 0.                                              | `BE`      | FastAPI/Pydantic (existing), Category validation logic                                  |
| Category Validation       | Define valid categories list or enum for product categorization. Implement validation logic to ensure only valid categories are accepted.                                                                                                                    | `BE`      | Product model validation, Pydantic validators                                           |
| Unit Tests                | Backend unit tests for: product model validation including category, API endpoint, error cases (missing fields, invalid values, length violations, invalid category). Database integration tests for: create/read product, persistence, category validation. | `BE`      | Existing test infrastructure (pytest)                                                   |

### Architecture Decision

| Topic                   | Recommendation                                                                                                                                                          | Human Decision      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Product Price Data Type | Use DECIMAL/NUMERIC in PostgreSQL instead of Float to avoid precision issues with currency values                                                                       | `APPROVED`          |
| Product Visibility      | Derive from quantity only (no separate visibility/approval workflow for MVP)                                                                                            | `APPROVED` (per BA) |
| Stock Concurrency       | Out of scope for MS-001. Inventory management and concurrency control are downstream concerns                                                                           | `APPROVED`          |
| Product Categories      | Use predefined enum for product categorization: `string_instruments`, `keyboard_instruments`, `wind_instruments` (matching MVP product categories from product context) | `APPROVED`          |

---

## QA Analysis

| Area                 | Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical behavior    | **Product Creation:** POST `/products` API must accept valid product data, validate all fields per business rules, persist to database, return created product with ID. **Field Validation:** Name (required, ≤250 chars), Description (optional, ≤500 chars), Category (required, must be valid enum), Quantity (required, ≥0), Price (required, >0). **Error Handling:** Invalid/missing required fields must return 400 Bad Request with validation error details. **Stock Derivation:** Product availability must be derived from quantity (quantity > 0 = in stock; quantity = 0 = out of stock). |
| Risks                | **Risk 1 - Category Enum Validation:** Invalid category values must be rejected. Likelihood: Medium (common validation bug). Impact: High (inconsistent data). Verification: Unit + API tests for valid/invalid enum values. **Risk 2 - Price Precision:** Floating-point precision errors with currency. Likelihood: Medium. Impact: High (financial data). Mitigation: Use DECIMAL type (architecture decision D-01). Verification: API/database integration tests with edge cases (0.01, 99.99, etc.). **Risk 3 - Boundary Values:** Name/description exactly at length limits (250, 500 chars). Likelihood: Low. Impact: Medium (edge case failures). Verification: Unit tests with boundary values (249, 250, 251 chars). **Risk 4 - Quantity Validation:** Quantity = 0 should be valid (out of stock), but quantity = -1 should fail. Likelihood: Low. Impact: Medium. Verification: Unit tests for boundary (0, 1, -1). |
| Existing coverage    | **FACT:** No existing tests for: Product model, POST /products endpoint, product validation, database schema, Pydantic schemas. Story defines new backend component with zero existing coverage. No regression to existing Order tests expected.                                                                                                                                                                                                                                                                                                                                                           |
| Coverage gaps        | **Gap 1 - API Contract:** No existing test validates POST /products request/response schema. **Gap 2 - Category Validation:** No tests for valid/invalid category enum values. **Gap 3 - Boundary Values:** No tests for field length boundaries (name: 249/250/251 chars). **Gap 4 - Price Edge Cases:** No tests for price precision (0.01, 999.99, etc.) or negative values. **Gap 5 - Error Responses:** No tests for error handling (missing fields, invalid types, invalid category). **Gap 6 - Database Constraints:** No tests for database-level constraint enforcement (NOT NULL, VARCHAR length, DECIMAL precision, etc.).                                             |
| Verification targets | **VT-01 (AC-01):** Product creation via API with all required fields succeeds and returns product with ID + timestamps. **VT-02 (AC-02):** Product name validation: required, max 250 chars, longer names rejected with error. **VT-03 (AC-03):** Product description validation: optional, max 500 chars, longer descriptions rejected. **VT-04 (AC-04):** Quantity validation: non-negative integer, rejects negative values with error. **VT-05 (AC-05):** Price validation: positive decimal in PLN, rejects non-positive/non-decimal values. **VT-06 (AC-06):** Error handling: missing required fields (name, category, quantity, price) each return 400 Bad Request with field-specific error. **VT-07 (AC-07):** Stock status derived correctly (quantity > 0 = true, quantity = 0 = false). **VT-08 (AC-08):** Category validation: required, must match enum, invalid categories rejected. **VT-09 (Regression):** Existing Order API tests still pass. |
| BDD scenarios        | **Scenario 1 - Create product successfully:** GIVEN valid product data (name, category, quantity, price) WHEN POST /products THEN product created with ID and timestamps returned. **Scenario 2 - Reject missing name:** GIVEN product data without name WHEN POST /products THEN 400 error returned. **Scenario 3 - Reject invalid category:** GIVEN product with category not in enum WHEN POST /products THEN 400 error returned. **Scenario 4 - Name length boundary:** GIVEN name with exactly 250 chars WHEN POST /products THEN product created; given 251 chars THEN 400 error. **Scenario 5 - Stock status:** GIVEN product with quantity=0 WHEN product retrieved THEN stock status = false; GIVEN quantity=5 THEN stock status = true. |
| Test level           | **Unit Tests (Pydantic models, validators):** Fast, reliable, isolated. Test name/description length validation, category enum, price/quantity constraints at Pydantic level. **API Integration Tests (FastAPI endpoint):** Test POST /products endpoint with valid/invalid data, error handling, response schema. **Database Integration Tests:** Verify schema constraints (NOT NULL, VARCHAR length, DECIMAL precision), data persistence, timestamp generation. **Rationale:** Unit tests provide fast feedback on validation logic. API tests verify endpoint contract. Database tests verify schema enforcement. E2E testing not needed for this feature (no UI, no cross-component flow). |
| Automation           | **Unit Tests:** Automate all Pydantic validation tests. Test category enum strictly. **API Tests:** Automate POST /products endpoint with fixtures for valid/invalid test data (boundary values, edge cases). Automate error response validation. **Database Tests:** Automate schema verification (constraint enforcement). **Regression:** Ensure existing Order API tests continue to pass. **CI Integration:** All tests run in CI pipeline (part of existing pytest infrastructure). **No manual testing required for this feature (automated validation sufficient).** |
| Regression impact    | **LOW:** New endpoint/model, no changes to existing Order API or models. Order tests should not be affected. Architecture: monolith, no service boundary changes. **Scope:** Regression testing should verify: Order API still works (smoke test GET /health, GET /ready). Order model tests still pass. No database migration breaks existing Order data. |
| Quality gate         | **REQUIRED:** All 8 ACs verified (unit + integration tests). Unit tests: category validation, field constraints, error handling. API tests: POST /products endpoint, valid/invalid scenarios, error responses. Database tests: schema constraints, data persistence. Coverage: ≥90% of new Product model code. **CI Passes:** Build, linting, database migrations, all tests. No blocking defects. **Gate recommendation:** READY for merge when all tests pass and coverage ≥90%. |

### QA Quality Contract

| Area                         | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Required verification        | ✅ All 8 Acceptance Criteria verified via automated tests. **VT-01:** Product creation (API integration test). **VT-02-05:** Field validation (unit + API tests). **VT-06:** Error handling (API tests). **VT-07:** Stock derivation (unit + API tests). **VT-08:** Category validation (unit + API tests). **VT-09:** Order regression (smoke test). |
| Required automation          | ✅ **Unit tests:** Pydantic ProductCreate/ProductResponse models, category enum validation, field constraints (min/max). ✅ **API Integration tests:** POST /products with valid product data, invalid categories, missing fields, boundary values. ✅ **Database Integration tests:** Schema constraints, data persistence, timestamps. ✅ **Regression tests:** Order API smoke test (GET /health, existing Order tests). ✅ **CI:** All tests automated in pytest, run on every commit. |
| Required manual verification | ❌ **None required.** Feature is backend-only (API), no UI. Validation logic is testable at unit/API level. Database constraints are enforceable. Error handling is testable programmatically. |
| Quality gate                 | ✅ **MERGE GATE:** (1) All pytest tests PASS. (2) Code coverage ≥90% for new Product model. (3) No failing linter (ruff check). (4) CI pipeline completes. (5) No known defects or BLOCKED risks. **Recommendation: READY for merge when gate criteria met.** |

---

## Human Decisions

| ID   | Topic                         | Recommendation                    | Decision                       | Reason                                                                                                                                                                                                                                                   |
| ---- | ----------------------------- | --------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D-01 | MVP Scope: Product Management | Clarify product creation approach | **APPROVED: YES, via API**     | Product creation is in MVP scope. No UI management system yet. Products added programmatically via backend API. Resolves conflict with "Admin functionality out of scope"—this is system/backend integration, not admin UI.                              |
| D-02 | Product Creation Method       | Define how products enter system  | **APPROVED: Backend API only** | No management UI required for MVP. Products loaded via API integration or automated processes. Enables product listing/discovery features to work in MVP.                                                                                                |
| D-03 | Product Visibility Control    | Separate from stock quantity?     | **APPROVED: NO for MVP**       | Product visibility controlled via stock quantity only. If quantity > 0, product is available. No separate approval/visibility workflow for MVP.                                                                                                          |
| D-04 | Field Constraints             | Validate business rationale       | **APPROVED: 250/500 chars**    | Product name: 250 characters sufficient for musical instrument names. Description: 500 characters sufficient for product description. Constraints are business decisions, not technical only.                                                            |
| D-05 | Currency Support              | Multi-currency or single?         | **APPROVED: PLN only**         | MVP supports Polish Zloty (PLN) only. Price stored as decimal. No multi-currency support or conversion.                                                                                                                                                  |
| D-06 | Product Category              | Should category be in MS-001?     | **APPROVED: YES, required**    | Category is required field added to MS-001 to support future product listing/filtering features. Enables product organization in catalog. Predefined categories: `string_instruments`, `keyboard_instruments`, `wind_instruments` (per product context). |
| D-07 | Product Category Values       | Define valid categories           | **APPROVED: Predefined enum**  | Valid categories are: `string_instruments` (instrumenty strunowe), `keyboard_instruments` (instrumenty klawiszowe), `wind_instruments` (instrumenty dęte). Matches MVP product categories from product context. Validated via Pydantic enum.             |

---

## Implementation

### FE

| Area                   | Output |
| ---------------------- | ------ |
| Changes                |        |
| Unit / component tests |        |
| Documentation          |        |
| Notes / deviations     |        |

### BE

| Area               | Output |
| ------------------ | ------ |
| Changes            |        |
| Unit tests         |        |
| Documentation      |        |
| Notes / deviations |        |

---

## Implementation Evidence

| Check                     | Result | Evidence |
| ------------------------- | ------ | -------- |
| FE unit / component tests |        |          |
| BE unit tests             |        |          |
| Build / static checks     |        |          |
| Other checks              |        |          |

---

## Verification

| Verification      | Result | Evidence |
| ----------------- | ------ | -------- |
| API / integration |        |          |
| E2E               |        |          |
| Manual            |        |          |
| CI                |        |          |

---

## Final Review

| Area                | Result | Notes |
| ------------------- | ------ | ----- |
| Acceptance Criteria |        |       |
| QA Quality Contract |        |       |
| Implementation      |        |       |
| Verification        |        |       |
| Documentation       |        |       |

**Final status:** `OPEN`
