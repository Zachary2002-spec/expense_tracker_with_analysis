import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "data/expenses.csv"

def analyze_expenses():
    # Check if the file exists
    if not os.path.exists(FILE_PATH):
        print("No expense file found. Please add some expenses first.")
        return

    # Load data with proper handling for the header
    try:
        df = pd.read_csv(FILE_PATH)
    except pd.errors.EmptyDataError:
        print("The expenses file is empty. Please add some expenses first.")
        return

    # Ensure the DataFrame is not empty
    if df.empty:
        print("No data available to analyze.")
        return

    # Convert 'Amount' column to numeric and drop invalid rows
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df.dropna(subset=["Amount"], inplace=True)

    # Convert 'Date' column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Total spending by category
    category_summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    print("\nSpending by Category:")
    print(category_summary)

    # Spending over time
    time_summary = df.groupby("Date")["Amount"].sum()

    # Visualization - Category
    plt.figure(figsize=(10, 6))
    category_summary.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Spending by Category", fontsize=16)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Amount Spent", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Visualization - Time
    plt.figure(figsize=(10, 6))
    time_summary.plot(kind="line", marker="o", color="orange")
    plt.title("Spending Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Total Amount Spent", fontsize=12)
    plt.grid(axis="both", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()
