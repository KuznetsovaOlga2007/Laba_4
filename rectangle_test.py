import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = rectangle.area(10, 0)
        res2 = rectangle.area(0, 10)
        res3 = rectangle.area(0, 0)

        self.assertEqual(res1, -1)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_square_mul(self):
        res = rectangle.area(10, 10)

        self.assertEqual(res, 100)

    def test_diff_mul(self):
        res1 = rectangle.area(5, 10)
        res2 = rectangle.area(10, 5)

        self.assertEqual(res1, 50)
        self.assertEqual(res1, res2)

    def test_zero_sum(self):
        res1 = rectangle.perimeter(0, 0)
        res2 = rectangle.perimeter(0, 10)
        res3 = rectangle.perimeter(10, 0)

        self.assertEqual(res1, -1)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_square_sum(self):
        res = rectangle.perimeter(10, 10)

        self.assertEqual(res, 40)

    def test_diff_sum(self):
        res1 = rectangle.perimeter(5, 10)
        res2 = rectangle.perimeter(10, 5)

        self.assertEqual(res1, 30)
        self.assertEqual(res1, res2)
