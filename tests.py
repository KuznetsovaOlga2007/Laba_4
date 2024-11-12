import unittest
from math import pi
import rectangle, circle, triangle, square

class RectangleTestCase(unittest.TestCase):
    def test_area_zero (self) :
        res = rectangle.area (10 , 0)
        self.assertEqual(res, 0)
    def test_area_zero_zero (self) :
        res = rectangle.area (0, 0)
        self.assertEqual(res, 0)
    def test_area_two (self) :
        res = rectangle.area (2, 2)
        self.assertEqual(res, 4)
    def test_area_ten (self) :
        res = rectangle.area (10, 4)
        self.assertEqual(res, 40)
    def test_per_zero (self) :
        res = rectangle.perimeter (10 , 0)
        self.assertEqual(res, 20)
    def test_per_zero_zero (self) :
        res = rectangle.perimeter (0, 0)
        self.assertEqual(res, 0)
    def test_per_two (self) :
        res = rectangle.perimeter (3, 2)
        self.assertEqual(res, 10)
    def test_per_ten (self) :
        res = rectangle.perimeter (10, 4)
        self.assertEqual(res, 28)
class CircleTestCase(unittest.TestCase) :
    def test_area_null (self) :
        res = circle.area (0)
        self.assertEqual(res, 0)
    def test_area_three (self) :
        res = circle.area (3)
        self.assertEqual(res, 9 * pi)
    def test_area_four (self) :
        res = circle.area (4)
        self.assertEqual(res, 16 * pi)
    def test_area_ten (self) :
        res = circle.area (10)
        self.assertEqual(res, 100 * pi)
    def test_per_null (self) :
        res = circle.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_three (self) :
        res = circle.perimeter (3)
        self.assertEqual(res, 6 * pi)
    def test_per_four (self) :
        res = circle.perimeter (4)
        self.assertEqual(res, 8 * pi)
    def test_per_ten (self) :
        res = circle.perimeter (10)
        self.assertEqual(res, 20 * pi)

class SquareTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = square.area (0)
        self.assertEqual(res, 0)
    def test_area_two (self) :
        res = square.area (2)
        self.assertEqual(res, 4)
    def test_area_eight (self) :
        res = square.area (8)
        self.assertEqual(res, 64)
    def test_area_ten (self) :
        res = square.area (10)
        self.assertEqual(res, 100)
    def test_per_zero (self) :
        res = square.perimeter (0)
        self.assertEqual(res, 0)
    def test_per_two (self) :
        res = square.perimeter (2)
        self.assertEqual(res, 8)
    def test_per_five (self) :
        res = square.perimeter (5)
        self.assertEqual(res, 20)
    def test_per_ten (self) :
        res = square.perimeter (10)
        self.assertEqual(res, 40)
class TriangleTestCase(unittest.TestCase) :
    def test_area_zero (self) :
        res = triangle.area (10 , 0)
        self.assertEqual(res, 0)
    def test_area_six (self) :
        res = triangle.area (3, 2)
        self.assertEqual(res, 3)
    def test_area_two (self) :
        res = triangle.area (2, 2)
        self.assertEqual(res, 2)
    def test_area_ten (self) :
        res = triangle.area (10, 8)
        self.assertEqual(res, 40)
    def test_per_zero (self) :
        res = triangle.perimeter (0, 0, 0)
        self.assertEqual(res, 0)
    def test_per_six (self) :
        res = triangle.perimeter (1, 2, 3)
        self.assertEqual(res, 6)
    def test_per_nine (self) :
        res = triangle.perimeter (3, 2, 4)
        self.assertEqual(res, 9)
    def test_per_ten (self) :
        res = triangle.perimeter (2, 3, 5)
        self.assertEqual(res, 10)


