import sys

def myfunc(args):
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        arguments = sys.argv[1:]
        print(arguments)
    myfunc(arguments)
