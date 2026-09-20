"""Unit tests covering product validation and catalog data rules.

These checks document the expected business rules for the QA Academy product
catalog so the application remains consistent with the approved concept.
"""

from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.models import Product
from app.schemas.products import ProductCreate


def make_product_create(**overrides: object) -> ProductCreate:
    """Build a valid product payload with optional overrides for targeted tests."""
    values: dict[str, object] = {
        "name": "API Testing Fundamentals",
        "description": "Hands-on course covering API testing principles",
        "category": "QA Courses",
        "price": Decimal("19.99"),
    }
    values.update(overrides)
    return ProductCreate(**values)


def test_product_create_accepts_valid_catalog_payload() -> None:
    product = make_product_create()

    assert product.name == "API Testing Fundamentals"
    assert product.category == "QA Courses"
    assert product.price == Decimal("19.99")


def test_product_create_rejects_extra_fields_like_quantity() -> None:
    """Inventory metadata is not part of the approved product contract."""
    with pytest.raises(ValidationError):
        ProductCreate(
            name="API Testing Fundamentals",
            description="Hands-on course covering API testing principles",
            category="QA Courses",
            price=Decimal("19.99"),
            quantity=5,
        )


@pytest.mark.parametrize("price", [Decimal("0"), Decimal("-1.00")])
def test_product_create_rejects_non_positive_price(price: Decimal) -> None:
    """Prices must always be greater than zero."""
    with pytest.raises(ValidationError):
        make_product_create(price=price)


def test_product_create_rejects_price_with_more_than_two_decimal_places() -> None:
    """Currency values are limited to two decimal places to match pricing rules."""
    with pytest.raises(ValidationError):
        make_product_create(price=Decimal("19.999"))


def test_product_model_can_be_created_without_inventory_fields() -> None:
    """Product records represent catalog items, not stock ledger entries."""
    product = Product(
        name="Playwright Automation",
        description="Automation course for browser and API validation",
        category="Automation",
        price=Decimal("79.99"),
    )

    assert product.name == "Playwright Automation"
    assert product.category == "Automation"
    assert product.price == Decimal("79.99")
