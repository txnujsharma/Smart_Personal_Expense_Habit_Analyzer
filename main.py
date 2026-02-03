import datetime

def main_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Habit Tracker")
    print("4. Save & Exit")


def new_expense():
    date = datetime.date.today()
    name = input("What is new expense: ")
    cost = int(input("What was the cost: "))
    category = input("What was the category: ")

    with open("expenses.csv", "a") as file:
        file.write(f"{date},{category},{name},{cost}\n")

    print("Expense saved successfully")


def view_expense():
    try:
        with open("expenses.csv", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found")
            return

        print("\n--- Your Expenses ---")
        for exp in expenses:
            date, category, name, cost = exp.strip().split(",")
            print(f"{date} | {category} | {name} | ₹{cost}")

    except FileNotFoundError:
        print("No expenses file found")


def habit_tracker():
    print("Habit tracker coming soon")


def save_and_exit():
    print("Data saved successfully")
    exit()


# MAIN LOOP
while True:
    main_menu()

    try:
        choice = int(input("Choose from 1 to 4: "))

        if choice == 1:
            new_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            habit_tracker()
        elif choice == 4:
            save_and_exit()
        else:
            print("Invalid choice. Enter 1 to 4.")

    except ValueError:
        print("Please enter a NUMBER only.")
