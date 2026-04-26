from dataclass import dataclass, asdict

@dataclass
class OrderItem:
	
	order_id: str
	sku: str
	quantity: int


	def validate(self):
		
		if not self.order_id: 
			raise ValueError("Order ID required")
		if not self.sku:
			raise ValueError("SKU required")
		if int(self.quantity) <= 0:
				raise ValueError("Quantity must be greater than zero")


	def to_dict(self):
		
		return {
			"order_id": self.order_id,
			"sku": self.sku,
			"quantity": str(self.quantity) # CSV compatibility

		}


	@staticmethod
	def from_dict(data: dict):
		
		return OrderItem(
				order_id = data["order_id"],
				sku = data["sku"],
				quantity = int(data["quantity"])
			)


