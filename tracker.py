import csv
from datetime import datetime

FILE_PATH = "data/expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Bills): ")

    # Save to CSV
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])
    print("Expense added successfully!")

def view_expenses():
    print("\nExpenses:")
    with open(FILE_PATH, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
