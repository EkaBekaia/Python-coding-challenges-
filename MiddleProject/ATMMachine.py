import json
import random
import os

# Constants
file_name = 'accounts.json'
transaction_file = 'transactions.json'
nominals = [200, 100, 50, 20, 10, 5]

# Load or Generate Accounts and History
def load_accounts():
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            return json.load(f)
    return {}

def load_history():
    if os.path.exists(transaction_file):
        with open(transaction_file, 'r') as f:
            return json.load(f)
    return {}

def save_accounts(accounts):
    with open(file_name, 'w') as f:
        json.dump(accounts, f)

def save_history(history):
    with open(transaction_file, 'w') as f:
        json.dump(history, f)

# Generate Random Users
def generate_random_users():
    users = {}
    for i in range(1, 51):
        username = f'user{i:03d}'
        pin_code = random.randint(1000, 9999)
        balance = random.randint(0, 10000)
        users[username] = {'pin': pin_code, 'balance': balance}
    return users

# Generate Random History for Transactions
def generate_random_history(users):
    history = {}
    for user in users:
        history[user] = []
        for _ in range(random.randint(1, 5)):  # random 1-5 transactions per user
            transaction_type = random.choice(['deposit', 'withdraw'])
            amount = random.randint(1, 1000)
            history[user].append({'type': transaction_type, 'amount': amount})
    return history

# Functions for account interactions
def check_balance(account):
    print(f"Your current balance is: {account['balance']}₾")

def deposit(account, username, history):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        account['balance'] += amount
        history[username].append({'type': 'deposit', 'amount': amount})
        print(f"Deposited {amount}₾. New balance: {account['balance']}₾")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def withdraw(account, username, history):
    try:
        amount = int(input("Enter amount to withdraw: "))
        
        # Check if the amount is zero
        if amount == 0:
            print("You cannot withdraw zero amount. Please enter a valid amount.")
            return

        # Check if the amount is greater than the current balance
        if amount > account['balance']:
            print(f"Insufficient balance. Your current balance is {account['balance']}₾.")
            return

        # Check if the amount can be broken down into available nominals
        remaining_amount = amount
        bill_breakdown = {}

        for nominal in nominals:
            bill_count = remaining_amount // nominal
            if bill_count > 0:
                bill_breakdown[nominal] = bill_count
            remaining_amount -= bill_count * nominal

        # If remaining_amount is not zero, the amount cannot be withdrawn with the available nominals
        if remaining_amount != 0:
            print(f"Cannot withdraw {amount}₾ with available nominals (5, 10, 20, 50, 100, 200).")
            return

        # Deduct the amount from the account and log the transaction
        account['balance'] -= amount
        history[username].append({'type': 'withdraw', 'amount': amount})
        print(f"Withdrawn {amount}₾. New balance: {account['balance']}₾")

    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_transaction_history(username, history):
    if username in history:
        print(f"Transaction history for {username}:")
        for transaction in history[username]:
            print(f"{transaction['type']} of {transaction['amount']}₾")
    else:
        print("No transaction history found.")

def create_account(accounts):
    username = input("Enter a new username: ")
    if username in accounts:
        print("Username already exists.")
        return
    pin_code = int(input("Enter a 4-digit PIN code: "))
    accounts[username] = {'pin': pin_code, 'balance': 0}
    print(f"Account created for {username}.")

def login(accounts):
    username = input("Enter your username: ")
    if username not in accounts:
        print("Username not found.")
        return None
    pin_code = int(input("Enter your PIN: "))
    if accounts[username]['pin'] == pin_code:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Incorrect PIN.")
        return None

def delete_account(accounts, username, history):
    confirm = input(f"Are you sure you want to delete the account {username}? (yes/no): ")
    if confirm.lower() == "yes":
        del accounts[username]
        del history[username]
        print(f"Account {username} deleted.")
    else:
        print("Account deletion canceled.")

# Main program logic

if __name__ == '__main__':
    accounts = load_accounts()
    history = load_history()

    # If no data is available, generate some random users and transactions
    if not accounts:
        accounts = generate_random_users()
        history = generate_random_history(accounts)
        save_accounts(accounts)
        save_history(history)

    print("Welcome to TBC Bank!")
    
    # Example Workflow:
    
    # 1. Create a new account (if necessary)
    create_account(accounts)  

    # 2. Login the user
    username = login(accounts)

    if username:
        while True:
            print("\n1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Delete Account")
            print("6. Exit")
            
            choice = input("Choose an option: ")

            if choice == "1":
                check_balance(accounts[username])
            elif choice == "2":
                deposit(accounts[username], username, history)
                save_accounts(accounts)
                save_history(history)
            elif choice == "3":
                withdraw(accounts[username], username, history)
                save_accounts(accounts)
                save_history(history)
            elif choice == "4":
                view_transaction_history(username, history)
            elif choice == "5":
                delete_account(accounts, username, history)
                save_accounts(accounts)
                save_history(history)
                break
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
    else:
        print("Failed to log in.")
