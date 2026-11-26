import json
import datetime
import csv
import pathlib
import sys

expenses = []

def add_expenses():
    name = input("Enter your name: ")

    try:
        amount = float(input("Enter the amount you spend: "))
    except ValueError:
        print("Amount should be a number.")
        return

    today = datetime.datetime.today()
    clean_time = today.strftime("%d-%m-%y %I-%M-%S %p")
    expense = {
        "Name" : name,
        "Date" : clean_time,
        "expense" : amount
    }
    expenses.append(expense)

    # Fixed: Standardized to lowercase "tracker" to match loading function
    with open("expense_tracker.txt", "a") as file:
        file.write(f"{name},{clean_time},{amount}\n")

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expense record available.")
        return
    for expense in expenses:
        print(f"Name: {expense['Name']} | Date: {expense['Date']} | Expense: {expense['Expense']}")


def load_Expenses():
    try:
        with open("expense_tracker.txt", "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue  # Skip blank lines safely
                
                # Split elements by a comma
                parts = cleaned_line.split(",")
                
                # Check if the line actually has exactly 3 sections (Name, Date, Amount)
                if len(parts) == 3:
                    name, date, amount = parts
                    try:
                        expense = {
                            "name" : name.strip(),
                            "date" : date.strip(),
                            "expense": float(amount.strip())
                        }
                        expenses.append(expense)
                    except ValueError:
                        print(f"Skipping line with invalid amount number: {cleaned_line}")
                else:
                    print(f"Skipping badly formatted line (missing commas): {cleaned_line}")

    except FileNotFoundError:
        pass


# Load previous records right when the program starts
load_Expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expense")
    print("3. Exit")

    options = input("Enter your option: ")

    if options == "1":
        add_expenses()
    elif options == "2":
        show_expenses()
    elif options == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Option.")
