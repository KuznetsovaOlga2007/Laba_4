def area(a: float) -> float:
    """
    Calculates the area of a square given its side length.

    Parameters:
    a (float): Length of the side of the square.

    Returns:
    float: Area of the square.

    Raises:
    ValueError: If the side length is non-positive.

    Example:
    area(4) -> 16.0
    """
    if a <= 0:
        raise ValueError("Side length must be positive.")
    return a * a


def perimeter(a: float) -> float:
    """
    Calculates the perimeter of a square given its side length.

    Parameters:
    a (float): Length of the side of the square.

    Returns:
    float: Perimeter of the square.

    Raises:
    ValueError: If the side length is non-positive.

    Example:
    perimeter(4) -> 16.0
    """
    if a <= 0:
        raise ValueError("Side length must be positive.")
    return 4 * a
