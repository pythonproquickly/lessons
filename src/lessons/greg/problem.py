def use_input():
    name_of_customer = input("Name of customer: ")
    package_description = input("Write a package description: ")
    danger = contents_dangerous()


def contents_dangerous():
    while True:
        contents = input("Are the contents dangerous? (Y/N)").lower()
        if contents in ("yn"):
            break
        else:
            contents = input("Are the contents dangerous? (Y/N)").lower()


def main():
    use_input()
    contents_dangerous()


main()
