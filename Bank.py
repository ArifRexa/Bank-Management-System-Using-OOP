from Account import Account
class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, initial_deposit):
        account = Account(name, initial_deposit)
        self.accounts.append(account)
        self.total_balance += initial_deposit
        return account

    def get_account_by_name(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount
