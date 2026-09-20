from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import get_db
from app.models import Base
from main import create_app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db() -> Generator[Session, None, None]:
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app = create_app()
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_create_product_contract(client: TestClient) -> None:
    payload = {
        "name": "API Testing Fundamentals",
        "description": (
            "Hands-on course covering API testing principles and practical workflows"
        ),
        "category": "QA Courses",
        "price": 89.99,
    }

    response = client.post("/api/products", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["description"] == payload["description"]
    assert body["category"] == payload["category"]
    assert body["price"] == "89.99"
    assert "id" in body


def test_get_products_contract(client: TestClient) -> None:
    payload = {
        "name": "Playwright Automation",
        "description": "Automation course for browser and API validation",
        "category": "Automation",
        "price": 79.99,
    }

    create_response = client.post("/api/products", json=payload)
    product_id = create_response.json()["id"]

    response = client.get("/api/products?page=1&page_size=20")

    assert response.status_code == 200
    products = response.json()
    assert len(products) >= 1
    assert any(item["id"] == product_id for item in products)
    assert all("stock_status" not in item for item in products)


def test_missing_product_contract(client: TestClient) -> None:
    missing_id = "00000000-0000-0000-0000-000000000001"

    response = client.get(f"/api/products/{missing_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"
