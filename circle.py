import math

def area(r):
    '''Принимает число - радиус окружности, возвращает площадь круга с заданным радиусом'''
    if r <= 0:
        print("error: no such circle")
        return -1

    return math.pi * r * r


def perimeter(r):
    '''Принимает число - радиус окружности, возвращает длину окружности с заданным радиусом'''
    if r <= 0:
        print("error: no such circle")
        return -1

    return 2 * math.pi * r
