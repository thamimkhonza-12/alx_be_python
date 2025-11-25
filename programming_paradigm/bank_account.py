class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Format using format() instead of f"{value:.2f}"
        balance_str = "${}".format(format(self.account_balance, ".2f"))
        print("Current Balance: " + balance_str)
