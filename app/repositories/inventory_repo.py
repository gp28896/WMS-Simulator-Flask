from typing import List
from app.repositories.csv_repository import CSVRepository
from app.models.inventory import Inventory
from app.config import INVENTORY_CSV


class InventoryRepository:


	def __init__(self):

		self.repo = CSVRepository(
				INVENTORY_CSV,
				["warehouse_id", "sku", "quantity"]
			)

	def get_all(self) -> List[Inventory]:

		rows = self.repo.read_all()
		return [Inventory.from_dict(r) for r in rows]


	def save(self, inventory: Inventory):
		
		inventory.validate()
		self.repo.append(inventory.to_dict())


	def update_all(self, inventories: List[Inventory]):

		rows = [inv.to_dict() for inv in inventories]
		self.repo.write_all(rows)
