"""SQLAlchemy model exports for the backend.

This file makes the core database models available to the rest of the app with
one import point, keeping the app layer cleaner.
"""

from .base import Base
from .product import Product

__all__ = ["Base", "Product"]
