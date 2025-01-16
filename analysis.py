import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/expenses.csv"

def analyze_expenses():
    # Load data
    df = pd.read_csv(FILE_PATH, names=["Date", "Description", "Amount", "Category"])

    # Total by category
    summary = df.groupby("Category")["Amount"].sum()
    print("\nSpending by Category:")
    print(summary)

    # Bar chart
    summary.plot(kind="bar", title="Spending by Category")
    plt.ylabel("Amount")
    plt.show()
