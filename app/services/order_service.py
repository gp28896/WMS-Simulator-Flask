import uuid
from datetime import datetime
from app.repositories.order_repo import OrderRepository
from app.repositories.order_item_repo import OrderItemRepository
from app.models.order import Order
from app.models.order_item import OrderItem


class OrderService:

    def __init__(self, order_repo=None, item_repo=None):
        self.order_repo = order_repo or OrderRepository()
        self.item_repo = item_repo or OrderItemRepository()

    def create_order(self, items: list) -> str:
        order_id = str(uuid.uuid4())

        # create order
        order = Order(
            order_id=order_id,
            status="CREATED",
            timestamp=datetime.utcnow().isoformat()
        )
        self.order_repo.save(order)

        # create order items
        for item in items:
            order_item = OrderItem(
                order_id=order_id,
                sku=item["sku"],
                quantity=item["quantity"]
            )
            order_item.validate()
            self.item_repo.save(order_item)

        return order_id