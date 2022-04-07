def get_factor():
    return 1.1


def subtract(lhs, rhs):
    return (lhs - rhs) * get_factor()


def addup(lhs, rhs):
    x = subtract(lhs, rhs)
    x = x * 45
    total = lhs + rhs + x
    return total * get_factor()


def main():
    first_number = int(input("enter #1 "))
    second_number = int(input("enter #2 "))
    sub = subtract(first_number, 6)
    result = addup(sub, second_number)
    print(result)


if __name__ == "__main__":
    main()
