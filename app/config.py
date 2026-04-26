import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_DIR = os.path.join(DATA_DIR, "csv")
JSON_DIR = os.path.join(DATA_DIR, "json")

PRODUCTS_CSV = os.path.join(CSV_DIR, "products.csv")
INVENTORY_CSV = os.path.join(CSV_DIR, "inventory.csv")
ORDERS_CSV = os.path.join(CSV_DIR, "orders.csv")
ORDER_ITEMS_CSV = os.path.join(CSV_DIR, "order_items.csv")

EVENTS_JSON = os.path.join(JSON_DIR, "events.json")