def expense_tracker():
    expenses = {}
    while True:
        category = input("Enter expense category (type 'quit' to exit): ").lower()
        if category == "quit":
            break
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
    print("Expenses:")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

expense_tracker()

        

