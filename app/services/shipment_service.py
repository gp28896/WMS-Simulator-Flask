from app.repositories.order_repo import OrderRepository
from app.repositories.order_item_repo import OrderItemRepository
from app.repositories.event_repo import EventRepository
from app.utils.time_utils import current_timestamp


class ShipmentService:

    def __init__(self, order_repo=None, item_repo=None, event_repo=None):
        self.order_repo = order_repo or OrderRepository()
        self.item_repo = item_repo or OrderItemRepository()
        self.event_repo = event_repo or EventRepository()

    def ship_order(self, order_id: str):
        orders = self.order_repo.get_all()

        for order in orders:
            if order.order_id == order_id:
                if order.status != "ALLOCATED":
                    raise Exception("Order must be allocated before shipping")

                order.status = "SHIPPED"
                break
        else:
            raise Exception("Order not found")

        self.order_repo.update_all(orders)

        items = self.item_repo.get_order_by_id(order_id)

        for item in items:
            self.event_repo.log_event({
                "event": "SHIP",
                "order_id": order_id,
                "sku": item.sku,
                "quantity": item.quantity,
                "timestamp": current_timestamp()
            })

        return True