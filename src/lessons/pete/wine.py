from pywebio import *
from pywebio.output import *
from pywebio.input import *


def main():
    pass

def check_ta():
    total_acidity = input("Enter Ta", placeholder="total acidity", required=True)
    return total_acidity

def _date_brix_temperature_check_ta_output():
    date, brix = date_brix()
    f, c = temperature_convertor()
    with put_collapse("Date | Brix | Fahrenheit | Celsius | Total Acidic"):
        put_table([
            ['Date', 'Brix', 'Fahrenheit', 'Celsius', 'Total Acidic'],
            [put_text(date), put_text(brix), put_text(f), put_text(c), put_text(check_ta())]
    ])

def date_brix():
    date_checked = input("Enter current date", placeholder="Enter today's date", required=True)
    sugar = input("Enter brix")
    return date_checked, sugar

def sO2():
    sugar = float(input(type=NUMBER, placeholder='bring up sO2'))
    return sugar

def moving_decimal(num):
    num /= 1000.
    return num


def calculating_sO2(desired_sO2, gallons):
    bring_up = desired_sO2 * 3.745 * gallons / 0.57
    return round(bring_up, 2)


def temperature_convertor():
    temp = float(input("Enter temp: "))
    celsius = round((temp - 32) * 5 / 9, 1)
    return temp, celsius



def main():
    '''
    An interactive web app that takes user's name
    and output hello <username> on the webpage
    '''
    put_markdown("# **Leony's Inventory Manegmant System**")

    year_of_grape = input("The year grape picked", placeholder="Year picked",
                           required=True)
    put_text("The year: %s" % year_of_grape)

    ava = input("Name of AVA:", placeholder="Whats the AVA name?", required=True)
    put_text("Name of AVA: %s" % ava)

    name_of_vine = input("The name of vine", placeholder="Name of vine", required=True)
    put_text("Name of vine: %s" % name_of_vine)

    date_grapes_picked = input('Date picked:', placeholder='The exact date grapes were picked',
                                required=True)
    put_text('The date Grapes were picked on:  %s' % date_grapes_picked)

    tons = input("How many lbs were picked?", type=FLOAT, placeholder="Weight of product", required=True)
    put_text("Total weight: %slbs" % tons)

    cost = input('Cost', type=NUMBER, placeholder='What was the cost of purchase?', required=True)
    put_text("Cost was: $%s" % cost)

    date_crushed = input("Date grapes crushed:", placeholder="Date grapes crushed", required=True)
    gallons = input("Gallons produced after crushing", type=FLOAT, placeholder="Gallons produced", required=True)

    with put_collapse("Date crushed | Weight | Crushed Gallons"):
        put_table([
            ['Date crushed', 'Weight Crushed', 'Gallons'],
            [put_text("%s" % date_crushed), put_text("%slbs" % tons), put_text("%s" % gallons)]
        ])

    sweet = sO2()
    with put_collapse('Added sO2'):
        put_table([
            ['Add sO2 grams'],
            [put_text(calculating_sO2(moving_decimal(sweet), gallons), "g")]
        ])

    fahrenheit, celsius = temperature_convertor()
    with put_collapse("Temperature"):
        put_table([
            ["Fahrenheit", "Celsius"],
            [put_text(fahrenheit), put_text(celsius)]
        ])

    date, brix = date_brix()
    fahrenheit, celsius = temperature_convertor()
    with put_collapse("Today's date | Brix | Temperature"):
        put_table([
            ["Today's date", "Brix", "Fahrenheit", "Celsius"],
            [put_text(date), put_text(brix), put_text(fahrenheit), put_text(celsius)]
        ])


if __name__ == "__main__":
    main()

