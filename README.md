# Expense Tracker with Data Analysis

An intermediate-level Python project that helps users track their expenses, categorize them, and analyze spending habits using visualizations and summaries. This project showcases skills in data manipulation, file handling, and visualization.

---

## Features

- **Add Expenses**: Record daily expenses, including date, description, amount, and category.
- **View Expenses**: Display all recorded expenses in a neat table format.
- **Analyze Spending**: Generate reports for spending summaries and visualize data with charts.
- **Data Storage**: Save expenses in a CSV file for persistence.
- **Visualization**: Create bar charts or pie charts to represent spending patterns.

---

## Requirements

- Python 3.8+
- Libraries:
  - `pandas`
  - `matplotlib`
  - `tabulate`

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Zachary2002-spec/expense-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd expense-tracker
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Linux/Mac
   env\Scripts\activate   # On Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the program:
   ```bash
   python main.py
   ```

---

## Project Structure

```
expense-tracker/
│
├── README.md             # Project documentation
├── main.py               # Entry point for the application
├── tracker.py            # Core functions for expense tracking
├── analysis.py           # Functions for data analysis and visualization
├── requirements.txt      # List of dependencies
├── data/                 # Folder for CSV/SQLite data storage
└── charts/               # Folder for generated charts
```

---

## Examples

### Adding an Expense:

```
Date (YYYY-MM-DD): 2025-01-16
Description: Grocery Shopping
Amount: 55.80
Category: Food
Expense added successfully!
```

### Viewing Expenses:

```
+------------+------------------+--------+----------------+
| Date       | Description      | Amount | Category       |
+------------+------------------+--------+----------------+
| 2025-01-16 | Grocery Shopping | 55.80  | Food           |
| 2025-01-15 | Gas              | 30.00  | Transportation |
+------------+------------------+--------+----------------+
```

### Analysis Summary:

```
Spending by Category:
Food              120.50
Transportation     85.00
Bills             150.00
```

![Sample Chart](charts/sample_chart.png)

---

## Future Enhancements

- Add a budgeting feature to set spending limits.
- Implement a GUI using Tkinter or Flask.
- Export reports as PDFs.
- Add user authentication for personalized expense tracking.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

Inspired by real-life needs to manage personal finances effectively. Built with Python to demonstrate data analysis and visualization skills.
