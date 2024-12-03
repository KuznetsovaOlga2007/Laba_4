import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)

        self.assertEqual(res, -1)

    def test_mul(self):
        res = square.area(10)

        self.assertEqual(res, 100)

    def test_zero_sum(self):
        res = square.perimeter(0)

        self.assertEqual(res, -1)

    def test_sum(self):
        res = square.perimeter(10)

        self.assertEqual(res, 40)
