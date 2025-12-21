def main_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Habit Tracker")
    print("5. Save & Exit")


def new_expense():
    name = input("What is new expense: ")
    cost = input("What was the cost: ")
    print(f"Expense: {name}, Cost: {cost}")


def view_expense():
    print("view_expense_selected")


def expense_analysis():
    print("expense_analysis_selected")


def habit_tracker():
    print("habit tracker selected")


def save_and_exit():
    print("data is saved successfully")
    exit()


# MAIN PROGRAM LOOP
while True:
    main_menu()
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
        print("Invalid choice. Try again.")
