class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add amount to the balance
        self.account_balance += amount

    def withdraw(self, amount):
        # Check if there is enough money to withdraw
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Print the current balance in a user-friendly way
        print(f"Current Balance: ${self.account_balance}")
