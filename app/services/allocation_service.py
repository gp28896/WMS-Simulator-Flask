from app.services.inventory_service import InventoryService
from app.repositories.order_repo import OrderRepository
from app.utils.logger import logger


class AllocationService:

    def __init__(self, inventory_service=None, order_repo=None):
        self.inventory_service = inventory_service or InventoryService()
        self.order_repo = order_repo or OrderRepository()

    def allocate(self, order_id: str, items: list):
        inventories = self.inventory_service.repo.get_all()
        allocations = []

        for item in items:
            sku = item["sku"]
            required = item["quantity"]

            sku_inventories = [i for i in inventories if i.sku == sku]
            sku_inventories.sort(key=lambda x: x.quantity, reverse=True)

            remaining = required

            for inv in sku_inventories:
                if remaining <= 0:
                    break

                take = min(inv.quantity, remaining)

                allocations.append({
                    "warehouse_id": inv.warehouse_id,
                    "sku": sku,
                    "allocated": take
                })

                inv.quantity -= take
                remaining -= take

            if remaining > 0:
                logger.error(f"Insufficient stock for {sku}")
                raise Exception(f"Insufficient stock for {sku}")

        # persist inventory
        self.inventory_service.repo.update_all(inventories)

        # update order status
        found = False

        for o in orders:
            if o.order_id == order_id:
                o.status = "ALLOCATED"
                found = True
                logger.info(f"Order {order_id} allocated")
                break

        if not found:
            raise Exception(f"Order {order_id} not found")
                self.order_repo.update_all(orders)

        return allocations