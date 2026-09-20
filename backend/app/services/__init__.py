"""Application service layer.

The services package keeps the business and persistence logic separate from the
HTTP route layer, making the backend easier to reason about and extend.
"""

from app.services.products import create_product, get_product_by_id, list_products

__all__ = ["create_product", "get_product_by_id", "list_products"]
