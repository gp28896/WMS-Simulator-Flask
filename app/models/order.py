from dataclasses import dataclasses
from datetime import datetime

@dataclass:
class Order:
	order_id: str
	status: str
	timestamp: str = datetime.utcnow().isformat()