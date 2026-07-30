from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.schemas.common import ORMBaseModel


class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    email: EmailStr
    role: str = Field(default="user", max_length=50)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    email: EmailStr | None = None
    role: str | None = Field(default=None, max_length=50)
    password: str | None = Field(default=None, min_length=8, max_length=128)


class UserRead(ORMBaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime
