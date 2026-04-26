from app.services.inventory_service import InventoryService

def test_add_and_get_stock():
	service = InventoryService()
	service.add_stock("WH1", "SKU1", 10)
	assert service.get_stock("SKU1") >= 10
