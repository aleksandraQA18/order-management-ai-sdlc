# AI SDLC Experiment --- Architecture Baseline

## Target Stack

-   Frontend: React + TypeScript + Vite
-   Backend: Python + FastAPI + Pydantic
-   Database: PostgreSQL
-   Test automation: Playwright + TypeScript
-   CI/CD: GitHub Actions
-   Containers: Docker + Docker Compose

## Architecture

Modular monolith:

Browser → React → REST/JSON → FastAPI → domain/application logic →
persistence → PostgreSQL

## Principles

1.  Keep the architecture proportional to the MVP.
2.  No microservices, Kubernetes, Kafka or cloud infrastructure for MVP.
3.  Separate API, application/domain logic, persistence and
    schemas/models.
4.  Backend enforces business rules.
5.  Make tests deterministic and isolated.
6.  Support reproducible local and CI execution.
7.  Keep secrets out of source control.
8.  Do not expose database credentials to the frontend.
9.  Design for testability.

## Repository Baseline

``` text
order-management/
├── frontend/
├── backend/
├── tests/
│   ├── api/
│   ├── e2e/
│   └── fixtures/
├── qa/
├── docs/
├── .github/workflows/
├── docker-compose.yml
└── README.md
```

## Architecture Agent

Owns system boundaries, architectural decisions, constraints,
non-functional expectations, testability and architectural risks. It
should not micromanage implementation.
