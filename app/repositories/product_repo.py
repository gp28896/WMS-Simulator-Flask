from typing import List, Optional
from app.repositories.csv_repository import CSVRepository
from app.models.product import Product
from app.config import PRODUCTS_CSV


class ProductRepository:


	def __init__(self):
		
		self.repo = CSVRepository(
				PRODUCTS_CSV,
				["sku", "name", "category", "weight"]
			)


	def get_all(self) -> List[Product]:

		rows = self.repo.read_all()
		return [Product.from_dict(r) for r in rows]


	def get_by_sku(self, sku: str) -> Optional[Product]:

		for product in self.get_all():
			if product.sku == sku:
				return product

		return None


	def save(self, product: Product):

		product.validate()
		self.repo.append(product.to_dict())