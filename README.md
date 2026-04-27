# WMS Simulator (Flask)

A lightweight **Warehouse Management System (WMS) simulator** built using Flask, CSV, and JSON.

This project models real-world backend concepts like:

* inventory management
* order lifecycle
* stock allocation
* event logging

without using a traditional database.

---

# Architecture Overview

```text
API Layer → Services → Repositories → CSV/JSON Files
```

* **Services** → Business logic (allocation, shipment)
* **Repositories** → Data access abstraction
* **CSV** → Relational-style storage
* **JSON** → Event logging

---

# Project Structure

```text
WMS-Simulator-Flask/
│
├── app/
├── data/
│   ├── csv/
│   └── json/
├── scripts/
├── tests/
├── run.py
```

---

# Setup & Run Instructions

## 1. Navigate to project

```bash
cd WMS-Simulator-Flask
```

---

## 2. Create virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Git Bash (Windows)
# OR
venv\Scripts\activate          # CMD
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Step 1: Reset Data (IMPORTANT)

```bash
python scripts/reset_data.py
```

 This clears:

* all CSV files
* all JSON logs

---

# Step 2: Seed Initial Data

```bash
python scripts/seed_data.py
```

This creates:

* sample products
* initial inventory in warehouses

---

# Step 3: Verify Data Creation

Open these files:

```text
data/csv/products.csv
data/csv/inventory.csv
```

### You should see:

**products.csv**

```text
sku,name,category,weight
SKU1,Laptop,Electronics,2.5
...
```

**inventory.csv**

```text
warehouse_id,sku,quantity
WH1,SKU1,50
...
```

If these are populated → your system is working correctly.

---

# Step 4: Run Flask Server

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

You should see:

```json
{"msg": "WMS Running"}
```

---

# Step 5: Simulate Orders

```bash
python scripts/simulate_orders.py
```

### Expected output:

```text
Order <id> allocated
Order <id> failed: Insufficient stock
```

---

# Step 6: Verify Inventory Changes

Open:

```text
data/csv/inventory.csv
```

Quantities should **decrease** after allocation.

---

# Step 7: Verify Event Logging

Open:

```text
data/json/events.json
```

You should see entries like:

```json
[
  {
    "event": "SHIP",
    "order_id": "...",
    "sku": "SKU1",
    "quantity": 2,
    "timestamp": "..."
  }
]
```

---

# Running Tests

```bash
pytest
```

---

# What This Confirms

If all steps work, your system is successfully:

* Creating products
* Storing inventory
* Creating orders
* Allocating stock
* Updating inventory
* Logging events

---

# Upcoming changes

* Replace CSV with DB
* Concurrency handling
* Upgraded allocation logic
* Making code production-ready
* Addition of Redis for locking
---
