class MenuItem:
    """A MenuItem object represents a menu item to be offered for sale at the
    lemonade stand."""

    def __init__(self, name, wholesale_cost, selling_price):
        self.name = name
        self.wholesale_cost = wholesale_cost
        self.selling_price = selling_price


class SalesForDay:
    """A SalesForDay object represents the sales for a particular day."""

    def __int__(self, sales):
        self.sales = sales

    def calculate_profit(self, calculate_days=-1):
        if calculate_days == -1:
            profit = 0
            for day, products in self.sales:
                profit += products['name']
        return self.sales[day]


class LemonadeStand:
    def __int__(self, stand_name):
        self.stand_name = stand_name
        self.menu = {}
        self.daily_sales = []

    def add_to_menu(self, menu_item):
        self.menu[menu_item.name] = (
            menu_item.wholesale_cost, menu_item.selling_price)
