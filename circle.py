import math


def area(r):
    if r < 0:
        raise AssertionError("mistake")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise AssertionError("mistake")
    return 2 * math.pi * r
