import math


def area_circle(r):
    """Вычисление площади круга"""
    return math.pi * r * r


def perimeter_circle(r):
    """Вычисление периметра круга"""
    return 2 * math.pi * r


def area_square(a):
    """Вычисление площади квадрата"""
    return a * a


def perimeter_square(a):
    """Вычисление периметра квадрата"""
    return 4 * a


def area_triangle(a, b, c):
    """Вычисление площади треугольника по формуле Герона"""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter_triangle(a, b, c):
    """Вычисление периметра треугольника"""
    return a + b + c


def calc(shape, *args):
    """Функция для вычисления площади или периметра заданной фигуры"""
    if shape == "circle":
        if len(args) != 1:
            raise ValueError("Круг должен иметь только один аргумент (радиус)")
        r = args[0]
        return {"area": area_circle(r), "perimeter": perimeter_circle(r)}
    elif shape == "square":
        if len(args) != 1:
            raise ValueError("Квадрат должен иметь только один аргумент (сторону)")
        a = args[0]
        return {"area": area_square(a), "perimeter": perimeter_square(a)}
    elif shape == "triangle":
        if len(args) != 3:
            raise ValueError("Треугольник должен иметь три аргумента (стороны)")
        a, b, c = args
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма двух сторон треугольника должна быть больше третьей")
        return {"area": area_triangle(a, b, c), "perimeter": perimeter_triangle(a, b, c)}
    else:
        raise ValueError(f"Неизвестная фигура: {shape}")
