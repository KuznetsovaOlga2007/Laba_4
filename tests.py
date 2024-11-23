import unittest
from math import pi
import rectangle, circle, square, triangle

import math
from math import *
from math import pi

"""
each class tests its own file's functions using 4 metrics (zero value, minimal integer value, sum of 2, difference)
tested functions are "area" and "perimeter"
"""

# tests for rectangle.py
class TestRectangle (unittest.TestCase):
    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    def test_area_one(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)
    def test_area_sum(self):
        a = rectangle.area(10, 15)
        b = rectangle.area(20, 25)
        c = rectangle.area(30, 15)
        d = rectangle.area(20, 10)
        self.assertEqual(a+b, c+d)
    def test_area_not_eq(self):
        self.assertNotEqual(rectangle.area(10, 90), rectangle.area(10, 9))
    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)
    def test_perimeter_one(self):
        self.assertEqual(rectangle.perimeter(1, 1), 4)
    def test_perimeter_sum(self):
        self.assertEqual(rectangle.perimeter(10+20, 30+40), rectangle.perimeter(10, 30) + rectangle.perimeter(20, 40))
    def test_perimeter_not_eq(self):
        self.assertNotEqual(rectangle.perimeter(10, 20), rectangle.perimeter(1, 20))


# tests for circle.py
class TestCircle (unittest.TestCase):
    def test_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    def test_area_one(self):
        res = circle.area(1)
        self.assertEqual(res, pi)
    def test_area_sum(self):
        a = circle.area(3)
        b = circle.area(4)
        c = circle.area(5)
        self.assertEqual(a+b, c)
    def test_area_not_eq(self):
        self.assertNotEqual(circle.area(10), circle.area(9))
    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)
    def test_perimeter_one(self):
        self.assertEqual(circle.perimeter(1), 2*pi)
    def test_perimeter_sum(self):
        self.assertEqual(circle.perimeter(10) + circle.perimeter(20),circle.perimeter(30))
    def test_perimeter_not_eq(self):
        self.assertNotEqual(circle.perimeter(10), circle.perimeter(20))

# tests for square.py
class TestSquare (unittest.TestCase):
    def test_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_area_one(self):
        res = square.area(1)
        self.assertEqual(res, 1)
    def test_area_sum(self):
        a = square.area(30)
        b = square.area(40)
        c = square.area(50)
        self.assertEqual(a+b, c)
    def test_area_not_eq(self):
        self.assertNotEqual(square.area(9), square.area(10))
    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)
    def test_perimeter_one(self):
        self.assertEqual(square.perimeter(1), 4)
    def test_perimeter_sum(self):
        self.assertEqual(square.perimeter(30), square.perimeter(20) + square.perimeter(10))
    def test_perimeter_not_eq(self):
        self.assertNotEqual(square.perimeter(10), square.perimeter(20))

# tests for triangle.py
class TestTriangle (unittest.TestCase):
    def test_area_zero(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
    def test_area_one(self):
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)
    def test_area_sum(self):
        a = triangle.area(10, 15)
        b = triangle.area(20, 25)
        c = triangle.area(30, 15)
        d = triangle.area(20, 10)
        self.assertEqual(a+b, c+d)
    def test_area_not_eq(self):
        self.assertNotEqual(triangle.area(10, 90), triangle.area(10, 9))
    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
    def test_perimeter_one(self):
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)
    def test_perimeter_sum(self):
        self.assertEqual(triangle.perimeter(10, 20, 30), triangle.perimeter(3, 7, 16) + triangle.perimeter(7, 13, 14))
    def test_perimeter_not_eq(self):
        self.assertNotEqual(triangle.perimeter(10, 20, 5), triangle.perimeter(1, 20, 5))

if __name__ == '__main__':
    unittest.main()
