def area(a, h):
    '''Принимает два числа - длину основания треугольника и его высоту, 
    возвращает площадь треугольника с заданными основанием и высотой'''
    if a <= 0 or h <= 0:
        print("error: no such triangle")
        return -1

    return a * h / 2 


def perimeter(a, b, c):
    '''Принимает три числа - длины сторон треугольника, возвращает периметр треугольника с заданными сторонами'''
    if a <= 0 or b <= 0 or c <= 0:
        print("error: no such triangle")
        return -1

    if a + b <= c or a + c <= b or b + c <= a:
        print("error: no such triangle")
        return -1

    return a + b + c
