import json
from pathlib import Path
from typing import List, Dict
from app.models.expense import Expense

DATA_FILE = Path("data/expenses.json")

class JSONRepository:

    def __init__(self):
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        if not DATA_FILE.exists():
            with open(DATA_FILE, "w") as f:
                json.dump({"expenses": [], "goals": {}}, f, indent=4)

    
    def load_data(self) -> Dict:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
        
    def save_data(self, data: Dict):
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_expense(self, expense: Expense):
        data = self.load_data()
        data["expenses"].append(expense.__dict__)
        self.save_data(data)

    def get_all_expenses(self) -> List[Expense]:
        data = self.load_data()
        return [Expense(**item) for item in data["expenses"]]
    
    def set_goal(self, category: str, amount: float):
        data = self.load_data()
        data["goals"][category] = amount
        self.save_data(data)

    def get_goals(self):
        data = self.load_data()
        return data["goals"]

