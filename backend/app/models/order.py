from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )
    customer_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    product: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
