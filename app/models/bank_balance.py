from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bank_Balance:
    total_balance: float
    last_updated: str = datetime.now().strftime("%Y-%m-%d")
