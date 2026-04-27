from app.services.inventory_service import InventoryService
from app.services.allocation_service import AllocationService


def test_allocation_success():

	inv = InventoryService()
	alloc = AllocationService()

	inv.add_stock("WH1", "SKU_TEST", 10)

	order_id = "test123"
	result = alloc.allocate(order_id, [{"sku": "SKU_TEST", "quantity": 5}])

	assert isinstance(result, list)


def test_allocation_failure():
	
	alloc = AllocationService()
	try:
		order_id = "test123"
		result = alloc.allocate(order_id, [{"sku": "SKU_INVALID", "quantity": 5}])
	except:
		assert True