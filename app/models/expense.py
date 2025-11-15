from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Expense:
    amount: float
    category: str
    description: Optional[str] = ""
    date: str = datetime.now().strftime("%Y-%m-%d")
