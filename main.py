def main_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Habit Tracker")
    print("5. Save & Exit")


def new_expense():
    name = input("What is new expense: ")
    cost = input("What was the cost: ")

    with open("data.txt", "a") as file:
        file.write(f"{name},{cost}\n")

    print("Expense saved successfully")


def view_expense():
    try:
        with open("data.txt", "r") as file:
            data = file.readlines()

        if not data:
            print("No expenses found")
            return

        print("\n--- Your Expenses ---")
        for exp in data:
            name, cost = exp.strip().split(",")
            print(f"{name} : ₹{cost}")

    except FileNotFoundError:
        print("No expenses file found")


def expense_analysis():
    print("expense_analysis_selected")


def habit_tracker():
    print("habit tracker selected")


def save_and_exit():
    print("Data saved successfully")
    exit()


# 🔁 MAIN LOOP (THIS WAS MISSING)
while True:
    main_menu()

    try:
        choice = int(input("Choose from 1 to 5: "))

        if choice == 1:
            new_expense()
        elif choice == 2:
            view_expense()
        elif choice == 3:
            expense_analysis()
        elif choice == 4:
            habit_tracker()
        elif choice == 5:
            save_and_exit()
        else:
            print("Invalid choice. Enter 1 to 5.")

    except ValueError:
        print("Please enter a NUMBER only.")
