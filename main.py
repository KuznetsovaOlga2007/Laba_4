import unittest
from rectangle import *
from square import *
from triangle import *
from circle import *
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_test_1(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)
    def test_rectangle_area_test_2(self):
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_area_test_3(self):
        res = rectangle_area(1, 55676865462)
        self.assertEqual(res, 55676865462)
    def test_rectangle_area_test_4(self):
        res = rectangle_area(1000000, 10000)
        self.assertEqual(res, 10000000000)
    def test_rectangle_area_test_5(self):
        res = rectangle_area(1, 1)
        self.assertEqual(res, 1)
    def test_rectangle_area_test_6(self):
        res = rectangle_area(89, 9)
        self.assertEqual(res, 801)
    def test_rectangle_area_test_7(self):
        res = rectangle_area(89, 90)
        self.assertEqual(res, 8010)
    def test_rectangle_area_test_8(self):
        res = rectangle_area(9, 9)
        self.assertEqual(res, 81)
    def test_rectangle_area_test_9(self):
        res = rectangle_area(12, 9)
        self.assertEqual(res, 108)
    def test_rectangle_area_test_10(self):
        res = rectangle_area(17, 19)
        self.assertEqual(res, 323)
    
    def test_rectangle_perimeter_test_1(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_rectangle_perimeter_test_2(self):
        res = rectangle_perimeter(100, 100)
        self.assertEqual(res, 400)
    def test_rectangle_perimeter_test_3(self):
        res = rectangle_perimeter(1, 9)
        self.assertEqual(res, 20)
    def test_rectangle_perimeter_test_4(self):
        res = rectangle_perimeter(100000000, 1)
        self.assertEqual(res, 200000002)
    def test_rectangle_perimeter_test_5(self):
        res = rectangle_perimeter(7857965785, 5424346)
        self.assertEqual(res, 15726780262)
    def test_rectangle_perimeter_test_6(self):
        res = rectangle_perimeter(78, 542)
        self.assertEqual(res, 1240)
    def test_rectangle_perimeter_test_7(self):
        res = rectangle_perimeter(52, 52)
        self.assertEqual(res, 208)
    def test_rectangle_perimeter_test_8(self):
        res = rectangle_perimeter(13, 4)
        self.assertEqual(res, 34)
    def test_rectangle_perimeter_test_9(self):
        res = rectangle_perimeter(0, 52)
        self.assertEqual(res, 104)
    def test_rectangle_perimeter_test_10(self):
        res = rectangle_perimeter(2, 2)
        self.assertEqual(res, 8)
    
class CircleTestCase(unittest.TestCase):
    def test_circle_area_test_1(self):
        res = circle_area(1)
        self.assertEqual(res, math.pi)
    def test_circle_area_test_2(self):
        res = circle_area(100000)
        self.assertEqual(res, 10000000000 * math.pi)
    def test_circle_area_test_3(self):
        res = circle_area(25)
        self.assertEqual(res, 625 * math.pi)
    def test_circle_area_test_4(self):
        res = circle_area(250)
        self.assertEqual(res, 62500 * math.pi)
    def test_circle_area_test_5(self):
        res = circle_area(0)
        self.assertEqual(res, 0)
    def test_circle_area_test_6(self):
        res = circle_area(89)
        self.assertEqual(res, 7921 * math.pi)
    def test_circle_area_test_7(self):
        res = circle_area(52)
        self.assertEqual(res, 2704 * math.pi)
    def test_circle_area_test_8(self):
        res = circle_area(2)
        self.assertEqual(res, 4 * math.pi)
    def test_circle_area_test_9(self):
        res = circle_area(0.1)
        self.assertEqual(res, 0.01 * math.pi)
    def test_circle_area_test_10(self):
        res = circle_area(-1)
        self.assertEqual(res, math.pi)

    def test_circle_perimeter_test_1(self):
        res = circle_perimeter(1)
        self.assertEqual(res, 2 * math.pi)
    def test_circle_perimeter_test_2(self):
        res = circle_perimeter(1 / math.pi)
        self.assertEqual(res, 2)
    def test_circle_perimeter_test_3(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)
    def test_circle_perimeter_test_4(self):
        res = circle_perimeter(2 / math.pi)
        self.assertEqual(res, 4)
    def test_circle_perimeter_test_5(self):
        res = circle_perimeter(100000)
        self.assertEqual(res, 200000 * math.pi)
    def test_circle_perimeter_test_6(self):
        res = circle_perimeter(-100000)
        self.assertEqual(res, -200000 * math.pi)
    def test_circle_perimeter_test_7(self):
        res = circle_perimeter(52)
        self.assertEqual(res, 104 * math.pi)
    def test_circle_perimeter_test_8(self):
        res = circle_perimeter(2)
        self.assertEqual(res, 4 * math.pi)
    def test_circle_perimeter_test_9(self):
        res = circle_perimeter(0.5)
        self.assertEqual(res, math.pi)
    def test_circle_perimeter_test_10(self):
        res = circle_perimeter(0.01)
        self.assertEqual(res, 0.02 * math.pi)

class SquareTestCase(unittest.TestCase):
    def test_square_area_test_1(self):
        res = square_area(1)
        self.assertEqual(res, 1)
    def test_square_area_test_2(self):
        res = square_area(2)
        self.assertEqual(res, 4)
    def test_square_area_test_3(self):
        res = square_area(100000)
        self.assertEqual(res, 10000000000)
    def test_square_area_test_4(self):
        res = square_area(52)
        self.assertEqual(res, 2704)
    def test_square_area_test_5(self):
        res = square_area(8)
        self.assertEqual(res, 64)
    def test_square_area_test_6(self):
        res = square_area(-10)
        self.assertEqual(res, 100)
    def test_square_area_test_7(self):
        res = square_area(0)
        self.assertEqual(res, 0)
    def test_square_area_test_8(self):
        res = square_area(25)
        self.assertEqual(res, 625)
    def test_square_area_test_9(self):
        res = square_area(9)
        self.assertEqual(res, 81)
    def test_square_area_test_10(self):
        res = square_area(600)
        self.assertEqual(res, 360000)

    def test_square_perimeter_test_1(self):
        res = square_perimeter(1)
        self.assertEqual(res, 4)
    def test_square_perimeter_test_2(self):
        res = square_perimeter(10000)
        self.assertEqual(res, 40000)
    def test_square_perimeter_test_3(self):
        res = square_perimeter(-1)
        self.assertEqual(res, -4)
    def test_square_perimeter_test_4(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)
    def test_square_perimeter_test_5(self):
        res = square_perimeter(0.1)
        self.assertEqual(res, 0.4)
    def test_square_perimeter_test_6(self):
        res = square_perimeter(2546)
        self.assertEqual(res, 10184)
    def test_square_perimeter_test_7(self):
        res = square_perimeter(1.5)
        self.assertEqual(res, 6)
    def test_square_perimeter_test_8(self):
        res = square_perimeter(6.25)
        self.assertEqual(res, 25)
    def test_square_perimeter_test_9(self):
        res = square_perimeter(8)
        self.assertEqual(res, 32)
    def test_square_perimeter_test_10(self):
        res = square_perimeter(3545224345)
        self.assertEqual(res, 14180897380)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_test_1(self):
        res = triangle_area(5, 4)
        self.assertEqual(res, 10)
    def test_triangle_area_test_2(self):
        res = triangle_area(0, 4)
        self.assertEqual(res, 0)
    def test_triangle_area_test_3(self):
        res = triangle_area(5, 0)
        self.assertEqual(res, 0)
    def test_triangle_area_test_4(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 0)
    def test_triangle_area_test_5(self):
        res = triangle_area(1, 2)
        self.assertEqual(res, 1)
    def test_triangle_area_test_6(self):
        res = triangle_area(-1, 2)
        self.assertEqual(res, -1)
    def test_triangle_area_test_7(self):
        res = triangle_area(-1, -2)
        self.assertEqual(res, 1)
    def test_triangle_area_test_8(self):
        res = triangle_area(1000000, 1000000)
        self.assertEqual(res, 500000000000)
    def test_triangle_area_test_9(self):
        res = triangle_area(0.5, 4)
        self.assertEqual(res, 1)
    def test_triangle_area_test_10(self):
        res = triangle_area(52, 4)
        self.assertEqual(res, 104)

    
    def test_triangle_perimeter_test_1(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_triangle_perimeter_test_2(self):
        res = triangle_perimeter(1, 1, 1)
        self.assertEqual(res, 3)
    def test_triangle_perimeter_test_3(self):
        res = triangle_perimeter(1000, 1000, 1000)
        self.assertEqual(res, 3000)
    def test_triangle_perimeter_test_4(self):
        res = triangle_perimeter(200, 300, 400)
        self.assertEqual(res, 900)
    def test_triangle_perimeter_test_5(self):
        res = triangle_perimeter(252, 312, 499)
        self.assertEqual(res, 1063)
    def test_triangle_perimeter_test_6(self):
        res = triangle_perimeter(1000000000, 1000000000, 1000000000)
        self.assertEqual(res, 3000000000)
    def test_triangle_perimeter_test_7(self):
        res = triangle_perimeter(-5, -3, -4)
        self.assertEqual(res, -12)
    def test_triangle_perimeter_test_8(self):
        res = triangle_perimeter(25, 50, 60)
        self.assertEqual(res, 135)
    def test_triangle_perimeter_test_9(self):
        res = triangle_perimeter(250, 520, 640)
        self.assertEqual(res, 1410)
    def test_triangle_perimeter_test_10(self):
        res = triangle_perimeter(6, 8, 10)
        self.assertEqual(res, 24)