from app.repositories.inventory_repo import InventoryRepository

class InventoryService:
    def __init__(self, repo=None):
        self.repo = repo or InventoryRepository()

    def get_stock(self, sku: str) -> int:
        rows = self.repo.get_all()
        return sum(inv.quantity for inv in rows if inv.sku == sku)

    def add_stock(self, warehouse_id: str, sku: str, quantity: int):
        from app.models.inventory import Inventory
        inv = Inventory(warehouse_id, sku, quantity)
        inv.validate()
        self.repo.save(inv)

    def reduce_stock(self, sku: str, quantity: int):
        inventories = self.repo.get_all()
        remaining = quantity

        for inv in inventories:
            if inv.sku == sku and remaining > 0:
                deduction = min(inv.quantity, remaining)
                inv.quantity -= deduction
                remaining -= deduction

        if remaining > 0:
            raise Exception("Insufficient stock")

        self.repo.update_all(inventories)