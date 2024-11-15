import math


def area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle inequality violated")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle inequality violated")
    return a + b + c
