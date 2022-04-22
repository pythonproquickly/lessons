class Account:
    def __init__(self, balance):
        self.balance = balance

    def calculate_balance(self):
        # pretend I do a calc
        return 132.09

    def payin(self, amount):
        self.balance += amount
        return self.balance


# instantiation
andy = Account(785.09)
value = andy.calculate_balance()
print(andy.balance)

fred = Account(999.78)
fred.payin(10000)
print(fred.balance)
