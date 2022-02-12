from typing import Any

import re
from operator import itemgetter


def readData():

    d = dict()
    listDicts = list()
    numbers = list()
    alphabet = list()
    i = 0
    # j = 0

    file = open("data.txt", "r")
    line = file.read()

    lines_list = line.split("\n")

    for i in range(0, len(lines_list) - 1):
        alphabet = [char for char in lines_list[i].split() if char.isupper()]
        alphabet = [s.strip(":") for s in alphabet]
        numbers = [int for int in lines_list[i].split() if int.isdigit()]
        d.update({"A": i + 1})
        d.update(dict(zip(alphabet, numbers)))
        listDicts.append(d)
        d = {}

    return listDicts

    # print(listDicts)
    # print(d)
    # for i in range(0, len(listDicts)):
    # print(listDicts[i])


data = readData()


def parse_query_file(
    data=data,
):  # read file removing the new line and spliting the string by delimeter ;
    path = "final.txt"

    file = open(path, "r")

    x = True

    count = 0
    while x:
        line = file.readline()
        if not line:
            # print('EOF')
            x = False

        elif line == "SORT\n":
            x = file.readline()
            if "= 1" in x:
                key_to_sort = x[0]
                val = int
                for i in data:
                    if key_to_sort in i:
                        print(key_to_sort, i.get(key_to_sort))

                        # first I need to put i.get(key to sort) in a list and sort then print
                        # print(key_to_sort + ":" + "", (i.get(key_to_sort)))

                """
                for i in data:
                    if key_to_sort in i.keys():
                        print(i)
                """
            if "= -1" in x:
                key_to_sort = x[0]
                for i in data:
                    if key_to_sort in i:
                        # use pythons key value pair to sort on value
                        print(i)

                        # if ><= in x do something
                        # elif ; in line print whatevers in this line

        elif "FIND\n" in line:
            x = file.readline()
            key_to_find = x[0]
            for i in data:
                cond = x[2]
                num = int(x[4:])
                if (
                    key_to_find in i and cond == "<"
                ):  # and i.get(key_to_find) < num is True:

                    # print(int(i.get(key_to_find)))
                    if int(i.get(key_to_find)) < num:
                        print(i)
                        # x = file.readline()

                        # if ";" in x:

                        # keys_to_print = x[0:-1]
                        # if keys_to_print in i:

                        # print(i)
                if (
                    key_to_find in i and cond == ">"
                ):  # and i.get(key_to_find) < num is True:

                    # print(int(i.get(key_to_find)))
                    if int(i.get(key_to_find)) > num:
                        print(i)
                if key_to_find in i and cond == "=":

                    if int(i.get(key_to_find)) == num:
                        print(i)

                # if "Y" in line:
                # print("Y in line")
                # x = file.readline()
                # key_to_find = x[0:-1]
                # if key_to_find in i:
                # print(i)

                # cond = x[2]
                # num = int(x[4:])
                # if cond == "<" and i.get(key_to_find) < num is True:
                # print(key_to_find + ":" + " ", (i.get(key_to_find)))

                # elif cond == ">":

                # elif cond == "=":

                # else:

                # print(i.get(key_to_find) + " " + cond + " " + num)
                # if (i.get(key_to_find) + " " + cond + " " + num) is True:
                # print(key_to_find + ":" + " ", (i.get(key_to_find)))
                # print(type())

        else:
            if ";" in line:
                print("error")

        count += 1
    file.close()


pq = parse_query_file()
