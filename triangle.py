import unittest;
def area(a, h):
    '''
    Принимает сторону треугольника и высоту к ней.
    Возвращает площадь треугольника

        Параметры:
            a (float) : сторона треугольника
            b (float) : высота, проведённая к этой стороне

        Возвращаемое значение:
            S (float) : площадь треугольника
    '''
    S = a * h / 2 
    return S

def perimeter(a, b, c):
    '''
    Принимает три стороны треугольника.
    Возвращает периметр треугольника.

        Параметры:
            a (float) : первая сторона треугольника
            b (float) : вторая сторона треугольника
            c (float) : третья сторона треугольника

        Возвращаемое значение:
            P (float) : периметр треугольника
    '''
    P = a + b + c
    return P
class TriangleTest(unittest.TestCase):
    def test_triangle_default_area(self):
        res = area(4, 5);
        self.assertEqual(res,10);
    def test_triangle_default_perimeter(self):
        res = perimeter(2, 5, 4)
        self.assertEqual(res,11)
    def test_triangle_zero_side_perimeter(self):
        res1 = perimeter(3, 0, 2);
        self.assertFalse(res1);
    def test_triangle_wrong_side_perimeter(self):
        res1 = perimeter(4, 1, 2);
        self.assertFalse(res1);
    def test_triangle_same_sides(self):
        res1 = area(2 , 3);
        res2 = area(3, 2);
        self.assertEqual(res1, res2);