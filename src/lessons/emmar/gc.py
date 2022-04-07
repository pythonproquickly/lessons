import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # also time.process_time()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def a():
    pass


def main():
    a()


if __name__ == "__main__":
    main()


"""
timeit.Timer('for i in xrange(10): oct(i)', 'gc.enable()').timeit()
BUT doesnt measure GC by default (turns it off)
CAN iterate
BUT not part of program
"""
