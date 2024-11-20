import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = triangle.area(10, 0)
        res2 = triangle.area(0, 10)
        res3 = triangle.area(0, 0)

        self.assertEqual(res1, -1)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_equal_mul(self):
        res = triangle.area(10, 10)

        self.assertEqual(res, 50)

    def test_diff_mul(self):
        res1 = triangle.area(5, 10)
        res2 = triangle.area(10, 5)

        self.assertEqual(res1, 25)
        self.assertEqual(res1, res2)

    def test_zero_sum(self):
        res1 = triangle.perimeter(0, 0, 0)
        res2 = triangle.perimeter(10, 0, 0)
        res3 = triangle.perimeter(10, 10, 0)

        self.assertEqual(res1, -1)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_triple_equal_sum(self):
        res = triangle.perimeter(10, 10, 10)

        self.assertEqual(res, 30)

    def test_double_equal_sum(self):
        res1 = triangle.perimeter(5, 10, 10)
        res2 = triangle.perimeter(10, 5, 10)
        res3 = triangle.perimeter(10, 10, 5)

        self.assertEqual(res1, 25)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_double_equal_existence(self):
        res = triangle.perimeter(5, 5, 10)

        self.assertEqual(res, -1)

    def test_diff_sum(self):
        res1 = triangle.perimeter(3, 4, 5)
        res2 = triangle.perimeter(3, 5, 4)
        res3 = triangle.perimeter(4, 5, 3)

        self.assertEqual(res1, 12)
        self.assertEqual(res1, res2)
        self.assertEqual(res1, res3)

    def test_diff_existence(self):
        res = triangle.perimeter(5, 10, 15)

        self.assertEqual(res, -1)
