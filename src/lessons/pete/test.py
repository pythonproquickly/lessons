from pywebio import *
from pywebio.output import *
from pywebio.input import *


def date_brix():
    date_checked = input("Enter current date", placeholder="Enter today's date", required=True)
    sugar = input("Enter brix")
    return date_checked, sugar


def temperature_convertor():
    temp = float(input("Enter temp: "))
    celsius = round((temp - 32) * 5 / 9, 1)
    return temp, celsius


def check_ta():
    total_acidity = input("Enter Ta", placeholder="total acidity", required=True)
    return total_acidity


def date_brix_temperature_check_ta_output():
    date, brix = date_brix()
    f, c = temperature_convertor()
    put_table([
        ['Date', 'Brix', 'Fahrenheit', 'Celsius', 'Total Acidic'],
        [put_text(date), put_text(brix), put_text(f), put_text(c), put_text(check_ta())]
    ])


@use_scope('scope1', clear=True)
def edit():
    put_text(input("edit")).onclick(edit)


@use_scope('scope2', clear=True)
def edit1():
    put_text(input("edit")).onclick(edit1)


def main():
    put_table([
        ['date', 'time'],
        [put_scope('scope1', put_text('eggs')), put_scope('scope2', put_text('bacon'))]
    ])
    while True:
        if actions('Edit?', ['edit', 'Cancel']) == 'edit':
            edit()
            edit1()
        else:
            break


if __name__ == "__main__":
    main()
