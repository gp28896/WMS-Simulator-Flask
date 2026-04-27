import random
from app.services.order_service import order_service
from app.services.allocation_service import AllocationService


order_service = OrderService()
allocation_service = AllocationService()


SKUS = ["SKU1", "SKU2", "SKU3"]


def simulate(n = 20):
	for _ in range(n):
		items = [{
			"sku": random.choice(SKUS),
			"quantity": random.randind(1, 5)
		}]

		order_id = order_service.allocate(items)
		
		try:
			allocation_service.allocate(items)
			print(f"Order {order_id} allocated")
		except Exception as e:
			print(f"Order {order_id} failed to allocate. {e}")


if __name__ == "__main__":
	simulate()