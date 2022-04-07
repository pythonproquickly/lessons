from threading import Thread
import os
from speedup import timer


def replace_in_file(filename, from_value, to_value):
    print(f"Processing {filename}")
    with open(filename, "r") as f:
        file_data = f.read()
    file_data = file_data.replace(from_value, to_value)

    with open(filename, "w") as f:
        f.write(file_data)


def setup():
    filenames = [f"data/thread_demo/thread_demo{n}.txt" for n in range(10)]
    for filename in filenames:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        with open(filename, "w") as f:
            f.write("xxyyzzaaa" * 1000000)
    return filenames


@timer
def run_multi_threaded(filenames):

    threads = [
        Thread(target=replace_in_file, args=(filename, "yy", "1234"))
        for filename in filenames
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


@timer
def run_single_threaded(filenames):
    [replace_in_file(filename, "xx", "5678") for filename in filenames]


def main():
    thread_test_filenames = setup()
    run_multi_threaded(thread_test_filenames)
    run_single_threaded(thread_test_filenames)


if __name__ == "__main__":
    main()
