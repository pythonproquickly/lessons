# Author: Julian MacLeod
# GitHub Username:AzureBarrage
# Date: 4/6/2022
# Description: Keeps track of finances for fictional lemonade stand

class InvalidSalesItemOrderError(Exception):
    """Start by adding exception to error we face in later method"""
    pass


class MenuItem:
    """Creating the menu item object"""

    def __init__(self, name, wholesale_cost, selling_price):
        """initializing our data members"""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """method in order to access private name of the item"""
        return self._name

    def get_wholesale_cost(self):
        """method in order to access private wholesale cost of the item"""
        return self._wholesale_cost

    def get_selling_price(self):
        """method to get the private selling price of the item"""
        return self._selling_price


class SalesForDay:
    """Creating an object to keep track of sales"""

    def __init__(self, day, sales_dict):
        """initializing data members for new object"""
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """making the day accessible"""
        return self._day

    def get_sales_dict(self):
        """Giving us access to the dictionary of sales"""
        return self._sales_dict


class LemonadeStand:
    """Object to represent lemonade stand, keeps track of sales and profits"""

    def __init__(self, name):
        """Initializing data members for new object"""
        self._name = name  # name of our stand
        self._current_day = 0  # The stand must start at 0 days
        self._menu_items = {}  # dictionary to store menu items
        self._list_sales_for_day = []  # list to track sales

    def get_name(self, name):
        """Giving access to private stand name"""
        self._name = name
        return self._name

    def add_menu_item(self, menu_items):
        """method to add items to our menu using the necessary key"""
        menu_items.append_menu_items(self._menu_items)

    def enter_sales_for_today(self, list_sales_for_day):
        """method which tracks day to day sales"""
        for menu_items in list_sales_for_day:
            """for loop to iterate over our sales"""
            list_sales_for_day[menu_items] = 0  # We start with 0 sales
            if menu_items not in self._menu_items:
                """raise and exception for InvalidSalesItemOrderError"""
                raise InvalidSalesItemOrderError
            else:
                """Otherwise, our loop will execute a series of tasks"""
                self._list_sales_for_day = list_sales_for_day
                list_sales_for_day = LemonadeStand(self._current_day)  # Accessing the list of sales and day
                list_sales_for_day.add_menu_item(self._list_sales_for_day)  # add item to menu using appropriate key
                self._current_day = self._current_day + 1  # iterating days

    def get_sales_dict_for_day(self, current_day):
        """method which gives access to our sales dictionary for a specific day"""
        self._current_day = current_day
        return LemonadeStand(self._list_sales_for_day)

    def total_sales_for_menu_item(self, sales_dict):
        """method to track our sales for menu items in dictionary"""
        for self._menu_items in sales_dict:
            """for loop to iterate over the items in our dictionary"""
            self._menu_items = sales_dict.get_sales_dict()
            return sales_dict

    def total_profit_for_menu_item(self, sales_dict):
        """method to calculate profit from an item"""
        for self._list_sales_for_day in sales_dict:
            """for loop to iterate our list of sales which we stored in our dictionary"""
            self._list_sales_for_day = sales_dict.get_sales_dict()
            MenuItem.get_wholesale_cost(self._list_sales_for_day)  # Accessing object wholesale cost with key
            MenuItem.get_selling_price(self._list_sales_for_day)  # Accessing object selling price with key
        return sales_dict * ((MenuItem.get_selling_price(self._list_sales_for_day) -  # Calculating profit
                              MenuItem.get_wholesale_cost(self._list_sales_for_day)))

    def total_profit_for_stand(self, sales_dict):
        """Method to keep track of all sales"""
        initial_profit = 0  # We start with having made no money
        for self._list_sales_for_day in self._menu_items:
            """"for loop to iterate sales of menu items"""
            for self.total_profit_for_menu_item in self._menu_items:
                """nested for loop iterate profit for each item"""
                total_profit = initial_profit + self.total_profit_for_menu_item(sales_dict)  # Calculations
                return total_profit


def main():
    """Calling the main function"""
    stand = LemonadeStand("Krusty Krab"
    stand.add_menu_item("Lemonade", 2.15, 3.59)
    stand.enter_sales_for_today(10)

    """stand = LemonadeStand("Krusty Krab")
    MenuItem = item1
    stand.add_menu_item(MenuItem)
    sales_for_today = {item1}
    try:
        sales_for_today(item3)
    except InvalidSalesItemOrderError:
        print("That item does not exist")"""


if __name__ == '__main__:':
    """If method to make main function execute when ran as a script"""
    main()
