"""API routes for product management.

These endpoints form the main public interface of the backend: creating new
products and fetching product records from the database.
"""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product
from app.schemas.products import ProductCreate, ProductResponse
from app.services.products import create_product, get_product_by_id, list_products

router = APIRouter()


@router.post(
    "/api/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Products"],
)
def create_product_route(
    product: ProductCreate,
    db: Annotated[Session, Depends(get_db)],
) -> Product:
    """Create a new product record and persist it to the database."""
    return create_product(db, product)


@router.get("/api/products", response_model=list[ProductResponse])
def get_products_route(
    db: Annotated[Session, Depends(get_db)],
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    tags=["Products"],
) -> list[Product]:
    """Return a paginated list of products in a stable order."""
    return list_products(db, page=page, page_size=page_size)


@router.get("/api/products/{product_id}", response_model=ProductResponse)
def get_product_route(
    product_id: UUID,
    db: Annotated[Session, Depends(get_db)],
    tags=["Products"],
) -> Product:
    """Fetch a single product by ID or return a 404 response when missing."""
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
