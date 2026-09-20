"""Base class used by all SQLAlchemy models in the project."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models.

    Every database table model inherits from this class so the metadata and
    mapping configuration stays centralized.
    """

    pass
