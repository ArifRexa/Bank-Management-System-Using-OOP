from Account import Account
class Bank:
    def __init__(self):
        self.__accounts = []
        self.__total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, initial_deposit):
        account = Account(name, initial_deposit)
        account.bank = self
        self.__accounts.append(account)
        self.__total_balance += initial_deposit
        return account
    # ====================== for updating bank balance while user deposite ======================
    def update_total_balance(self, amount):
        self.__total_balance += amount

    # ====================== for updating bank balance while user withdrawing ======================
    def withdraw_total_balance(self, amount):
        self.__total_balance -= amount

    def get_total_balance(self):
        return self.__total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount
