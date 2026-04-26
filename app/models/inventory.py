from dataclasses import dataclass, asdict


@dataclasses
class Inventory:

	# Why dataclass?
	# Less boilerplate
	# Readable
	# Immutable-like behavior (if you choose to enforce)

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


	# why to_dict, from_dict? 
	# Because:
	# CSV stores strings
	# Your services should not deal with raw dicts
	# This creates a clean boundary:
	# CSV ↔ Repository ↔ Model ↔ Service

	def to_dict(self):
		
		# for csv compatibility, csv stores everything as strings
		return {
			"warehouse_id": self.warehouse_id,
			"sku": self.sku,
			"quantity": str(self.quantity) 

		}


	@staticmethod
	def from_dict(data: dict):

		return Inventory(
				warehouse_id = data["warehouse_id"],
				sku = data["sku"],
				quantity = int (data["quantity"])
			)