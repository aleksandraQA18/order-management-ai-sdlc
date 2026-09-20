"""Product ORM model and inventory rules.

This model represents the main catalog item in the system and includes simple
business constraints such as non-negative quantity and positive price.
"""

from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    """Catalog item stored in the products table."""

    __tablename__ = "products"
    __table_args__ = (
        # Prevent invalid stock values and impossible pricing during database writes.
        CheckConstraint("quantity >= 0", name="ck_products_quantity_non_negative"),
        CheckConstraint("price > 0", name="ck_products_price_positive"),
    )

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )
    category: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    @property
    def stock_status(self) -> str:
        """Return a simple human-friendly status based on the stock quantity."""
        return "in_stock" if self.quantity and self.quantity > 0 else "out_of_stock"
