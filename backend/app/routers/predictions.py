from fastapi import APIRouter, Depends, Query, status

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.routers.dependencies import get_prediction_service
from app.schemas.prediction import PredictionCreate, PredictionRead, PredictionUpdate
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/predictions", tags=["Predictions"])


@router.get("/", response_model=list[PredictionRead])
def list_predictions(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=1000),
    current_user: User = Depends(get_current_user),
    prediction_service: PredictionService = Depends(get_prediction_service),
) -> list[PredictionRead]:
    return prediction_service.list_predictions(offset=offset, limit=limit)


@router.get("/{prediction_id}", response_model=PredictionRead)
def read_prediction(
    prediction_id: int,
    current_user: User = Depends(get_current_user),
    prediction_service: PredictionService = Depends(get_prediction_service),
) -> PredictionRead:
    return prediction_service.get_prediction(prediction_id)


@router.post("/", response_model=PredictionRead, status_code=status.HTTP_201_CREATED)
def create_prediction(
    prediction_in: PredictionCreate,
    current_user: User = Depends(get_current_user),
    prediction_service: PredictionService = Depends(get_prediction_service),
) -> PredictionRead:
    return prediction_service.create_prediction(prediction_in)


@router.put("/{prediction_id}", response_model=PredictionRead)
def update_prediction(
    prediction_id: int,
    prediction_in: PredictionUpdate,
    current_user: User = Depends(get_current_user),
    prediction_service: PredictionService = Depends(get_prediction_service),
) -> PredictionRead:
    return prediction_service.update_prediction(prediction_id, prediction_in)


@router.delete("/{prediction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prediction(
    prediction_id: int,
    current_user: User = Depends(get_current_user),
    prediction_service: PredictionService = Depends(get_prediction_service),
) -> None:
    prediction_service.delete_prediction(prediction_id)
