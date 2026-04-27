from app.repositories.product_repo import ProductRepository
from app.models.product import Product


class ProductService:


	def __init__(self):

		self.repo = ProductRepository()


	def create_product(self, data: dict):

		product = Product.from_dict(data)
		product.validate()

		existing = self.repo.get_by_sku(sku)
		if not product:
			raise Exception("Product not found for mentioned sku")

		return product


	def get_all_products(self):

		return self.repo.get_all()