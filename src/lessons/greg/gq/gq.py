from datetime import datetime
from datetime import date


class Package:

    def __init__(self, booking):
        self.booking = booking  # setting the instance variables of package
        # to be equal to the booking dictionary

    def shipping_info(self):
        '''self.booking[
            "volume"] = self.package_volume()  # running those new functions
        # to add new keys to the isntance variable of booking
        self.booking["weight"] = self.package_weight()
        self.booking["dangerous"] = self.contents_dangerous()
        self.booking["international"] = self.international()
        self.booking["delivery_date"] = self.delivery_date()
        self.booking["contents"] = self.contents_dangerous()
        self.booking["shipment_type"] = self.shipment_type()'''
        self.package_volume()  # running those new functions
        # to add new keys to the isntance variable of booking
        self.package_weight()
        self.contents_dangerous()
        self.international()
        self.delivery_date()
        self.contents_dangerous()
        self.shipment_type()


    def package_weight(self):
        while True:
            if self.booking["weight"] <= 10:
                print("This package is an appropriate weight  to ship.")
                break
            else:
                print("You're package is too heavy")
                self.booking["weight"] = int(
                    input("Write a package weight (in kgs): "))

    def package_volume(self):
        while True:
            if self.booking["volume"] <= 125:
                print("This package's volume is an appropriate size to ship.")
                break
            else:
                print("You're package is too large")
                self.booking["volume"] = int(
                    input("Write a package weight (in cubic meters): "))

    def contents_dangerous(self):
        while True:
            if self.booking["contents"] in ("yn"):
                break
            else:
                self.booking["contents"] = input(
                    "Are the contents dangerous? (Y/N)").lower()

    def international(self):
        while True:
            if self.booking["international"] in ("yn"):
                break
            else:
                self.booking["international"] = input(
                    "Are you shipping internationally? (Y/N)").lower()

    def delivery_date(self):
        today = date.today()
        today = today.strftime("%d/%m/%Y")
        start = datetime.strptime(today, "%d/%m/%Y")
        end = datetime.strptime(self.booking["delivery_date"], "%d/%m/%Y")
        # get the difference between wo dates as timedelta object
        diff = end.date() - start.date()
        self.booking["delivery_date"] = int(diff.days)


    def shipment_type(self):
        print(self.booking["delivery_date"])
        print(self.booking["weight"])
        print(self.booking["volume"])
        if self.booking["delivery_date"] <= 3 and self.booking[
            "weight"] <= 10 and self.booking["volume"] <= 125:
            self.booking["shipment_type"] == "air"
        elif self.booking["contents"] == "y".lower():
            self.booking["shipment_type"] != "air"
        elif self.booking["weight"] <= 9 and self.booking["volume"] <= 124 and \
                self.booking["delivery_date"] >= 3:
            self.booking["shipment_type"] == "truck"
        elif self.booking["weight"] <= 9 and self.booking["volume"] <= 124 and \
                self.booking["international"] == "y".lower():
            self.booking["shipment_type"] == "ocean"
        return self.booking["shipment_type"]

        # elif: self.package_weight <

        self.volume = volume
        self.package_weight = package_weight
        self.delivery_date = delivery_date
        self.international = international

        ocean = 30
        # truck = 25 or 45 if urgent


def user_input():
    booking = dict()
    booking["name_of_customer"] = input("Name of customer: ")
    booking["volume"] = int(
        input("Write a package volume (in cubic meters): "))
    booking["weight"] = int(input("Write a package weight (in kgs): "))
    booking["description"] = input("Write a package description: ")
    booking["delivery_date"] = input(
        "Write a package description (DD/MM/YYYY): ")
    booking["international"] = input(
        "Is this shipping internationally? (Y/N): ").lower()
    booking["contents"] = input("Are the contents dangerous? (Y/N): ").lower()
    booking["shipment_type"] = ""
    return booking


def main():
    booking = user_input()
    print(booking)
    packaging = Package(booking)
    packaging.shipping_info()


main()
