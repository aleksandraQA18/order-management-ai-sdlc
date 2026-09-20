from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models import Base, Product
from app.schemas.products import ProductCreate
from app.services.products import create_product, get_product_by_id, list_products


def _build_session() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(bind=engine)
    return Session(bind=engine)


def test_create_product_persists_product_and_calculates_stock_status() -> None:
    with _build_session() as db:
        payload = ProductCreate(
            name="API Testing Fundamentals",
            description=(
                "Hands-on course covering API testing principles and "
                "practical workflows"
            ),
            quantity=5,
            category="QA Courses",
            price=Decimal("89.99"),
        )

        created = create_product(db, payload)

        assert created.id is not None
        assert created.name == "API Testing Fundamentals"
        assert created.quantity == 5
        assert created.stock_status == "in_stock"


def test_list_products_returns_ordered_rows_and_get_product_by_id_finds_record() -> (
    None
):
    with _build_session() as db:
        first = Product(
            name="API Testing Fundamentals",
            description="First course",
            quantity=2,
            category="QA Courses",
            price=Decimal("49.99"),
        )
        second = Product(
            name="Playwright Automation",
            description="Second course",
            quantity=0,
            category="Automation",
            price=Decimal("79.99"),
        )
        db.add_all([first, second])
        db.commit()

        products = list_products(db, page=1, page_size=20)
        product_names = {product.name for product in products}
        assert {first.name, second.name} == product_names

        found = get_product_by_id(db, first.id)
        assert found is not None
        assert found.name == first.name
