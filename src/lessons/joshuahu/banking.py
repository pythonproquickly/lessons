class Account:
    """this represents a customers account for holding money in a bank"""
    def __init__(self, opening_balance):
        self.balance = opening_balance
        self.amounts = []

    def calculate_balance(self):
        return self.balance

    def pay_in(self, amount):
        self.balance += amount
        self.amounts.append(['in', amount])

    def withdraw(self, amount):
        self.balance -= amount
        self.amounts.append(['out', -amount])

    def get_transaction_history(self):
        return self.amounts


class CheckingAccount(Account):
    pass

class SavingsAccount(Account):
    def withdraw(self, amount):
        pass

    def xyz(self):
        pass





def bank_demo():
    checking = Account(345.12)
    checking.pay_in(2000)
    checking.pay_in(3000)
    checking.withdraw(4000)
    checking_balance = checking.calculate_balance()
    print(checking_balance)
    print(checking.get_transaction_history())

    savings = Account(1_009.32)
    savings_balance = savings.calculate_balance()
    print(savings_balance)

if __name__ == "__main__":
    bank_demo()

