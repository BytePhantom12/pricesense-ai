from pydantic import BaseModel

from app.schemas.common import ORMBaseModel
from app.schemas.user import UserRead


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: str | None = None


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthResponse(ORMBaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRead
