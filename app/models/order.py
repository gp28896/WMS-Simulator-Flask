from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Order:
    order_id: str
    status: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())