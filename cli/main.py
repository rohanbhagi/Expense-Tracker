import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.services.expense_service import ExpenseService

service = ExpenseService()


def show_menu():
    print("\n==== Expense Tracker ====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. View expenses by category")
    print("5. Set spending goal")
    print("6. Check goal status")
    print("7. Exit")


def add_expense_cli():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        description = input("Description (optional): ").strip()

        expense = service.add_expense(amount, category, description)
        print(f"Added: {expense}")

    except ValueError:
        print("Invalid amount. Try again.")


def view_all_expenses_cli():
    expenses = service.get_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    for e in expenses:
        print(f"{e.date} - {e.category}: {e.amount} ({e.description})")


def view_total_spent_cli():
    category = input("Category (leave blank for all): ").strip()
    category = category if category else None

    total = service.get_total_spent(category)
    print(f"Total spent: {total}")


def view_expenses_by_category_cli():
    category = input("Enter category: ").strip()
    expenses = service.get_expense_by_category(category)

    if not expenses:
        print("No expenses in this category.")
        return

    for e in expenses:
        print(f"{e.date} - {e.category}: {e.amount} ({e.description})")


def set_goal_cli():
    category = input("Enter category: ").strip()
    try:
        limit = float(input("Enter goal limit: "))
        service.set_goal(category, limit)
        print("Goal set.")
    except ValueError:
        print("Invalid number. Try again.")


def check_goal_status_cli():
    category = input("Enter category: ").strip()
    status = service.get_goal_status(category)

    if not status:
        print("No goal found for this category.")
        return

    print(f"\nGoal Status for '{category}'")
    print(f"Limit: {status['limit']}")
    print(f"Spent: {status['spent']}")
    print(f"Remaining: {status['remaining']}")
    if status['is_over']:
        print("⚠️ You have exceeded your goal!")
    else:
        print("✔ You are within your goal.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense_cli()
        elif choice == "2":
            view_all_expenses_cli()
        elif choice == "3":
            view_total_spent_cli()
        elif choice == "4":
            view_expenses_by_category_cli()
        elif choice == "5":
            set_goal_cli()
        elif choice == "6":
            check_goal_status_cli()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()