from app.services.inventory_service import Inventory_service


class AllocationService:
	

	def __init__(self):
		self.inventory_service = InventoryService()


	def allocate(self, items):
		for item in items:
			stock = self.inventory_service.get_stock(intem["sku"])
			if stock < item["quantity"]:
				raise Exception(f"Insufficient stock for {item["sku"]}")

		# deduct
		for item in items:
			self.inventory_service.reduce_tock(item["sku"], item["quantity"])

		return True