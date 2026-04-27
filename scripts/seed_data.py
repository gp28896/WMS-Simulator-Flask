from app.services.product_service import ProductService
from app.services.inventory_service import InventoryService


product_service = ProductService()
inventory_service = InventoryService()


def seed():
	
	products = [
        {"sku": "SKU1", "name": "Laptop", "category": "Electronics", "weight": 2.5},
        {"sku": "SKU2", "name": "Phone", "category": "Electronics", "weight": 0.5},
        {"sku": "SKU3", "name": "Chair", "category": "Furniture", "weight": 7.0},
    ]
    
    for p in products:
    	try:
    		product_service.create_product(p)
    	except:
    		pass


	inventory_service.add_stock("WH1", "SKU1", 50)    
	inventory_service.add_stock("WH1", "SKU2", 100)
    inventory_service.add_stock("WH2", "SKU3", 20)



if __name__ == "__main__":
	seed()
	print("Data seeded successfully")
