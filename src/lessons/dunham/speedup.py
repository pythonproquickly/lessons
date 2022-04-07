"""
performance analysis
try with and without speedy decorator and compare!!
"""
import functools
import time
import csv


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


class Speedy:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]

@Speedy
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def save_it(alist, name):
    with open(name, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(alist)

@timer
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
