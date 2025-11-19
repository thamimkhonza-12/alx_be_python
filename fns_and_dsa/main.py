from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()


    def display_menu():
        print("\n=== Shopping List Manager ===")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View shopping list")
        print("4. Exit")


    def add_item(shopping_list):
        item = input("Enter the item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")


    def remove_item(shopping_list):
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' is not in the shopping list.")


    def view_list(shopping_list):
        if not shopping_list:
            print("The shopping list is currently empty.")
        else:
            print("\nCurrent Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")


    def main():
        shopping_list = []

        while True:
            display_menu()

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                add_item(shopping_list)
            elif choice == "2":
                remove_item(shopping_list)
            elif choice == "3":
                view_list(shopping_list)
            elif choice == "4":
                print("Exiting Shopping List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


    if __name__ == "__main__":
        main()



from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)  # Save future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date


def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


if __name__ == "__main__":
    main()
