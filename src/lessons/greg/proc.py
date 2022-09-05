
import functools
import time


def time_me(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@time_me
def main():
    print("start")
    time.sleep(12)
    print("stop")


if __name__ == "__main__":
    main()
