def largest_perimeter(list_of_edges):
    list_of_edges.sort()
    z = list_of_edges[-1]
    y = list_of_edges[-2]
    x = list_of_edges[-3]
    counter = -3
    while y + x <= z:
        if len(list_of_edges) + counter <= 0:
            return 0
        counter -= 1
        z = y
        y = x
        x = list_of_edges[counter]

    return z + y + x


if __name__ == "__main__":
    assert largest_perimeter([2, 1, 2]) == 5
    assert largest_perimeter([1, 2, 1]) == 0
    assert largest_perimeter([3, 2, 3, 4]) == 10
    assert largest_perimeter([3, 6, 2, 3]) == 8
