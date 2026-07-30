from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from app.auth.security import hash_password
from app.utils.exceptions import ConflictError, NotFoundError
from app.services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self.repository = UserRepository(db)

    def list_users(self, *, offset: int = 0, limit: int = 100) -> list[User]:
        return self.repository.list(offset=offset, limit=limit)

    def get_user(self, user_id: int) -> User:
        user = self.repository.get(user_id)
        if user is None:
            raise NotFoundError("User not found")
        return user

    def get_user_by_email(self, email: str) -> User | None:
        return self.repository.get_by_email(email)

    def create_user(self, user_in: UserCreate) -> User:
        if self.repository.get_by_email(user_in.email):
            raise ConflictError("A user with this email already exists")
        user = User(
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
            role=user_in.role,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, user_in: UserUpdate) -> User:
        user = self.get_user(user_id)
        update_data = user_in.model_dump(exclude_unset=True)
        if "email" in update_data:
            existing_user = self.repository.get_by_email(update_data["email"])
            if existing_user and existing_user.id != user.id:
                raise ConflictError("A user with this email already exists")
        if "password" in update_data:
            update_data["hashed_password"] = hash_password(update_data.pop("password"))
        for field, value in update_data.items():
            setattr(user, field, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user_id: int) -> None:
        user = self.get_user(user_id)
        self.db.delete(user)
        self.db.commit()
