import math


def area(a: float, b: float, c: float) -> float:
    """
    Calculates the area of a triangle given its three sides using Heron's formula.

    Parameters:
    a (float): Length of the first side of the triangle.
    b (float): Length of the second side of the triangle.
    c (float): Length of the third side of the triangle.

    Returns:
    float: Area of the triangle.

    Raises:
    ValueError: If any side is non-positive or the sides do not satisfy the triangle inequality.

    Example:
    area(3, 4, 5) -> 6.0
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides must be greater than the third side.")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a: float, b: float, c: float) -> float:
    """
    Calculates the perimeter of a triangle given its three sides.

    Parameters:
    a (float): Length of the first side of the triangle.
    b (float): Length of the second side of the triangle.
    c (float): Length of the third side of the triangle.

    Returns:
    float: Perimeter of the triangle.

    Raises:
    ValueError: If any side is non-positive or the sides do not satisfy the triangle inequality.

    Example:
    perimeter(3, 4, 5) -> 12.0
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive.")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides must be greater than the third side.")
    return a + b + c
