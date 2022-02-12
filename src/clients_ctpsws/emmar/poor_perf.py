"""
performance analysis
"""
import csv


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def save_it(alist, name):
    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(alist)


def calc(write=False, ranges=(25, 35, 20, 42)):
    a = [fibo(i) for i in range(ranges[0])]
    if write:
        save_it(a, "a.csv")
    b = [fibo(i) for i in range(ranges[1])]
    if write:
        save_it(b, "b.csv")
    c = [fibo(i) for i in range(ranges[2])]
    if write:
        save_it(c, "c.csv")
    d = [fibo(i) for i in range(ranges[3])]
    if write:
        save_it(d, "d.csv")


if __name__ == "__main__":
    calc(True, (24, 34, 21, 42))
