class BankAccount:

    all_accounts = []
    def __init__(self, acct, amount, int_rate = 0.0025):
        self.acct = acct
        self.amount = amount
        self.int_rate = int_rate
        self.balance = 0 + amount
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Account: {self.acct}, Balance: ${self.balance}")

    def yield_interest(self):
        self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.all_accounts:
            print(f"Account Information: Your {account.acct} Balance is ${account.balance}, Your Annual Interest Rate is {account.int_rate}")

acct1 = BankAccount("Checking", 15000)
acct2 = BankAccount("Savings", 50000)

acct1.deposit(2500).deposit(5000).deposit(1000).withdraw(2500).yield_interest().display_account_info()
acct2.deposit(2500).deposit(5000).withdraw(1000).withdraw(2500).withdraw(1000).withdraw(2500).yield_interest().display_account_info()

BankAccount.all_account_info()
