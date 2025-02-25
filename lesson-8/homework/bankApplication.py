import os
import json

# Account class (Individual Account Details)
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

# Bank class (Manages multiple accounts)
class Bank:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1001)  # Generate a unique account number
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: ${account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    data = json.load(f)
                    self.accounts = {acc_num: Account(**acc_data) for acc_num, acc_data in data.items()}
                except json.JSONDecodeError:
                    print("Error reading file. Starting fresh.")

# Command-line Interface
if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        if choice == "2":
            account_number = input("Enter account number: ")
            bank.view_account(account_number)
        if choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, input("Enter amount to deposit: "))
        if choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
        if choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
