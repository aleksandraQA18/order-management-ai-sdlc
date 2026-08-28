# Architecture Context

## Purpose

This document describes the current architectural state of the application
and provides the architectural context required by agents working on the
system.

The document must reflect the architecture that actually exists at the
current point in time.

Detailed architectural documentation and significant architectural decisions
are maintained separately under `docs/architecture/`.

## Architecture Style

The application currently follows a modular monolith approach.

The backend is currently implemented as a single application. Business
capabilities are logically separated within the application and may evolve
into independently deployed services when justified by product or
architectural requirements.

The current architecture is intentionally kept proportional to the MVP,
while allowing gradual evolution toward a service-oriented architecture.

## Application Components

### Frontend

The application will provide a web-based user interface.

The frontend is planned as a React application using TypeScript and Vite.

It will communicate with the backend through HTTP APIs.

The frontend is part of the planned application architecture but is not yet
part of the current backend implementation baseline.

### Backend

The backend is currently implemented as a single application.

Current technologies include:

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic / FastAPI validation
- SQLAlchemy
- Alembic
- psycopg

The backend exposes the HTTP API and contains the application logic.

### Database

PostgreSQL is used as the persistent data store.

Database schema changes are managed using Alembic migrations.

## Current Runtime Architecture

### Local Development

The application is containerized using Docker Compose.

```text
Docker Compose
├── order-api
│   └── FastAPI application
│
└── PostgreSQL
```

The API connects to PostgreSQL using environment-based configuration.

PostgreSQL data is persisted using a Docker volume.

The API currently exposes:

- `/health` — service health check
- `/ready` — readiness check including database connectivity

## Containerization

The backend is packaged as a Docker image.

The image is built from:

```text
backend/Dockerfile
```

The container runs Uvicorn on port `8000`.

The Docker image is used as part of the CI/CD flow and is published to
GitHub Container Registry (GHCR).

## CI/CD

GitHub Actions is currently used for CI/CD.

The current pipeline includes:

- linting
- formatting validation
- database connectivity verification
- database migrations
- automated tests
- container testing
- readiness verification
- API smoke testing
- Docker image publication to GHCR

The CI workflow uses PostgreSQL as a service for application tests.

Detailed CI/CD configuration is maintained separately from this context.

## Staging

The application currently has a staging deployment on Render.

The staging environment contains:

```text
Render
├── order-api
└── PostgreSQL
```

The staging API exposes the health and readiness endpoints used to verify
service availability and database connectivity.

## Configuration and Secrets

Application configuration is provided through environment variables.

Database connection parameters are supplied through environment variables.

Secrets and environment-specific credentials must not be stored in source
control.

Database credentials must not be exposed to the frontend.

## Current Architectural Constraints

The current MVP architecture has the following constraints:

- the backend is currently deployed as a single application;
- a single PostgreSQL database is currently used;
- no independently deployed domain services currently exist;
- no Kubernetes is currently used;
- no message broker is currently used;
- no real payment provider integration is currently used;
- no real courier/shipping provider integration is currently used.

These constraints describe the current MVP architecture and may change as
product requirements evolve.

## Architectural Direction

The architecture is expected to evolve incrementally as the product grows.

Potential future service boundaries may include:

- Customers
- Orders
- Notifications
- Payments

These are architectural candidates, not current system components.

A business capability should be extracted into an independently deployed
service only when there is a justified business or architectural reason.

Service extraction must not be treated as an architectural goal by itself.

Potential reasons for introducing an independent service may include:

- clear domain boundaries;
- independent deployment requirements;
- significantly different scaling characteristics;
- isolation of external integrations;
- security or reliability requirements;
- organizational or operational requirements.

The decision to introduce a new service must be evaluated against the
complexity and operational cost it introduces.

## Architecture Evolution

This document represents the current accepted architectural state.

A Story may identify an architectural impact.

When an architectural change is identified, the responsible agent must:

1. describe the current architectural constraint;
2. describe the proposed change;
3. identify affected components;
4. identify risks and trade-offs;
5. identify alternatives when relevant;
6. identify open questions;
7. request human approval before the change is accepted.

An agent must not independently approve an architectural change.

After an architectural change is accepted and implemented:

- this document must be updated if the current architecture has changed;
- detailed architecture documentation must be updated when applicable;
- an Architecture Decision Record (ADR) should be created for significant
  architectural decisions.

## Architecture Principles

1. Keep architecture proportional to current product needs.
2. Prefer simple architectural boundaries before introducing distributed
   systems.
3. Keep business rules in the backend.
4. Design the system for testability.
5. Keep local and CI execution reproducible.
6. Keep secrets out of source control.
7. Do not expose database credentials to the frontend.
8. Do not introduce architectural complexity without a demonstrated
   requirement.
9. Prefer incremental architectural evolution over premature decomposition.
10. Treat microservices as an architectural option, not a default.
