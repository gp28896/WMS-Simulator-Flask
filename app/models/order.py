from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
	order_id: str
	status: str
	timestamp: str = datetime.utcnow().isformat()