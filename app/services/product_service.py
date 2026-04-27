from app.repositories.product_repo import ProductRepository
from app.models.product import Product


class ProductService:

    def __init__(self, repo=None):
        self.repo = repo or ProductRepository()

    def create_product(self, data: dict):
        product = Product.from_dict(data)
        product.validate()

        existing = self.repo.get_by_sku(product.sku)
        if existing:
            raise Exception("Product already exists")

        self.repo.save(product)
        return product

    def get_all_products(self):
        return self.repo.get_all()