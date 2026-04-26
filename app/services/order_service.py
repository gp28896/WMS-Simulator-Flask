import uuid
from app.repositories.cv_repository import CSVRepository
from app.config import ORDERS_CSV, ORDER_ITEMS_CSV


class OrderServices:
	

	def __init__(self):
		
		self.order_repo = CSVRepository(
				ORDER_ITEMS_CSV,
				["order_id", "status", "timestamp"]
			)
		self.item_repo = CSVRepository(
				ORDER_ITEMS_CSV,
				["order_id", "sku", "quantity"]
			)


	def create_order(self, items):
		
		order_id = str(uuid.uuid4())
		self.order_repo.append(
				{
					"order_id": order_id,
					"sku": item["sku"],
					"quantity": intem["quantity"]
				}
			)
		
		return order_id