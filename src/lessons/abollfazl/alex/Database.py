import csv
from pathlib import Path
from Item import Item


def updateDB():
    database_cols=['ID', 'name', 'packageDescription', 'isDangerous', 'weight', 'volume', 'deliveryDate',
                                 'internationalDestination', 'isUrgent', 'possibleShippingMethods']

    itemDict = Item().returnItemInfo()
    csv_file = 'booking_quotes.csv'
    file_exists = Path('booking_quotes.csv').exists()

    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=database_cols)
            if not file_exists:
                writer.writeheader()
            writer.writerow(itemDict)

    except IOError:
        print('I/O error')

    print("Added item to database!")
    print(itemDict)

updateDB()