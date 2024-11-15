import math


def area(a: float, b: float, c: float) -> float:
    """
    Вычисляет площадь треугольника.

    Параметры:
    a (float): длина первой стороны треугольника.
    b (float): длина второй стороны треугольника.
    c (float): длина третьей стороны треугольника.

    Возвращаемое значение:
    float: площадь треугольника.

    Raises:
    ValueError: Если треугольника нет.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides bad.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a: float, b: float, c: float) -> float:
    """
    Вычисляет периметр треугольника по заданным сторонам.

    Параметры:
    a (float): длина первой стороны треугольника.
    b (float): длина второй стороны треугольника.
    c (float): длина третьей стороны треугольника.

    Возвращаемое значение:
    float: периметр треугольника.

    Raises:
    ValueError: не удовлетворяют условиям существования треугольника.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum two sides must  third side.")
    return a + b + c
