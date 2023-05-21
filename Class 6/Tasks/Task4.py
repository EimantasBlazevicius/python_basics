# 4.
# Create a class called "BankAccount" with attributes for account number and balance.
# Add methods to the BankAccount class for depositing and withdrawing money.
# Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
# Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.

class BankAccount:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print('Not enough Money')


class SavingsAccount(BankAccount):
    def __init__(self, acc_number, balance, interest_rate):
        super().__init__(acc_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        fee = 0.5
        if self.balance >= amount+fee:
            self.balance = self.balance - (amount+fee)
        else:
            print('Not enough Money')


acc = SavingsAccount("123456789", 99, 6)
acc.deposit(99)
acc.withdraw(2)
print(acc.balance)
