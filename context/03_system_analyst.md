# AI SDLC Experiment --- System Analysis Baseline

## Domain

Customer: - id - name - email

Product: - id - name - price - active

Order: - id - customer_id - status - total - created_at - updated_at

OrderItem: - id - order_id - product_id - quantity - unit_price -
line_total

## State Machine

``` text
CREATED
 ├──> CONFIRMED ──> SHIPPED ──> COMPLETED
 └──> CANCELLED

CONFIRMED ──> CANCELLED
```

## API Capabilities

-   POST `/orders`
-   GET `/orders/{id}`
-   GET `/orders`
-   PATCH `/orders/{id}/status`
-   one explicit cancellation mechanism, selected during design

## System Rules

-   customer must exist
-   at least one item
-   product must exist
-   quantity \> 0
-   total calculated by server
-   order creation is atomic
-   invalid transitions rejected
-   consistent error response

## Example Error

``` json
{
  "code": "PRODUCT_NOT_FOUND",
  "message": "Product does not exist"
}
```

## Open Questions

Do not silently invent: - idempotency behavior - authentication
requirement - pagination requirement - money rounding rule -
inactive-product behavior - cancellation endpoint semantics

Mark unresolved items as `OPEN`.

## SA Agent

Owns system behavior, domain model, API contract, validation,
persistence rules, state transitions, technical edge cases and open
questions.
