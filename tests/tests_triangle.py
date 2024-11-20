import unittest

from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    def test_tri_area_zero_side(self):
        res = area(0, 10)
        self.assertEqual(res, 0.0)

    def test_tri_area_zero_height(self):
        res = area(10, 0)
        self.assertEqual(res, 0.0)

    def test_tri_perimeter_zero_sides(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_tri_area_neg_side(self):
        res = area(-3, 9)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_area_neg_height(self):
        res = area(9, -7)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_perimeter_neg_all_sides(self):
        res = perimeter(-3, -4, -5)
        self.assertEqual(res, "Wrong input parameters")

    def test_tri_area_no_existance(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, "Wrong input parameters")

    def test_large_area(self):
        res = area(5879324522, 134513256136)
        self.assertEqual(res, 395423542667225858048)

    def test_large_perimetr(self):
        res = perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res, 5818856535136027)

    def test_small_perimetr(self):
        res = perimeter(1, 1, 34)
        self.assertEqual(res, 36)


if __name__ == '__main__':
    unittest.main()