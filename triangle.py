import math


def area(a):
    p = (a[0] + a[1] + a[2]) / 2
    return math.sqrt(p * (p - a[0]) * (p - a[1]) * (p - a[2]))


def perimeter(a):
    return a[0] + a[1] + a[2]
