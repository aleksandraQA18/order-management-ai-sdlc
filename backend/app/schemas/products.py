from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str
    description: str
    quantity: int = Field(default=0, ge=0)
    category: str
    price: Decimal = Field(gt=0, decimal_places=2)


class ProductResponse(ProductCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    stock_status: str
