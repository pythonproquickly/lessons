def do_something(a_thing):
    def do_something_else(another_thing):
        return True

    return do_something_else


def the_func():
    return do_something("x")("y")


print(the_func())
