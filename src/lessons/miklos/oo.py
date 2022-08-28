class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        return self.balance

    def pay_in(self):
        pass

    def withdraw(self):
        pass


checking_account = Account(77826.12)
savings_account = Account(341.67)

checking = checking_account.show_balance()
savings = savings_account.show_balance()
print(checking)
print(savings)
