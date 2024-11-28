import unittest
from math import pi
import rectangle, circle, triangle, square
'''Each test checks if program returns right number. It tests for perimeter and area'''

class RectangleTestCase(unittest.TestCase):
    def test_area_zero (self) :
        res = rectangle.area (0 , 34567)
        self.assertEqual(res, 0)
    def test_area_int (self) :
        res = rectangle.area (122, 98)
        self.assertEqual(res, 11956)
    def test_area_float (self) :
        res = rectangle.area (14.87,2.57)
        self.assertEqual(res, 38.2159)

    def test_per_zero (self) :
        res = rectangle.perimeter (0, 0)
        self.assertEqual(res, 0)
    def test_per_float (self) :
        res = rectangle.perimeter (4.25, 5.75)
        self.assertEqual(res, 20)
    def test_per_int (self) :
        res = rectangle.perimeter (3, 745)
        self.assertEqual(res, 1496)


class CircleTestCase(unittest.TestCase) :
    def test_area_null (self) :
        res = circle.area (0)
        self.assertEqual(res, 0)
    def test_area_int (self) :
        res = circle.area (7)
        self.assertEqual(res, 49 * pi)
    def test_area_float (self) :
        res = circle.area (9.11)
        self.assertEqual(res, 82.9921 * pi)

    def test_per_zero(self):
        res = circle.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_float (self) :
        res = circle.perimeter (31.1)
        self.assertEqual(res, 62.2 * pi)
    def test_per_int (self) :
        res = circle.perimeter (80)
        self.assertEqual(res, 160 * pi)


class SquareTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = square.area (0)
        self.assertEqual(res, 0)
    def test_area_float(self):
        res = square.area (2.5)
        self.assertEqual(res, 6.25)
    def test_area_int (self) :
        res = square.area (17)
        self.assertEqual(res, 289)

    def test_per_zero (self) :
        res = square.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_int (self) :
        res = square.perimeter (11)
        self.assertEqual(res, 44)
    def test_per_float (self) :
        res = square.perimeter (11.5)
        self.assertEqual(res,46)

class TriangleTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = triangle.area (0,4,5)
        self.assertEqual(res, 0)
    def test_area_float (self) :
        res = triangle.area (0.3, 0.4, 0.5)
        self.assertEqual(res, 0.059999999999999984)
    def test_area_int (self) :
        res = triangle.area (99887, 88556, 12333)
        self.assertEqual(res, 228910574.3991371)

    def test_per_zero (self) :
        res = triangle.perimeter (0, 0, 0)
        self.assertEqual(res, 0)
    def test_per_int (self) :
        res = triangle.perimeter (45378, 96343, 76845)
        self.assertEqual(res, 218566)
    def test_per_float (self) :
        res = triangle.perimeter (865.3, 342.8, 498.45)
        self.assertEqual(res, 1706.55)


