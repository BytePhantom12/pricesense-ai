from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.base import BaseRepository


class TransactionRepository(BaseRepository[Transaction]):
    model = Transaction

    def __init__(self, db: Session) -> None:
        super().__init__(db)

    def list_by_product(self, product_id: int) -> list[Transaction]:
        statement = select(Transaction).where(Transaction.product_id == product_id)
        return list(self.db.scalars(statement).all())
