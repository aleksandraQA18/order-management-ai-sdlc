"""Service-level health endpoints for the products API.

These checks are intentionally kept separate from product-domain routes so the
same pattern can be reused by future API services without coupling health
status to a specific business resource.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.database import check_database_connection

router = APIRouter()


@router.get("/", tags=["Health"])
def read_root() -> dict[str, str]:
    """Return a simple service identity for deployment and smoke checks."""
    return {"message": "Products API is running"}


@router.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Confirm the app process is alive and responding."""
    return {"status": "OK"}


@router.get("/ready", tags=["Health"])
def readiness_check():
    """Check whether the service can connect to the configured database."""
    if check_database_connection():
        return {"status": "ready"}
    return JSONResponse(status_code=503, content={"status": "not ready"})
