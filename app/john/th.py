#import pysnooper


def main():
    n = int(input("Enter the number of discs: "))
    source = 1
    spare = 2
    target = 3
    hanoi(n, source, spare, target)


# @pysnooper.snoop()
def hanoi(n, source, spare, target):
    if n == 1:
        print("Move a disk from ", source, " to ", target)
    elif n == 0:
        return
    else:
        hanoi(n - 1, source, target, spare)
        print("Move a disk from ", source, " to ", target)
        hanoi(n - 1, spare, source, target)


if __name__ == "__main__":
    main()
