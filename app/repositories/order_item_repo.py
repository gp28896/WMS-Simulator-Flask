from typing import List
from app.repositories.csv_repository import CSVRepository
from app.models.order_item import OrderItem
from app.config import ORDER_ITEMS_CSV


class OrderItemRepository:


	def __init__(self):

		self.repo = CSVRepository(
				ORDER_ITEMS_CSV,
				["order_id", "sku", "quantity"]
			)


	def save(self, item: OrderItem):

		item.validate()
		self.repo.append(item.to_dict())


	def get_order_by_id(self, order_id: str) -> List[OrderItem]:

		rows = self.repo.read_all()
		return [
			OrderItem.from_dict(r)
			for r in rows
			if r["order_id"] == order_id
		]


	def get_all(self) -> List[OrderItem]:

		rows = self.repo.read_all()
		return [OrderItem.from_dict(r) for r in rows]


	def delete_by_order_id(self, order_id: str):
		
	    rows = self.repo.read_all()
	    filtered = [r for r in rows if r["order_id"] != order_id]
	    self.repo.write_all(filtered)