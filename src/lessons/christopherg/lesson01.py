class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        return self.name, self.balance

    def __str__(self):
        return f"{self.name} has {self.balance}"


checking = Account("Andy", 25)
savings = Account("Sue", 9999999)

print(checking.show_balance())
print(savings.show_balance())

print(checking)
