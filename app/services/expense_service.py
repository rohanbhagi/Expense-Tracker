from typing import List, Dict, Optional
from app.models.expense import Expense
from app.repositories.json_repository import JSONRepository

class ExpenseService:
    def __init__(self, repository: Optional[JSONRepository] = None):
        self.repo = repository if repository else JSONRepository()
    
    # ---------------------------
    # Expense Management
    # ---------------------------

    def add_expense(self, amount: float, category: str, description: str = "") -> Expense:
        expense =  Expense(amount=amount, category=category, description=description)
        self.repo.add_expense(expense=expense)
        return expense
    
    def get_expenses(self) -> List[Expense]:
        return self.repo.get_all_expenses()
    
    def get_expense_by_category(self, category: str) -> List[Expense]:
        all_expense = self.repo.get_all_expenses()
        return [expense for expense in all_expense if expense.category.lower() == category.lower()]
    
    def get_total_spent(self, category: Optional[str] = None):
        all_expense = self.get_expenses()
        if category:
            expenses = [expense for expense in all_expense if expense.category.lower() == category.lower()]
        
        return sum(e.amount for e in expenses)
    
    # ---------------------------
    # Goals
    # ---------------------------

    def set_goal(self, category: str, amount: float):
        self.repo.set_goal(category=category, amount=amount)

    def get_goals(self) -> Dict[str, float]:
        return self.repo.get_goals()
    
    def get_goal_status(self, category: str) -> Optional[Dict]:
        goals = self.get_goals()
        if category not in goals: 
            return None
        
        limit = goals[category]
        spent = self.get_total_spent(category=category)
        remaining = limit - spent

        return {
            "category": category,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "is_over": remaining < 0
        }
    






    


        
