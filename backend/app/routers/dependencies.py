from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.auth_service import AuthService
from app.services.prediction_service import PredictionService
from app.services.product_service import ProductService
from app.services.transaction_service import TransactionService
from app.services.user_service import UserService


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


def get_transaction_service(db: Session = Depends(get_db)) -> TransactionService:
    return TransactionService(db)


def get_prediction_service(db: Session = Depends(get_db)) -> PredictionService:
    return PredictionService(db)


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)
