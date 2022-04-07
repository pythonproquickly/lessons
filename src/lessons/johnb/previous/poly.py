def multiplyPolynomials(a, v):
    product = [0] * (len(a) + len(v) - 1)

    for n in range(len(a)):
        for m in range(len(v)):
            product[n + m] += v[m] * a[n]

    return product


def testMultiplyPolynomials():
    assert multiplyPolynomials([2, 3, 0, 4], [1, 5]) == [2, 13, 15, 4, 20]
    assert multiplyPolynomials([1, 5], [2, 3, 0, 4]) == [2, 13, 15, 4, 20]
    assert multiplyPolynomials([7, 3], [2, 4]) == [14, 34, 12]
    assert multiplyPolynomials([3], [5]) == [15]
    assert multiplyPolynomials([0], [2, 1]) == [0, 0]


testMultiplyPolynomials()
