import unittest

from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_sq_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_sq_area(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_sq_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_sq_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_sq_area_neg(self):
        res = area(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_sq_perimeter_neg(self):
        res = perimeter(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_large_area(self):
        res = area(29813745390)
        self.assertEqual(res, 888859414179746252100)

    def test_large_perimetr(self):
        res = perimeter(973165903242)
        self.assertEqual(res, 3892663612968)


if __name__ == '__main__':
    unittest.main()