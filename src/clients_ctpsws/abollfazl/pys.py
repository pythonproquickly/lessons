import pysnooper


@pysnooper.snoop()
def add_up(lhs, rhs):
    return lhs + rhs


add_up(9, 8)
