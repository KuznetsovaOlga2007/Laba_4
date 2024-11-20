import unittest
def area(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (float) : первая сторона прямоугольника
            b (float) : вторая сторона прямоугольника

        Возвращаемое значение:
            S (float) : площадь прямоугольника
    '''
    S = a * b
    return S 

def perimeter(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (float) : первая сторона прямоугольника
            b (float) : вторая сторона прямоугольника

        Возвращаемое значение:
            P (float) : периметр прямоугольника
    '''
    P = (a + b) * 2 
    return P

class RectangleTest(unittest.TestCase):
    def test_rectangle_default_area(self):
        res = area(4, 6);
        self.assertEqual(res,24);
    def test_rectangle_default_perimeter(self):
        res = perimeter(1, 2)
        self.assertEqual(res,6)
    def test_rectangle_zero_side_area(self):
        res1 = area(0, 4);
        self.assertFalse(res1);
    def test_rectangle_zero_side_perimeter(self):
        res1 = perimeter(15, 0);
        self.assertFalse(res1);
    def test_rectangle_same_sides(self):
        res1 = area(3, 4);
        res2 = area(4,3);
        self.assertEqual(res1,12);
        self.assertEqual(res2,res1);