import math


def area(r):
    '''

    Принимает число r (r > 0) и возвращает площадь круга с радиусом r.
    r: радиус круга, положительное число.
    Для подсчёта площади подключается math, чтобы взять оттуда pi.

    '''
    return math.pi * r * r


def perimeter(r):
    '''

    Принимает число r (r > 0) и возвращает длину окружности с радиусом r.
    r: радиус окружности, положительное число.
    Для подсчёта периметра подключается math, чтобы взять оттуда pi.

    '''
    return 2 * math.pi * r

