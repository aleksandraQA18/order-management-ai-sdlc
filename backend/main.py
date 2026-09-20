"""FastAPI application entry point for the QA Academy backend.

This module composes the service-level routers and keeps app assembly separate
from domain-specific route code.
"""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router


def create_app() -> FastAPI:
    """Build the application and register the routes for each startup."""
    app = FastAPI(title="Products API")
    app.include_router(health_router)
    app.include_router(products_router)
    return app


app = create_app()
