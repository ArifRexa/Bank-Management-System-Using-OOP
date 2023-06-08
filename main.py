from Bank import Bank

def main():
    bank = Bank()
    user1 = bank.create_account("John", 1000)
    user2 = bank.create_account("Alice", 500)

    user1.deposit(500)
    user2.withdraw(200)
    user1.transfer(user2, 300)
    user1.take_loan(bank)

    print(user1.check_balance())
    print(user2.check_balance())  

    print(bank.get_total_balance())  
    print(bank.get_total_loan_amount())  

    user1.view_transaction_history()  
    user2.view_transaction_history()  


if __name__ == "__main__":
    main()
