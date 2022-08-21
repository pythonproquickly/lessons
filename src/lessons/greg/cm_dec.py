from contextlib import contextmanager


@contextmanager
def print_it():
    print("Setup here") # eg open file
    yield
    print("Tear down here") # eg close file


with print_it() as manager:
    print('use here')
    