import unittest
import circle
import math


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)

        self.assertEqual(res, -1)

    def test_mul(self):
        res = circle.area(10)

        self.assertEqual(res, math.pi * 100)

    def test_zero_sum(self):
        res = circle.perimeter(0)

        self.assertEqual(res, -1)

    def test_sum(self):
        res = circle.perimeter(10)

        self.assertEqual(res, math.pi * 20)
