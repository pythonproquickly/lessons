class VendingMachine:
    def __init__(self):
        self.products = {}

    def vend(self):
        return "drink"

    def __str__(self):
        result = ""
        for key, value in self.products.items():
            result = result + key + " " + str(value) + " | "
        return result


drinks = VendingMachine()
drinks.products["coffee"] = 2.30
drinks.products["tea"] = 1.30
assert drinks.products["coffee"] == 2.30

print(drinks)
