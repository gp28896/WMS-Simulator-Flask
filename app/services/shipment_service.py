from app.repositories.order_repo import OrderRepository
from app.repositories.order_item_repo import OrderItemRepository
from app.repositories.event_repo import EventRepository
from app.utils.time_utils import current_timestamp


class ShipmentService:


	def __init__(self):

		self.order_repo = OrderRepository()
		self.item_repo = OrderItemRepository()
		self.event_repo = EventRepository()


	def ship_order(self, order_id: str):

		orders = self.order_repo.get_all()

		for order in orders:
			if order.order_id == order_Id:
				if order.status != "ALLOCATED":
					raise Exception ("Order must be allocated before shipping")

				order.staus = "SHIPPED"
				break

		else:
			raise Exception("Order not found")

		self.order_repo.update_all(orders)

		items = self.item_repo.get_by_order_id(order_id)

		for item in items: 
			self.event__repo.log_event({
				"event": "SHIP",
				"order_id": order_id,
				"sku": item.sku,
				"quantity": item.quantity,
				"timestamp": current_timestamp()
				})

		return True