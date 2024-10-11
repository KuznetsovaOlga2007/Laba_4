import math


def area(r):
    '''
    Функция для вычисления площади круга.
        Параметры:
            r(int) - радиус круга
        Возращаемое значение:
            pi*r*r - площадь круга 
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Функция для вычисления периметра круга:
        Параметры:
            r (int) - радиус круга
        Возвращаемое значение:
            2*pi*r - периметр круга
    '''
    return 2 * math.pi * r

