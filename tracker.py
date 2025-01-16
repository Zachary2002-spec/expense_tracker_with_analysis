import csv
import os
from datetime import datetime

FILE_PATH = "data/expenses.csv"

# Ensure the file and directory exist
def ensure_file_exists():
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    # Create the file if it doesn't exist and add headers
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Amount", "Category"])  # Add headers
        print(f"File created at {FILE_PATH}")

def add_expense():
    ensure_file_exists()  # Ensure file exists before adding expenses

    # Input details
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    description = input("Enter description: ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    category = input("Enter category (e.g., Food, Bills): ").strip()

    # Save to CSV
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])
    print("Expense added successfully!")

def view_expenses():
    ensure_file_exists()  # Ensure file exists before viewing expenses

    print("\nExpenses:")
    try:
        with open(FILE_PATH, mode="r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header
            print(f"{'Date':<12} {'Description':<20} {'Amount':<10} {'Category':<15}")
            print("-" * 60)
            for row in reader:
                print(f"{row[0]:<12} {row[1]:<20} {row[2]:<10} {row[3]:<15}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
