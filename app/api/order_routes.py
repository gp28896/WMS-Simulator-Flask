from flask import request, jsonify
from app.services.order_service import OrderService
from app.services.allocation_service import AllocationService


order_service = OrderService()
allocation_service = AllocationService()


def register_order_routes(app):

	@app.route("/orders", methods = ["POST"])
	def create_order():
		data = request.json
		order_id = order_service.create_order(data["items"])
		return jsonify({"order_id": order_id})


	@app.route("/orders/allocate", methods=["POST"])
	def allocate():
			data = request.json
			allocation_service.allocate(data["order_id"], data["items"])
			return {"Status": "Allocated"}