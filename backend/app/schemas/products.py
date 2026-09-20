"""Validation and response schemas for product payloads.

These models guarantee that incoming data matches the API contract before the
service layer stores it and shape the JSON returned to clients.
"""

from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    """Fields required when creating a product through the API."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "example": {
                "name": "API Testing Fundamentals",
                "description": (
                    "Hands-on course covering API testing principles and "
                    "practical workflows"
                ),
                "category": "QA Courses",
                "price": 89.99,
            }
        },
    )

    name: str = Field(examples=["API Testing Fundamentals"])
    description: str = Field(
        examples=[
            ("Hands-on course covering API testing principles and practical workflows")
        ]
    )
    category: str = Field(examples=["QA Courses"])
    price: Decimal = Field(gt=0, decimal_places=2, examples=[89.99])


class ProductResponse(ProductCreate):
    """Returned product data, including the database ID."""

    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "API Testing Fundamentals",
                "description": (
                    "Hands-on course covering API testing principles and "
                    "practical workflows"
                ),
                "category": "QA Courses",
                "price": 89.99,
            }
        },
    )

    id: UUID = Field(examples=["3fa85f64-5717-4562-b3fc-2c963f66afa6"])
