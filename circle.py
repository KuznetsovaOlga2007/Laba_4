import math


def area(r: float) -> float:
    """
    Calculates the area of a circle given its radius.

    Parameters:
    r (float): Radius of the circle.

    Returns:
    float: Area of the circle.

    Raises:
    ValueError: If the radius is non-positive.

    Example:
    area(5) -> 78.53981633974483
    """
    if r <= 0:
        raise ValueError("Radius must be positive.")
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Calculates the perimeter (circumference) of a circle given its radius.

    Parameters:
    r (float): Radius of the circle.

    Returns:
    float: Perimeter of the circle.

    Raises:
    ValueError: If the radius is non-positive.

    Example:
    perimeter(5) -> 31.41592653589793
    """
    if r <= 0:
        raise ValueError("Radius must be positive.")
    return 2 * math.pi * r
