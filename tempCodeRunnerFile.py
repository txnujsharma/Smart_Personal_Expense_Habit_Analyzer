def main_menu():
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Expense Analysis\n4. Habit Tracker\n5. Save & Exit\n")
        choice = int(input("choose from 1 to 5: "))

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
            break
        else:
            print("invalid choice")



def new_expense():
     new_expense_name = input("What is new expense: ")
     new_expense_cost = input("What was the cost: ")
     print(f"Expense: {new_expense_name}, Cost: {new_expense_cost}")

def view_expense():
     print("view_expense_selected")

def expense_analysis():
     print("expense_analysis_selected")

def habit_tracker():
     print("habit tracker selected")

def save_and_exit():
     print("data is saved successfully")

main_menu()