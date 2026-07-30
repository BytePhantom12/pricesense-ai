from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate
from app.utils.exceptions import ConflictError, NotFoundError
from app.services.base_service import BaseService


class ProductService(BaseService):
    def __init__(self, db: Session) -> None:
        super().__init__(db)
        self.repository = ProductRepository(db)

    def list_products(self, *, offset: int = 0, limit: int = 100) -> list[Product]:
        return self.repository.list(offset=offset, limit=limit)

    def get_product(self, product_id: int) -> Product:
        product = self.repository.get(product_id)
        if product is None:
            raise NotFoundError("Product not found")
        return product

    def create_product(self, product_in: ProductCreate) -> Product:
        if self.repository.get_by_sku(product_in.sku):
            raise ConflictError("A product with this SKU already exists")
        product = self.repository.create(product_in)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(self, product_id: int, product_in: ProductUpdate) -> Product:
        product = self.get_product(product_id)
        update_data = product_in.model_dump(exclude_unset=True)
        if "sku" in update_data:
            existing_product = self.repository.get_by_sku(update_data["sku"])
            if existing_product and existing_product.id != product.id:
                raise ConflictError("A product with this SKU already exists")
        for field, value in update_data.items():
            setattr(product, field, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> None:
        product = self.get_product(product_id)
        self.db.delete(product)
        self.db.commit()
