import math


def area(r):
    '''
    Принимает радиус окружности, возвращает её площадь.

            Параметры:
                r (float): радиус окружности

            Возвращаемое значение:
                S (float) : площадь окружности
    '''
    S = math.pi * r * r
    return S


def perimeter(r):
        '''
    Принимает радиус окружности, возвращает её периметр.

            Параметры:
                r (float): радиус окружности

            Возвращаемое значение:
                P (float) : периметр окружности
    '''
    P = 2 * math.pi * r
    return P

