
def perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            "The sum of any two sides must be greater than the third side."
        )

    return a + b + c
