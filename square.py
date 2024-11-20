import unittest
def area(a):
    '''
    Возвращает площадь квадрата.

        Параметры:
            a (float) : сторона квадрата

        Возвращаемое значение:
            S (float) : площадь квадрата
    '''
    S = a * a
    return S


def perimeter(a):
    '''
    Возвращает периметр квадрата.

        Параметры:
            a (float) : сторона квадрата

        Возвращаемое значение:
            P (float) : периметр квадрата
    '''
    P = 4 * a
    return P

class SquareTest(unittest.TestCase):
    def test_square_default_area(self):
        res = area(4);
        self.assertEqual(res,16);
    def test_square_default_perimeter(self):
        res = perimeter(3.5)
        self.assertEqual(res,14)
    def test_square_zero_side_perimeter(self):
        res1 = perimeter(0);
        self.assertFalse(res1);
    def test_square_zero_side_area(self):
        res1 = area(0);
        self.assertFalse(res1);