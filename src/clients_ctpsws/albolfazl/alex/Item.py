from datetime import date
import uuid


class Item:
    def __init__(self):
        self.name = input("Provide the customer name: ")
        self.packageDescription = input("Enter package description: ")
        self.isDangerous = input("Are the contents dangerous (Y/N)? ").upper()
        self.weight = float(input("Enter the weight of the package (kgs): "))
        self.volume = float(input("Enter the volume of the package in cubic meters: "))
        self.deliveryDate = date.fromisoformat(
            input("Required delivery date (YYYY-MM-DD): ")
        )
        self.internationalDestination = input(
            "Are the contents going to an international destination (Y/N)? "
        ).upper()
        # if package has to be delivered in less than 3 business days (calculates from today's date)
        self.isUrgent = self.deliveryDate.day - date.today().day < 3

    def calcBestShippingMethod(self):
        possibleShippingMethods = {"air": 0.0, "ground": 0.0, "ocean": 0.0}

        if self.weight >= 10 and self.volume >= 125:
            possibleShippingMethods = {"air": None, "ground": None, "ocean": None}

        if self.isDangerous == "Y":
            possibleShippingMethods["air"] = None

        if self.isUrgent and possibleShippingMethods["air"] is not None:
            possibleShippingMethods["air"] = max(10 * self.weight, 20 * self.volume)
        if (
            possibleShippingMethods["ground"] is not None
            and possibleShippingMethods["ocean"] is not None
        ):
            possibleShippingMethods["air"] = None
            if self.internationalDestination == "Y":
                possibleShippingMethods["ocean"] = 30.0
            else:
                possibleShippingMethods["ocean"] = None
            if self.isUrgent:
                possibleShippingMethods["ground"] = 45.0
            else:
                possibleShippingMethods["ground"] = 25.0

        return possibleShippingMethods

    def returnItemInfo(self):
        return dict(
            [
                ("ID", str(uuid.uuid4())),
                ("name", self.name),
                ("packageDescription", self.packageDescription),
                ("isDangerous", self.isDangerous),
                ("weight", self.weight),
                ("volume", self.volume),
                ("deliveryDate", self.deliveryDate),
                ("internationalDestination", self.internationalDestination),
                ("isUrgent", self.isUrgent),
                ("possibleShippingMethods", self.calcBestShippingMethod()),
            ]
        )
