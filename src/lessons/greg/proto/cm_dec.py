from contextlib import contextmanager


@contextmanager
def print_it():
    print("Setup here")
    yield

    print("Tear down here")


with print_it() as manager:
    print('use here')