"""import pandas as pd
import matplotlib as mp
import numpy as np

pd.DataFrame()"""


def addup(x, y):
    return x + y


def divide(x, y=1):
    try:
        return x / y
    except ZeroDivisionError:
        return x / 1


def read_from_file():
    #f = open('stuff.txt', 'r')
    with open('stuff.txt', 'r') as f:
        contents = f.readlines()
    # f.close()
    return contents



def doit():
    print(addup(3, 4))
    print(divide(y=0, x=10))
    results = read_from_file()
    print(results)


if __name__ == "__main__":
    doit()
