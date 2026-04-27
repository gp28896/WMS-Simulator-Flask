from app.services.inventory_service import InventoryService
from app.repositories.order_repo import OrderRepository
from app.utils.logger import logger
import copy


class AllocationService:

    def __init__(self, inventory_service=None, order_repo=None):
        self.inventory_service = inventory_service or InventoryService()
        self.order_repo = order_repo or OrderRepository()

    def allocate(self, order_id: str, items: list):

        inventories = self.inventory_service.repo.get_all()
        inventories_copy = copy.deepcopy(inventories)

        allocations = []

        order = self.order_repo.get_by_id(order_id)
        if not order:
            raise Exception("Order not found")

        for item in items:
            if "sku" not in item or "quantity" not in item:
                raise Exception("Invalid item format")

            sku = item["sku"]
            required = item["quantity"]

            sku_inventories = [i for i in inventories_copy if i.sku == sku]

            if not sku_inventories:
                raise Exception(f"SKU {sku} not found")

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

        # persist ONLY after success
        self.inventory_service.repo.update_all(inventories_copy)

        orders = self.order_repo.get_all()

        for o in orders:
            if o.order_id == order_id:
                o.status = "ALLOCATED"
                break

        self.order_repo.update_all(orders)

        return allocations