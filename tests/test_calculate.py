import unittest
from main import calc


class TestCalculate(unittest.TestCase):
    def test_valid_square_area(self):
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_valid_square_perimeter(self):
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_valid_circle_area(self):
        self.assertAlmostEqual(calc("circle", "area", [3]), 28.274333882308138)

    def test_valid_circle_perimeter(self):
        self.assertAlmostEqual(calc("circle", "perimeter", [3]), 18.84955592153876)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc("triangle", "area", [3])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc("circle", "volume", [3])

    def test_invalid_size_length_square(self):
        with self.assertRaises(ValueError):
            calc("square", "area", [4, 5])

    def test_invalid_size_length_circle(self):
        with self.assertRaises(ValueError):
            calc("circle", "perimeter", [3, 5])

    def test_negative_size_square(self):
        with self.assertRaises(ValueError):
            calc("square", "area", [-4])

    def test_zero_size_square(self):
        with self.assertRaises(ValueError):
            calc("square", "perimeter", [0])

    def test_negative_size_circle(self):
        with self.assertRaises(ValueError):
            calc("circle", "area", [-3])

    def test_zero_size_circle(self):
        with self.assertRaises(ValueError):
            calc("circle", "perimeter", [0])


if __name__ == "__main__":
    unittest.main()
