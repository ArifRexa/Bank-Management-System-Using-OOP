class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.loan_amount = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        return self.balance

    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred {amount} to {recipient_account.name}")
            recipient_account.transaction_history.append(f"Received {amount} from {self.name}")
        else:
            print("Insufficient balance.")

    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            if self.loan_amount == 0:
                loan_amount = self.balance * 2
                self.loan_amount += loan_amount
                bank.total_loan_amount += loan_amount
                self.transaction_history.append(f"Loan taken: {loan_amount}")
            else:
                print("You have already taken a loan.")
        else:
            print("Loan feature is currently disabled.")

    def view_transaction_history(self):
        print(*self.transaction_history, sep="\n")

