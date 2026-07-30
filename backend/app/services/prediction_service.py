from sqlalchemy.orm import Session

from app.models.prediction import Prediction
from app.repositories.prediction_repository import PredictionRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.prediction import PredictionCreate, PredictionUpdate
from app.utils.exceptions import NotFoundError
from app.services.base_service import BaseService


class PredictionService(BaseService):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self.repository = PredictionRepository(db)
        self.product_repository = ProductRepository(db)

    def list_predictions(self, *, offset: int = 0, limit: int = 100) -> list[Prediction]:
        return self.repository.list(offset=offset, limit=limit)

    def get_prediction(self, prediction_id: int) -> Prediction:
        prediction = self.repository.get(prediction_id)
        if prediction is None:
            raise NotFoundError("Prediction not found")
        return prediction

    def create_prediction(self, prediction_in: PredictionCreate) -> Prediction:
        if self.product_repository.get(prediction_in.product_id) is None:
            raise NotFoundError("Product not found")
        prediction = self.repository.create(prediction_in)
        self.db.commit()
        self.db.refresh(prediction)
        return prediction

    def update_prediction(self, prediction_id: int, prediction_in: PredictionUpdate) -> Prediction:
        prediction = self.get_prediction(prediction_id)
        update_data = prediction_in.model_dump(exclude_unset=True)
        if "product_id" in update_data and self.product_repository.get(update_data["product_id"]) is None:
            raise NotFoundError("Product not found")
        for field, value in update_data.items():
            setattr(prediction, field, value)
        self.db.commit()
        self.db.refresh(prediction)
        return prediction

    def delete_prediction(self, prediction_id: int) -> None:
        prediction = self.get_prediction(prediction_id)
        self.db.delete(prediction)
        self.db.commit()
