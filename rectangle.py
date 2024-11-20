def area(a, b):
    '''Принимает два числа - длины сторон прямоугольника, возвращает площадь прямоугольника с заданными сторонами'''
    if a <= 0 or b <= 0:
        print("error: no such rectangle")
        return -1

    return a * b 


def perimeter(a, b):
    '''Принимает два числа - длины сторон прямоугольника, возвращает периметр прямоугольника с заданными сторонами'''
    if a <= 0 or b <= 0:
        print("error: no such rectangle")
        return -1

    return (a + b) * 2
