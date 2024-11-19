def area(a: float, b: float, c: float) -> float:
    # Проверка на отрицательные или нулевые длины сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    # Проверка, чтобы стороны могли образовать треугольник
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")
    
    return (a + b + c) / 2

def perimeter(a: float, b: float, c: float) -> float:
    # Проверка на отрицательные или нулевые длины сторон
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    # Проверка, чтобы стороны могли образовать треугольник
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")

    return a + b + c
