from datetime import datetime

from pydantic import BaseModel, Field

from app.schemas.common import ORMBaseModel


class PredictionBase(BaseModel):
    product_id: int = Field(gt=0)
    predicted_action: str = Field(min_length=1, max_length=120)
    confidence: float = Field(ge=0, le=1)
    recommended_price: float = Field(gt=0)
    predicted_demand: float = Field(ge=0)
    expected_revenue: float = Field(ge=0)
    revenue_improvement: float = Field(ge=-1000)


class PredictionCreate(PredictionBase):
    pass


class PredictionUpdate(BaseModel):
    product_id: int | None = Field(default=None, gt=0)
    predicted_action: str | None = Field(default=None, min_length=1, max_length=120)
    confidence: float | None = Field(default=None, ge=0, le=1)
    recommended_price: float | None = Field(default=None, gt=0)
    predicted_demand: float | None = Field(default=None, ge=0)
    expected_revenue: float | None = Field(default=None, ge=0)
    revenue_improvement: float | None = Field(default=None, ge=-1000)


class PredictionRead(ORMBaseModel):
    id: int
    product_id: int
    predicted_action: str
    confidence: float
    recommended_price: float
    predicted_demand: float
    expected_revenue: float
    revenue_improvement: float
    created_at: datetime
