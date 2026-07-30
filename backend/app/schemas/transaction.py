from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseModel


class TransactionBase(BaseModel):
    product_id: int = Field(gt=0)
    purchase_quantity: int = Field(gt=0)
    total_revenue: float = Field(ge=0)
    transaction_timestamp: datetime | None = None
    customer_region: str = Field(min_length=1, max_length=120)
    customer_gender: str = Field(min_length=1, max_length=50)
    customer_age_band: str = Field(min_length=1, max_length=50)
    customer_income_band: str = Field(min_length=1, max_length=50)


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    product_id: int | None = Field(default=None, gt=0)
    purchase_quantity: int | None = Field(default=None, gt=0)
    total_revenue: float | None = Field(default=None, ge=0)
    transaction_timestamp: datetime | None = None
    customer_region: str | None = Field(default=None, min_length=1, max_length=120)
    customer_gender: str | None = Field(default=None, min_length=1, max_length=50)
    customer_age_band: str | None = Field(default=None, min_length=1, max_length=50)
    customer_income_band: str | None = Field(default=None, min_length=1, max_length=50)


class TransactionRead(ORMBaseModel):
    id: int
    product_id: int
    purchase_quantity: int
    total_revenue: float
    transaction_timestamp: datetime
    customer_region: str
    customer_gender: str
    customer_age_band: str
    customer_income_band: str
