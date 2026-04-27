from typing import List
from app.repositories.csv_repository import CSVRepository
from app.models.order import Order
from app.config import ORDERS_CSV


class OrderRepository:


	def __init__(self):

		self.repo = CSVRepository(
					ORDERS_CSV,
					["order_id", "status", "timestamp"]
			)


	def save(self, order: Order):

		self.repo.append({
			"order_id": order.order_id,
			"status": order.status,
			"timestamp": order.timestamp
			})


	def get_all(self) -> List[Order]:

		rows = self.repo.read_all()
		return [Order(**r) for r in rows]


	def update_all(self, orders: List[Order]):

		rows = [o.__dict__ for o in orders]
		self.repo.write_all(rows)