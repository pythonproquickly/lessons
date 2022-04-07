# make sure everything is set up on gitHub
# how do I export/download the whole project? will it mess it up here?
import sqlalchemy
from models import Base, session, Brands, Product, engine
import datetime
import csv
from models import FILE_PATH

ANDY_TEST = True
if ANDY_TEST:  # delete me and this bool variable
    import os

    os.remove(f"{FILE_PATH}inventory.db")

engine.connect()


def menu():
    while True:
        print("""
        Dr. Joy's Grocery Store Inventory Application
        \n Please select a choice:
        N) New Product
        V) View Product
        A) Availability of Product
        B) Backup
        Q) Quit""")
        choice = input("What do you wish to do?").lower()
        if choice in "nvabq":
            return choice
        else:
            print("Please select a valid option")


def price_cents(price):
    return int(round(float(price[1:]) * 100, 0))


def import_csvinventory(brand_map):  # works, but needs cleans
    from datetime import datetime

    with open(f"{FILE_PATH}inventory.csv", newline="") as csvfile1:
        data = csv.DictReader(csvfile1)
        rows = list(data)
        row_counter = 0
        for row in rows:
            row_counter += 1
            new_item = Product(
                id=row_counter,
                name=row['product_name'],
                price=price_cents(row['product_price']),
                quantity=row['product_quantity'],
                updated=datetime.strptime(row['date_updated'], '%m/%d/%Y'),
                brand_id=brand_map[row['brand_name']])
            session.add(new_item)
        session.commit()


def import_csvbrands():  # works
    with open(f"{FILE_PATH}brands.csv") as csvfile2:
        data = csv.reader(csvfile2)
        brand_id_counter = 0
        brand_map = {}
        for row in data:
            brand_id_counter += 1
            brand_name = row[0].strip()
            new_item = Brands(brand_id=brand_id_counter,
                              name=brand_name)
            session.add(new_item)
            brand_map[brand_name] = brand_id_counter
        session.commit()
        return brand_map


def run_app():
    while True:
        choice = menu()
        if choice == "q":
            print("Later Gator, Have a great day!")
            break
        elif choice == "n":
            # new item
            product_name = input("Product name:  ")
            product_price = input("Price in cents, ex $4.21 would be 421:  ")
            product_quantity = input("Quantity:  ")
            date_updated = input("Updated date: (enter in format mm/dd/yyyy)")
            brand_name = input("Brand Name:  ")
            # test it exist / addd
            statement = "select max(id) from product"
            num = engine.execute(statement).fetchall()[0][0]
            statement = f"select brand_id from brands where name = " \
                        f"'{brand_name.strip()}'"
            brand_id = engine.execute(statement).fetchall()[0][0]
            new_item = Product(id=num + 1,
                               name=product_name,
                               price=price_cents(product_price),
                               quantity=product_quantity,
                               updated=datetime.datetime.strptime(date_updated,
                                                                  '%m/%d/%Y'),
                               brand_id=brand_id)
            session.add(new_item)
            session.commit()
            # something goes in here to deal with errors
        elif choice == "v":
            # view

            # Prompt for product id #### TODO
            ## also brancd id generated in db

            statement = "select product.name, product.price, brands.name as " \
                        "brand from brands join product " \
                        "on brands.brand_id = product.brand_id"
            products = engine.execute(statement).fetchall()
            for product in products:
                print(
                    f"{product.name}  |  {product.price}  |  {product.brand}")
            input("Press enter to return to main menu")
        elif choice == "a":

            statement = "select max(price) from product"
            most_expensive_item = engine.execute(statement).fetchall()[0][0]
            statement = "select min(price) from product"
            least_expensive_item = engine.execute(statement).fetchall()[0][0]
            statement = "select brands.name from brands join product  on " \
                        "brands.brand_id = product.brand_id " \
                        "group by brands.name order by count(*) desc limit 1"
            most_common = engine.execute(statement).fetchall()[0][0]
            print(f"""
                  The most expensive item is:\t{most_expensive_item}
                  The least expensive item is:\t {least_expensive_item}
                  The most common brand is:\t\t{most_common}""")
        elif choice == "b":
            with open(f"{FILE_PATH}backup_inventory.csv", "w") as csvfile1:
                fieldnames = ['product_id', 'product_name', 'product_price',
                              'product_quantity', 'date_updated', 'brand_id']
                backup_writer = csv.DictWriter(csvfile1, fieldnames=fieldnames)
                backup_writer.writeheader()
                statement = "SELECT id, name, price, quantity, updated, " \
                            "brand_id FROM product"
                results = engine.execute(statement).fetchall()
                for row in results:
                    csvfile1.write(
                        f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},"
                        f"{row[5]}\n")
                print("Backup database created.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    brand_map = import_csvbrands()
    import_csvinventory(brand_map)
    run_app()
