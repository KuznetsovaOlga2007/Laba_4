def area(a):
    if a < 0:
        raise AssertionError("mistake")
    return a * a


def perimeter(a):
    if a < 0:
        raise AssertionError("mistake")
    return 4 * a
