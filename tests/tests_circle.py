import unittest

from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_circ_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_circ_area(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_circ_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_circ_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_circ_area_neg(self):
        res = area(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_circ_perimeter_neg(self):
        res = perimeter(-1)
        self.assertEqual(res, "Wrong input parameters")

    def test_small_perimetr(self):
        res = perimeter(20)
        self.assertEqual(res, 125.66370614359172)


if __name__ == '__main__':
    unittest.main()