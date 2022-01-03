class Account:
    def __init__(self, opening_balance):
        self.opening_balance = opening_balance


 checking = Account(10)
savings = Account(99)

print(checking.opening_balance)
print(savings.opening_balance)
