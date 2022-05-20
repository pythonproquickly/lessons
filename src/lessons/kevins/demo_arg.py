import sys


def display(my_data):  # my_data is a parameter
    print(my_data)
    return


if __name__ == "__main__":
    data = sys.argv[1:]
    display(data)  # data is an argument
