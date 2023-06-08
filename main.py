from Bank import Bank

def main():
    bank = Bank()
    user1 = bank.create_account("John", 1000)
    user2 = bank.create_account("Alice", 500)

    user1.deposit(500)
    user2.withdraw(200)
    user1.transfer(user2, 300)
    user1.take_loan(bank)

    print(user1.check_balance())  # Output: 1000
    print(user2.check_balance())  # Output: 600

    print(bank.get_total_balance())  # Output: 1700
    print(bank.get_total_loan_amount())  # Output: 1000

    user1.view_transaction_history()  # Output: Deposited 500, Transferred 300 to Alice, Loan taken: 2000
    user2.view_transaction_history()  # Output: Withdrew 200, Received 300 from John


if __name__ == "__main__":
    main()
