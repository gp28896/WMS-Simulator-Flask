from app.repositories.cv_repository import CSVRepository
from app.config import INVENTORY_CSV

class InventoryService:

	def __init__(self):
		self.repo = CSVRepository(
					INVENTORY_CSV, 
					["warehouse_id", "sku", "quantity"]
			)


	def get_stock(self, sku: str) -> int:
		rows = self.repo.read_all()
		return sum(int(r["quantity"])for r in rows if r["sku"] == sku)		


	def add_stock(self, warehouse_id: str, sku: str, quantity: int):
		self.repo.append(
				"warehouse_id": warehouse_id,
				"sku": sku,
				"quantity": quantity
			)


	def reduce_stock(self, warehouse_id: str, quantity: int):
		rows = self.repo_read_all()
		remaining = quantity

		for r in rows:
			if r["sku"] == sku and remaining > 0:
				available = int(r["quantity"])
				deduction = min(available, remaining)
				r["quantity"] = str(available - deduction)
				remaining -= deduction

		if remaining > 0:
			raise Exception("Insufficient stock. ")

		self.repo_write_all(rows)