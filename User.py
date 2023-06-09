class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.__balance = initial_balance
        self.__loan_amount = 0
        self.bank = None
        self.__transaction_history = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transaction_history.append(f"Deposited {amount}")
        self.bank.update_total_balance(amount)

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew {amount}")
            self.bank.withdraw_total_balance(amount)
        elif self.__balance == amount:
            print("The bank is bankrupt")
        else:
            print("Insufficient balance. You can't withdraw more than your current balance.")

    def check_balance(self):
        return self.__balance

    def transfer(self, recipient_account, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            recipient_account.__balance += amount
            self.__transaction_history.append(f"Transferred {amount} to {recipient_account.name}")
            recipient_account.__transaction_history.append(f"Received {amount} from {self.name}")
        else:
            print("Insufficient balance. You can't transfer more than your current balance.")

    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            if self.__loan_amount == 0:
                loan_amount = self.__balance * 2
                self.__loan_amount += loan_amount
                bank.total_loan_amount += loan_amount
                self.__transaction_history.append(f"Loan taken: {loan_amount}")
            else:
                print("You have already taken a loan.")
        else:
            print("Loan feature is currently disabled.")

    def loanAamount(self):
        return self.__loan_amount

    def view_transaction_history(self):
        print("\n=================== Transection History ===================\n")
        print(f"Transection History of {self.name}")
        print(*self.__transaction_history, sep="\n")

