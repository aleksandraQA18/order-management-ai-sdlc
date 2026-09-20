"""Service functions for product persistence and retrieval.

This layer keeps the database and business logic separate from the HTTP
handlers, making the routes easier to read and the logic easier to reuse.
"""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Product
from app.schemas.products import ProductCreate


def create_product(db: Session, product_data: ProductCreate) -> Product:
    """Persist a new product record and return the stored row."""
    db_product = Product(**product_data.model_dump())
    try:
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except Exception:
        db.rollback()
        raise
    return db_product


def list_products(db: Session, page: int, page_size: int) -> list[Product]:
    """Return a paginated list of products ordered by ID."""
    statement = (
        select(Product)
        .order_by(Product.id)
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    return list(db.scalars(statement).all())


def get_product_by_id(db: Session, product_id: UUID) -> Product | None:
    """Fetch one product by ID or return None when the record does not exist."""
    return db.get(Product, product_id)
