import typing

T = typing.TypeVar("T")


def get_first_element(l: typing.Sequence[T]) -> T:
    return l[0]


assert get_first_element("987") == "9"

Point = typing.NamedTuple("Point", [("x", int), ("y", int)])
point = Point(2, 3)
assert point.x == 2
