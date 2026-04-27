import os
from app.config import CSV_DIR, JSON_DIR


CSV_HEADERS = {
    "products.csv": "sku,name,category,weight\n",
    "inventory.csv": "warehouse_id,sku,quantity\n",
    "orders.csv": "order_id,status,timestamp\n",
    "order_items.csv": "order_id,sku,quantity\n",
}


def reset_files():

    for file, header in CSV_HEADERS.items():
        path = os.path.join(CSV_DIR, file)
        with open(path, "w") as f:
            f.write(header)

    for file in os.listdir(JSON_DIR):
        path = os.path.join(JSON_DIR, file)
        with open(path, "w") as f:
            f.write("[]")

if __name__ == "__main__":

	reset_files()
	print("Data reset completed successfully")	
