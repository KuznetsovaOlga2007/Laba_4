def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    return a + b + c
