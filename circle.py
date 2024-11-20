import math
import unittest

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

class CircleTest(unittest.TestCase):
    def test_circle_zero_mul(self):
        res = area(0)
        self.assertFalse(res)
    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertFalse(res)
    def test_circle_default_perimeter(self):
        res = perimeter(4)
        self.assertAlmostEqual(res,25.1327,4)
    def test_circle_default_area(self):
        res = area(5)
        self.assertAlmostEqual(res,78.5398, 4)