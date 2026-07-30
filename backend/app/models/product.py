from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(255), nullable=False)
    sku: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    historical_price: Mapped[float] = mapped_column(Float, nullable=False)
    current_price: Mapped[float] = mapped_column(Float, nullable=False)
    competitor_price: Mapped[float] = mapped_column(Float, nullable=False)
    inventory_level: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price_elasticity: Mapped[float] = mapped_column(Float, nullable=False)
    competitor_popularity: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    market_segment: Mapped[str] = mapped_column(String(120), nullable=False)
    promotion_status: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    seasonal_indicator: Mapped[str] = mapped_column(String(50), nullable=False, default="none")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    transactions = relationship("Transaction", back_populates="product", cascade="all, delete-orphan")
    predictions = relationship("Prediction", back_populates="product", cascade="all, delete-orphan")
