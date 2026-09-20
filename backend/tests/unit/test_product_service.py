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


def test_create_product_persists_product_record() -> None:
    with _build_session() as db:
        payload = ProductCreate(
            name="API Testing Fundamentals",
            description=(
                "Hands-on course covering API testing principles and "
                "practical workflows"
            ),
            category="QA Courses",
            price=Decimal("89.99"),
        )

        created = create_product(db, payload)

        assert created.id is not None
        assert created.name == "API Testing Fundamentals"
        assert created.category == "QA Courses"
        assert created.price == Decimal("89.99")


def test_list_products_returns_ordered_rows_and_get_product_by_id_finds_record() -> (
    None
):
    with _build_session() as db:
        first = Product(
            name="API Testing Fundamentals",
            description="First course",
            category="QA Courses",
            price=Decimal("49.99"),
        )
        second = Product(
            name="Playwright Automation",
            description="Second course",
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
