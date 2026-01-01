import csv

FILE = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Note (optional): ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            print("\nDate | Category | Amount | Note")
            print("-" * 35)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No expenses found.")

def total_expense():
    total = 0
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print("Total Expense:", total)
    except FileNotFoundError:
        print("No expenses found.")

def category_summary():
    summary = {}
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                summary[category] = summary.get(category, 0) + amount

        print("\nCategory-wise Summary")
        for k, v in summary.items():
            print(k, ":", v)
    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Exiting... ")
        break
    else:
        print("Invalid choice!")
