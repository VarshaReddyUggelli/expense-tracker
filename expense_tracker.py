import json
import os
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    category = input("Category (food/transport/shopping/other): ")
    description = input("Description: ")
    amount = float(input("Amount (₹): "))
    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Added ₹{amount} for {description}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    print(f"\n{'Date':<12} {'Category':<12} {'Description':<20} {'Amount'}")
    print("-" * 55)
    total = 0
    for e in expenses:
        print(f"{e['date']:<12} {e['category']:<12} {e['description']:<20} ₹{e['amount']}")
        total += e['amount']
    print("-" * 55)
    print(f"{'Total':<44} ₹{total}")

def summary_by_category(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    print("\n=== Spending by Category ===")
    for cat, amt in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<15} ₹{amt}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Summary by category")
        print("4. Exit")
        choice = input("\nChoose (1-4): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

main()