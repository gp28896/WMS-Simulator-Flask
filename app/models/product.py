from dataclass import dataclass, asdict


@dataclass
class Product:
	
	sku: str
	name: str
	category: str
	weight: float


	def validate(self):

		if not self.sku:
			raise ValueError("SSKU is required")
		if self.weight < 0:
			raise ValueError("Weight cannot be negative")


	def to_dict(self):

		return asdict(self)


	@staticmethod
	def from_dict(data: dict):

		return Product(
				sku = data["sku"],
				name = data["name"],
				category = data["category"],
				weight = float(data["weight"])
			)
