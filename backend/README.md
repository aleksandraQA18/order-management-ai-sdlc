# Backend overview

This backend exposes the API for the QA Academy product catalogue and purchase flows.

## Structure

- `main.py` – application entry point and health/readiness routes.
- `app/database.py` – database connection configuration and SQLAlchemy session creation.
- `app/api/routes/` – HTTP route definitions for the public API.
- `app/services/` – business logic and persistence operations for each domain area.
- `app/models/` – SQLAlchemy models mapped to database tables.
- `app/schemas/` – request and response validation models used by FastAPI.
- `tests/unit/` – validation and service-level unit tests.
- `migrations/` – Alembic migration files.

## Core responsibilities

### API layer

The route modules focus on HTTP concerns only:

- parsing request data
- validating inputs through Pydantic models
- calling service functions
- returning structured responses
- translating missing records into HTTP 404 errors

### Service layer

The services package contains the main application logic for each domain area.
This keeps database operations and business rules separate from the route code,
which makes the backend easier to read and extend.

### Model layer

The model classes define table mapping and the database invariants.
For the current product concept, the relevant constraints are:

- price must be positive
- catalog entries store course metadata and pricing information
- inventory-level fields are not part of the approved product contract

### Schema layer

Schemas define the external API contract. They are used for:

- request validation
- response serialization
- Swagger/OpenAPI examples
- consistent payload structure across the API

## Local workflow

From the backend folder:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest tests/unit
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Health checks

- `GET /` – welcome message
- `GET /health` – application is alive
- `GET /ready` – database connection is healthy

## Product API

- `POST /api/products` – create a product
- `GET /api/products` – list products with pagination
- `GET /api/products/{product_id}` – fetch one product

## Notes

The project keeps a clear separation between public API routes, business logic,
ORM models, and validation. That makes it easier to add new features and keep
behavior understandable as the application grows.
