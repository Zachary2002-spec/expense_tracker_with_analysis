from tracker import add_expense, view_expenses
from analysis import analyze_expenses

def main():
    print("Welcome to Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
