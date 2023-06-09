from Bank import Bank

def main():
    bank = Bank()
    user1 = bank.create_account("Arif", 1000)
    user2 = bank.create_account("Reza", 500)


# ================================== Checking the total balance of Bank and Users ==================================
    print("================================== Checking the total balance of Bank and Users ==================================\n")
    print("The Total balance of bank: ", bank.get_total_balance())  
    print(f"{user1.name} balance: ",user1.check_balance())
    print(f"{user2.name} balance: ",user2.check_balance())  
    

# ======================== Checking the total balance of Users after deposit and withdrawing ========================
    print("\n======================== Checking the total balance of Users after deposit and withdrawing ========================\n")
    user1.deposit(500)
    print(f"The Total balance of bank after {user1.name} deposit 500: ",bank.get_total_balance())  
    user2.withdraw(200)
    print(f"{user2.name} balance After withdraw 200: ",user2.check_balance())  
    user2.withdraw(2000)



# ======================== Checking the total balance of Users balance after Transfer, taking loan and deposit ========================
    print("\n==================== Checking the total balance of Users balance after Transfer, taking loan and deposit ====================\n")
    user1.transfer(user2, 300)
    print(f"{user1.name} balance after tranfer 300: ",user1.check_balance())
    user1.take_loan(bank)
    print(f"{user1.name} take loan: ", user1.loanAamount())
    user1.deposit(500)
    print(f"{user1.name} balance after deposit 500: ",user1.check_balance())
    print(f"{user2.name} balance: ",user2.check_balance())  
    user1.withdraw(1700)
    print(f"{user1.name} balance: ",user1.check_balance())  

# ========================== Checking the total balance of Bank and Loan amount ===========================
    print("\n========================== Checking the total balance of Bank and Loan amount ===========================\n")
    print("The Total balance of bank: ", bank.get_total_balance()) 
    print(f"Total loan given: ",bank.get_total_loan_amount())  

# ==================================== Checking the transaction history ====================================
    user1.view_transaction_history()  
    user2.view_transaction_history()  

# ============================= Main Function =============================
if __name__ == "__main__":
    main()
