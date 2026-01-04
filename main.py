import datetime

def main_menu():
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Habit Tracker")
    print("5. Save & Exit")


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


def expense_analysis():
    try:
        with open("expenses.csv","r") as file:
            expenses = file.readlines()
            
        all_costs = []
        category_totals = {}

        for exp in expenses:
            date, category, name, cost = exp.strip().split(",")
            cost = int(cost)
            all_costs.append(cost) 


            if category in category_totals:
                category_totals[category] += cost
            else:
                category_totals[category] = cost
        
        
        total = sum(all_costs)
        average = total / len(all_costs)

        print("\n1. Total expense")
        print("2. Category wise spending")
        print("3. highest spending")
        print("4. Average spending")
        
        choice = int(input("Choose 1 to 4: "))

        if choice == 1:
            
            print(f"Total spent: ₹{total}")
            

        elif choice == 2:
            for cat, amt in category_totals.items():
                print(f"{cat} : ₹{amt}")
            
            
        elif choice == 3:
            highest_category = max(category_totals, key=category_totals.get)
            highest_amount = category_totals[highest_category]

            print(f"Highest spending category: {highest_category} (₹{highest_amount})")


        elif choice == 4:
            
            print(f"Average spending per expense: ₹{average:.2f}")
            

    except FileNotFoundError:
        print("No expenses file found")



def habit_tracker():
    print("habit tracker selected")


def save_and_exit():
    print("Data saved successfully")
    exit()



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
