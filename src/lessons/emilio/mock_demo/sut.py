from time import sleep


def big_long_func():
    sleep(50)
    return True


def do_something():
    done = big_long_func()
    return done
