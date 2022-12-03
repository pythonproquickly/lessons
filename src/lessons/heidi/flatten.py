import pysnooper


@pysnooper.snoop()
def flatten(nested_list):
    if not nested_list:
        return nested_list
    if isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])
    return nested_list[:1] + flatten(nested_list[1:])


if __name__ == '__main__':
    assert flatten([[[11], [33, 50]]]) == [11, 33, 50]
    assert flatten([[[24, 12, 6, 10]]]) == [24, 12, 6, 10]
