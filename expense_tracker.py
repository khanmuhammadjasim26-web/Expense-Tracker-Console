# ==============================================================================
# Project: Console-Based Expense Tracker
# Author: Mohd Jasim Khan
# Description: Personal finance tracking tool implemented using core Python
#              fundamentals (loops, conditionals, lists, and dictionaries).
# ==============================================================================

expenses = []

print("==================================================")
print("           WELCOME TO EXPENSE TRACKER")
print("==================================================")

while True:
    print("\n" + "=" * 22 + " MENU " + "=" * 22)
    print("  1. Add Expense")
    print("  2. View Recorded Expenses")
    print("  3. View Total Spending")
    print("  4. View Expenses by Category")
    print("  5. Exit")
    print("=" * 50)

    choice = input("Enter your choice (1-5): ").strip()

    # Option 1: Add an Expense
    if choice == "1":
        print("\n--- [ Add New Expense ] ---")
        date = input("Enter date (DD-MM-YYYY): ").strip()
        category = input("Enter category (e.g., Food, Travel, Stay, Shopping): ").strip().title()
        description = input("Enter short description: ").strip()
        
        # Numeric amount input with graceful handling
        raw_amount = input("Enter amount (INR): ").strip()
        try:
            amount = float(raw_amount)
        except ValueError:
            print("Invalid amount entered. Defaulting to 0.00.")
            amount = 0.0

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\n>> Expense added successfully!")

    # Option 2: View All Recorded Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("\n>> No expenses recorded yet.")
        else:
            print("\n" + "-" * 70)
            print("                       RECORDED EXPENSES")
            print("-" * 70)
            i = 1
            for expense in expenses:
                print(f"{i:>2}. Date: {expense['date']:<10} | Category: {expense['category']:<12} | "
                      f"Desc: {expense['description']:<18} | Amount: INR {expense['amount']:>8.2f}")
                i += 1
            print("-" * 70)

    # Option 3: View Total Spending
    elif choice == "3":
        total_spending = 0
        for expense in expenses:
            total_spending += expense["amount"]
        print("\n" + "-" * 35)
        print(f"  Total Spending: INR {total_spending:,.2f}")
        print("-" * 35)

    # Option 4: View Expenses Grouped by Category
    elif choice == "4":
        if len(expenses) == 0:
            print("\n>> No expenses recorded yet.")
        else:
            summary = {}
            for expense in expenses:
                cat = expense["category"]
                if cat in summary:
                    summary[cat] += expense["amount"]
                else:
                    summary[cat] = expense["amount"]

            print("\n" + "-" * 40)
            print("          EXPENSES BY CATEGORY")
            print("-" * 40)
            for category, total in summary.items():
                print(f"  * {category:<16} : INR {total:>8.2f}")
            print("-" * 40)

    # Option 5: Graceful Exit
    elif choice == "5":
        print("\n" + "=" * 50)
        print("  Exiting Expense Tracker. Thank you! Goodbye!")
        print("=" * 50)
        break

    else:
        print("\n>> Invalid choice. Please select an option from 1 to 5.")
