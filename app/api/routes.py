from app.api.order_routes import register_order_routes


def register_routes(app):
	register_order_routes(app)


	@app.route("/")
	def home():
		return {"Message": "WMS Running"}