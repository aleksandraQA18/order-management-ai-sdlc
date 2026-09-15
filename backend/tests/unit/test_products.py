from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.models import Product
from app.schemas.products import ProductCreate


def make_product_create(**overrides: object) -> ProductCreate:
    values: dict[str, object] = {
        "name": "Desk",
        "description": "Wooden desk",
        "category": "Furniture",
        "price": Decimal("19.99"),
    }
    values.update(overrides)
    return ProductCreate(**values)


def test_product_create_defaults_quantity_to_zero() -> None:
    product = make_product_create()

    assert product.quantity == 0


@pytest.mark.parametrize(
    ("quantity", "expected_status"),
    [
        (0, "out_of_stock"),
        (1, "in_stock"),
        (25, "in_stock"),
    ],
)
def test_product_stock_status_is_derived_from_quantity(
    quantity: int,
    expected_status: str,
) -> None:
    product = Product(
        name="Desk",
        description="Wooden desk",
        quantity=quantity,
        category="Furniture",
        price=Decimal("19.99"),
    )

    assert product.stock_status == expected_status


@pytest.mark.parametrize("price", [Decimal("0"), Decimal("-1.00")])
def test_product_create_rejects_non_positive_price(price: Decimal) -> None:
    with pytest.raises(ValidationError):
        make_product_create(price=price)


def test_product_create_rejects_price_with_more_than_two_decimal_places() -> None:
    with pytest.raises(ValidationError):
        make_product_create(price=Decimal("19.999"))


def test_product_create_rejects_negative_quantity() -> None:
    with pytest.raises(ValidationError):
        make_product_create(quantity=-1)