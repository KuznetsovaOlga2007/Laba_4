def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")
    
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The provided sides do not form a triangle")
    
    return a + b + c
