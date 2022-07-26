
def dothis():
    print("in dothis")


def dothat():
    print("dothat")


def main():

    while True:
        data = input("Enter something: ")
        if data == "q":
            break
        if data < "m":
            continue
        else:
            dothat()
        print("loop again")


if __name__ == "__main__":
    main()
