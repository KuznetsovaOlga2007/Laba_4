import math

def area(a, b, c):
    ''' Принимает 3 числа , возвращает площадь'''
    p = (a+b+c)/2
    return math.sqrt(p *(p-a) *(p-b) * (p-c))


def perimeter(a, b, c):
    ''' Принимает 3 числа , возвращает периметр'''
    return a + b + c
