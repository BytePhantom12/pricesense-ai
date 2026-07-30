from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False, index=True)
    purchase_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    total_revenue: Mapped[float] = mapped_column(Float, nullable=False)
    transaction_timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    customer_region: Mapped[str] = mapped_column(String(120), nullable=False)
    customer_gender: Mapped[str] = mapped_column(String(50), nullable=False)
    customer_age_band: Mapped[str] = mapped_column(String(50), nullable=False)
    customer_income_band: Mapped[str] = mapped_column(String(50), nullable=False)

    product = relationship("Product", back_populates="transactions")
