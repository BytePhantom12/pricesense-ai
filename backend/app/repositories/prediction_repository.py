from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.prediction import Prediction
from app.repositories.base import BaseRepository


class PredictionRepository(BaseRepository[Prediction]):
    model = Prediction

    def __init__(self, db: Session) -> None:
        super().__init__(db)

    def list_by_product(self, product_id: int) -> list[Prediction]:
        statement = select(Prediction).where(Prediction.product_id == product_id)
        return list(self.db.scalars(statement).all())
