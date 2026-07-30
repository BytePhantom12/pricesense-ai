from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.repositories.product_repository import ProductRepository
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.utils.exceptions import NotFoundError
from app.services.base_service import BaseService


class TransactionService(BaseService):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self.repository = TransactionRepository(db)
        self.product_repository = ProductRepository(db)

    def list_transactions(self, *, offset: int = 0, limit: int = 100) -> list[Transaction]:
        return self.repository.list(offset=offset, limit=limit)

    def get_transaction(self, transaction_id: int) -> Transaction:
        transaction = self.repository.get(transaction_id)
        if transaction is None:
            raise NotFoundError("Transaction not found")
        return transaction

    def create_transaction(self, transaction_in: TransactionCreate) -> Transaction:
        if self.product_repository.get(transaction_in.product_id) is None:
            raise NotFoundError("Product not found")
        transaction = self.repository.create(transaction_in)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def update_transaction(self, transaction_id: int, transaction_in: TransactionUpdate) -> Transaction:
        transaction = self.get_transaction(transaction_id)
        update_data = transaction_in.model_dump(exclude_unset=True)
        if "product_id" in update_data and self.product_repository.get(update_data["product_id"]) is None:
            raise NotFoundError("Product not found")
        for field, value in update_data.items():
            setattr(transaction, field, value)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def delete_transaction(self, transaction_id: int) -> None:
        transaction = self.get_transaction(transaction_id)
        self.db.delete(transaction)
        self.db.commit()
