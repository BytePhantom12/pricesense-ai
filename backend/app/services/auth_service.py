from datetime import timedelta

from sqlalchemy.orm import Session

from app.auth.security import create_access_token, verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.token import AuthResponse
from app.schemas.user import UserCreate, UserLogin, UserRead
from app.services.base_service import BaseService
from app.services.user_service import UserService
from app.utils.exceptions import AuthenticationError, ConflictError


class AuthService(BaseService):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self.user_repository = UserRepository(db)
        self.user_service = UserService(db)

    def register(self, user_in: UserCreate) -> AuthResponse:
        if self.user_repository.get_by_email(user_in.email):
            raise ConflictError("A user with this email already exists")
        user = self.user_service.create_user(user_in)
        token = create_access_token(subject=user.email)
        return AuthResponse(access_token=token, token_type="bearer", user=UserRead.model_validate(user))

    def login(self, login_in: UserLogin) -> AuthResponse:
        user = self.user_repository.get_by_email(login_in.email)
        if user is None or not verify_password(login_in.password, user.hashed_password):
            raise AuthenticationError("Incorrect email or password")
        token = create_access_token(subject=user.email)
        return AuthResponse(access_token=token, token_type="bearer", user=UserRead.model_validate(user))
