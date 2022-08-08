"""
today:
- recursion reviewed & explained
- the system stack

---------------

---------------

---------------

---------------

---------------

---------------
a(6)
--------------- ....
a(7)
---------------
a(8)

"""


def a(n):
    if n == 6:
        return n
    return n + a(n - 1)


a(8)
