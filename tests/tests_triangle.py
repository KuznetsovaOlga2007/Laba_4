import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(6, 8, 10), 24)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 4, 5), 0)
        self.assertEqual(area(3, 0, 5), 0)
        self.assertEqual(area(3, 4, 0), 0)

    def test_area_negative_sides(self):
        self.assertEqual(area(-3, 4, 5), 0)
        self.assertEqual(area(3, -4, 5), 0)
        self.assertEqual(area(3, 4, -5), 0)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(6, 8, 10), 24)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(3, 0, 5), 8)
        self.assertEqual(perimeter(3, 4, 0), 7)

    def test_perimeter_negative_sides(self):
        self.assertEqual(perimeter(-3, 4, 5), 6)
        self.assertEqual(perimeter(3, -4, 5), 4)
        self.assertEqual(perimeter(3, 4, -5), 2)

if __name__ == '__main__':
    unittest.main()
