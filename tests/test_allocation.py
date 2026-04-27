from app.services.inventory_service import InventoryService
from app.services.allocation_service import AllocationService


def test_allocation_success():

	inv = InventoryService()
	alloc = AllocationService()

	inv.add_stock("WH1", "SKU_TEST", 10)

	result = alloc.allocate([{"sku": "SKU_TEST", "quantity": 5}])
	assert result is True


def test_allocation_failure():
	
	alloc = AllocationService()
	try:
		alloc.allocate([{"sku": "INVALID", "quantity": 5}])
	except:
		assert True