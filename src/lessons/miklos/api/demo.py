class Account:
    def __init__(self, opening_balance):
        self.balance = opening_balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class CheckingAccount(Account):
    def withdraw(self, different):
        pass

    def atm(self):
        pass


class SavingsAccount(Account):
    def high_iterest(self):
        pass


account1 = CheckingAccount(100)
account2 = CheckingAccount(50)

print(account1.balance)
print(account2.balance)

account1.deposit(9000)
print(account1.balance)
