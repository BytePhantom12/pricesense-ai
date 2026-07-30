from fastapi import APIRouter, Depends, status

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.routers.dependencies import get_auth_service
from app.schemas.token import AuthResponse
from app.schemas.user import UserCreate, UserLogin, UserRead
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
def register(
    user_in: UserCreate,
    auth_service: AuthService = Depends(get_auth_service),
) -> AuthResponse:
    return auth_service.register(user_in)


@router.post("/login", response_model=AuthResponse)
def login(
    login_in: UserLogin,
    auth_service: AuthService = Depends(get_auth_service),
) -> AuthResponse:
    return auth_service.login(login_in)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)) -> UserRead:
    return UserRead.model_validate(current_user)
