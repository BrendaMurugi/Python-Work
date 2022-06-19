from datetime import datetime

class Account:
    def __init__(self,account_name,account_number):
        self.balance = 0
        self.transaction = 100
        self.deposits = []
        self.withdrawals = []
        self.account_name = account_name
        self.account_number = account_number
        self.combined_statements = []
        self.loan_balance = 0

    def deposit(self,amount):
        self.date = datetime.now().strftime("%c")
        empty_dict = {"Date": self.date,"Amount": amount,"Narration": "Deposit"}
        if amount <= 0:
            return f"Deposit amount must be greater than 0."
        else:
            self.balance += amount
            self.deposits.append(amount)
            self.combined_statements.append(empty_dict)
            # print(self.deposits)
            print(empty_dict)
        # return f"Hello {self.account_name}, you have deposited Ksh.{amount} and your new balance is {self.balance}."

    def withdraw(self,amount):
        self.date = datetime.now().strftime("%c")
        empty_dict = {"Date": self.date,"Amount": amount,"Narration": "Withdraw"}
        if amount <= 0:
            return f"Requested amount must be greater than 0."
        elif amount > self.balance - self.transaction:
            return f"Insufficient funds."
        else:
            self.balance -= amount + self.transaction
            self.withdrawals.append(amount)
            self.combined_statements.append(empty_dict)
            # print(self.withdrawals)
            print(empty_dict)
        # return f"Hello {self.account_name}, you have withdrawn Ksh.{amount} and your new balance is {self.balance}."

    def deposits_statement(self):
        for deposit in self.deposits:
            print(f"You deposited Ksh: {deposit}")

    def withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(f"You withdrew Ksh: {withdrawal}")

    def current_balance(self):
        balance = self.balance
        print(f"Current balance: {balance}")

    def full_statement(self):
        for x in self.combined_statements:
            time = x["Date"]
            narration = x["Narration"]
            amount = x["Amount"]
            print(f"{time}........{narration}........{amount}")

    def borrow(self,amount):
        num_deposits = len(self.deposits)
        sum_deposits = sum(self.deposits)
        requested = (sum_deposits) * 1/3
        amount += (amount) * 0.03
        
        if num_deposits < 1:
            print(f"You need to deposit at least 10 times into your account.")
        elif amount <= 100:
            print(f"Loan amount requested must be more than 100.")
        elif amount >= requested:
            print(f"You are not eligible for a loan higher than {sum_deposits//3}")
        elif self.loan_balance > 0:
            print(f"Loan request denied. You have an outstanding loan of {self.loan_balance}")
        else:
            self.loan_balance += amount
            return f"Loan request accepted. Your outstanding loan balance is {self.loan_balance}"

    def loan_repayment(self,amount):
        if amount < self.loan_balance:
            self.loan_balance -= amount
            return f"You have paid {amount} and your outstanding loan balance is {self.loan_balance}."
        elif amount == self.loan_balance:
            return f"Loan successfully settled."
        else:
            self.loan_balance -= amount
            overpayment = amount - self.loan_balance
            self.balance += overpayment
            return f"Loan successfully settled and current account balance is {self.balance}."

    def transfer(self,amount,account):
        if amount > self.balance:
            return f"Account balance is too low. Cannot transfer amount."
        elif amount <= 0:
            return f"Enter correct amount."
        else:
            self.balance -= amount
            account.balance += amount
            return f"You have sent {amount} to {account.account_name} and your balance is {self.balance}."
