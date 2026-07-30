from app.routers.auth import router as auth_router
from app.routers.predictions import router as predictions_router
from app.routers.products import router as products_router
from app.routers.transactions import router as transactions_router
from app.routers.users import router as users_router

__all__ = [
    "auth_router",
    "users_router",
    "products_router",
    "transactions_router",
    "predictions_router",
]
