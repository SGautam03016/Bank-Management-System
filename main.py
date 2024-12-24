class account:
    def __init__(self, acc_no, name, balance=0):
        self.Account_number = acc_no
        self.Name = name
        self.Balance = balance

    def credit(self, amount):    
        if amount > 0:
            self.Balance += amount
            print("Deposit Successful..!! ")
            print("After deposit, New Balance = ", self.Balance)
            print("---THANK YOU---")
        else:
            print("Deposit Amount Must be positive.")

    def debit(self, amount):    
        if amount > 0 and amount <= self.Balance:
            self.Balance -= amount
            print("Withdrawal Successful..!!")
            print("After Withdrawal, Balance = ", self.Balance)
            print("---THANK YOU---")
        elif amount > self.Balance:
            print("Insufficient Balance..")
        else:
            print("Withdrawal Amount must be positive...")

    def display_account_details(self):
        print("\n---ACCOUNT DETAILS---")
        print("Account Number: ", self.Account_number)
        print("Account Holder Name: ", self.Name)
        print("Account Balance: ", self.Balance)


class Bank:
    def __init__(self):                                                 
        self.account = {}  # Dictionary to store account objects by account number

    def create_account(self, acc_no, name, initial_credit):
        if acc_no in self.account:
            print("Account number already exists..!")
        else:
            self.account[acc_no] = account(acc_no, name, initial_credit) # Create account object and add to dictionary
            print("Account created successfully..!!")

    def find_account(self, acc_no):
        return self.account.get(acc_no, None)  # Changed from self.accounts to self.account
        # Returns: account object if found, None if account doesn't exist

    def credit_to_account(self, acc_no, amount):
        account = self.find_account(acc_no)
        if account:
            account.credit(amount)
        else:
            print("Account not found..!!")

    def debit_from_account(self, acc_no, amount):
        account = self.find_account(acc_no)
        if account:
            account.debit(amount)
        else:
            print("Account not found..!!")

    def display_account_details(self, acc_no):
        account = self.find_account(acc_no)
        if account:
            account.display_account_details()  # Corrected method call to display account details
        else:
            print("Account not found..!!")


def main():
    bank = Bank()
    while True:
        print("\n---Welcome to Bank Management System---")
        print("1. Create a bank account")
        print("2. Credit money")
        print("3. Debit money")
        print("4. View account details")
        print("5. Exit")

        choice = int(input("Enter your choice (1 to 5): "))

        if choice == 1:
            acc_no = int(input("Enter 11-digit Account number: "))
            name = input("Enter your name: ")
            starting_credit = float(input("Enter initial deposit: "))  # Changed to directly take float input
            bank.create_account(acc_no, name, starting_credit)

        elif choice == 2:
            acc_no = int(input("Enter 11-digit Account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.credit_to_account(acc_no, amount)

        elif choice == 3:
            acc_no = int(input("Enter 11-digit Account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.debit_from_account(acc_no, amount)

        elif choice == 4:
            acc_no = int(input("Enter 11-digit Account number: "))
            bank.display_account_details(acc_no)

        elif choice == 5:
            print("Exiting the system..")
            print("Goodbye... Visit again!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # this function used to call  the main function.
