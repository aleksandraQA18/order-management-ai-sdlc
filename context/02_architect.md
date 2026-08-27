# Architecture Context

## Architecture Style

The application currently follows a modular monolith approach.

The backend is implemented as a single application. Business capabilities
are kept logically separated within the application rather than deployed
as independent microservices.

The architecture is intentionally kept proportional to the current MVP.

## Application Components

### Frontend

- React
- TypeScript
- Vite

The frontend communicates with the backend through REST/JSON.

### Backend

- Python
- FastAPI
- Pydantic

The backend contains the application and domain logic and is responsible
for enforcing business rules.

### Database

- PostgreSQL

PostgreSQL is used as the persistent data store for the application.

## Current Runtime Architecture

### Local Development

The local environment is containerized using Docker Compose.

```text
Docker Compose
├── order-api
│   └── FastAPI application
│
└── PostgreSQL
```

The API connects to PostgreSQL using environment-based configuration.

The PostgreSQL data is persisted using a Docker volume.

### CI

GitHub Actions currently executes the following flow:

```text
GitHub push / pull request
        ↓
lint + formatting
        ↓
database connection check
        ↓
database migrations
        ↓
automated tests
        ↓
container test
        ↓
readiness check
        ↓
API smoke test
        ↓
Docker image
        ↓
GHCR
```

The CI workflow uses PostgreSQL as a temporary service for application
tests. Container testing uses the Docker Compose configuration.

## Container Image

The `order-api` image is built as part of the CI pipeline and published
to GitHub Container Registry (GHCR).

Current image:

`ghcr.io/aleksandraqa18/order-management-ai-sdlc:latest`

## Staging

The application is deployed to a staging environment on Render.

The staging environment currently consists of:

```text
Render
├── order-api
└── PostgreSQL
```

The staging API exposes health and readiness endpoints used to verify
that the service is running and ready.

## Configuration and Secrets

Application configuration is provided through environment variables.

Secrets and environment-specific credentials are not stored in source
control.

The frontend does not receive database credentials.

## Testing

The project currently uses automated backend tests and container-level
smoke/readiness verification.

The architecture is designed to support deterministic and reproducible
test execution locally and in CI.

## Current Architectural Constraints

- Single backend application
- Single PostgreSQL database
- No independent microservice deployments
- No Kubernetes
- No message broker
- No real payment provider integration
- No real courier/shipping provider integration

These constraints describe the current MVP architecture and may change
as the product evolves.

## Architecture Evolution

This document describes the current architecture.

When implementation of a feature requires an architectural change, the
change must be reviewed before implementation and this document must be
updated after the decision is accepted.

Significant architectural decisions should also be recorded separately
as Architecture Decision Records (ADRs).

## Architecture Principles

1. Keep architecture proportional to the MVP.
2. Prefer simple boundaries before introducing distributed systems.
3. Keep business rules in the backend.
4. Design for testability.
5. Support reproducible local and CI execution.
6. Keep secrets out of source control.
7. Do not expose database credentials to the frontend.
