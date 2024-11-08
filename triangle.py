import math


def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    return a + b + c
