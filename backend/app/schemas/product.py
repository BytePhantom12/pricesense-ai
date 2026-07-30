from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseModel


class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    category: str = Field(min_length=1, max_length=255)
    sku: str = Field(min_length=1, max_length=120)
    historical_price: float = Field(gt=0)
    current_price: float = Field(gt=0)
    competitor_price: float = Field(gt=0)
    inventory_level: int = Field(ge=0)
    price_elasticity: float = Field(ge=-10, le=10)
    competitor_popularity: float = Field(ge=0, le=100)
    market_segment: str = Field(min_length=1, max_length=120)
    promotion_status: bool = False
    seasonal_indicator: str = Field(default="none", max_length=50)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    category: str | None = Field(default=None, min_length=1, max_length=255)
    sku: str | None = Field(default=None, min_length=1, max_length=120)
    historical_price: float | None = Field(default=None, gt=0)
    current_price: float | None = Field(default=None, gt=0)
    competitor_price: float | None = Field(default=None, gt=0)
    inventory_level: int | None = Field(default=None, ge=0)
    price_elasticity: float | None = Field(default=None, ge=-10, le=10)
    competitor_popularity: float | None = Field(default=None, ge=0, le=100)
    market_segment: str | None = Field(default=None, min_length=1, max_length=120)
    promotion_status: bool | None = None
    seasonal_indicator: str | None = Field(default=None, max_length=50)


class ProductRead(ORMBaseModel):
    id: int
    name: str
    category: str
    sku: str
    historical_price: float
    current_price: float
    competitor_price: float
    inventory_level: int
    price_elasticity: float
    competitor_popularity: float
    market_segment: str
    promotion_status: bool
    seasonal_indicator: str
    created_at: datetime
