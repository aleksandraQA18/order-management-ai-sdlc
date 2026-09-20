"""FastAPI application entry point for the QA Academy backend.

This file wires together the API routes and exposes simple readiness endpoints
that are useful for local development, health checks, and deployment probes.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.routes.products import router as products_router
from app.database import check_database_connection


def create_app() -> FastAPI:
    """Build the application and register the routes for each startup."""
    app = FastAPI(title="QA Academy API")
    app.include_router(products_router)
    return app


app = create_app()


@app.get("/")
def read_root():
    """Simple welcome endpoint for the API."""
    return {"message": "QA Academy API is running"}


@app.get("/health")
def health_check():
    """Basic health endpoint used to confirm the service is alive."""
    return {"status": "OK"}


@app.get("/ready")
def readiness_check():
    """Checks whether the API can talk to the configured database."""
    if check_database_connection():
        return {"status": "ready"}
    return JSONResponse(status_code=503, content={"status": "not ready"})
