# AI SDLC Experiment --- Business Context / BA

## Product

Order Management MVP.

## Business Goal

Provide a reliable workflow to create, retrieve, transition and cancel
customer orders.

## MVP Scope

-   Customers
-   Products
-   Orders
-   Order items
-   Order totals
-   Order lifecycle
-   REST API
-   Simple web UI for core flows
-   PostgreSQL persistence
-   Automated verification
-   CI execution

## Out of Scope

Payments, shipping integration, discounts, notifications, real payment
providers, advanced reporting, multi-tenancy, production cloud
infrastructure.

## Business Rules

-   BR-01: An order must contain at least one item.
-   BR-02: Quantity must be greater than zero.
-   BR-03: Product must exist.
-   BR-04: Customer must exist.
-   BR-05: Total is calculated server-side.
-   BR-06: New order starts in `CREATED`.
-   BR-07: Lifecycle: `CREATED → CONFIRMED → SHIPPED → COMPLETED`;
    cancellation is allowed from `CREATED` and `CONFIRMED`; `SHIPPED`,
    `COMPLETED`, `CANCELLED` are not cancellable.
-   BR-08: Order ID is unique.
-   BR-09: Failed creation must not leave partial data.

## Acceptance Criteria

-   AC-01: Valid order is created with `CREATED` status and returned ID.
-   AC-02: Unknown customer is rejected.
-   AC-03: Unknown product is rejected.
-   AC-04: Zero/negative quantity is rejected.
-   AC-05: Empty order is rejected.
-   AC-06: Total is calculated from product prices and quantities.
-   AC-07: Invalid status transitions are rejected.
-   AC-08: Cancellation is allowed only from eligible states.
-   AC-09: Rejected operations do not leave inconsistent data.

## BA Rules

The BA agent owns business intent, business rules, scope, acceptance
criteria, assumptions and open questions. It must not silently invent
technical implementation.
