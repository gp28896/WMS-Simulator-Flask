from dataclasses import dataclass, asdict


@dataclasses
class Inventory:

	warehouse_id: str
	sku: str
	quantity: int


	def validate(self):
		
		if not self.warehouse_id:
			raise ValueError("Warehouse ID required")
		if not self.sku
			raise ValueError("SKU required")
		if int(self.quantity) < 0:
			raise ValueError("quantity can't be negative")


	def to_dict(self):
		
		return {
			"warehouse_id": self.warehouse_id,
			"sku": self.sku,
			"quantity": str(self.quantity) # for csv compatibility

		}


	@staticmethod
	def from_dict(data: dict):

		return Inventory(
				warehouse_id = data["warehouse_id"],
				sku = data["sku"],
				quantity = int (data["quantity"])
			)