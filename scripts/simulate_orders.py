import random
from app.services.order_service import OrderService
from app.services.allocation_service import AllocationService


order_service = OrderService()
allocation_service = AllocationService()

SKUS = ["SKU1", "SKU2", "SKU3"]


def simulate(n=10):
    for _ in range(n):
        items = [{
            "sku": random.choice(SKUS),
            "quantity": random.randint(1, 5)
        }]

        order_id = order_service.create_order(items)

        try:
            allocation_service.allocate(order_id, items)
            print(f"Order {order_id} allocated")
        except Exception as e:
            print(f"Order {order_id} failed: {e}")


if __name__ == "__main__":
    simulate()