# pip install pysnooper (in terminal)

import pysnooper


@pysnooper.snoop()
def something(a, q, e, r):
    a = q * 4
    b = q
    c = e / 6
    return a * b * c


something(2, 4, 1, 6)
