import unittest
import circle
import square
from calculate import calc

class TestCalc(unittest.TestCase):

    def test_circle_perimeter(self):
        result = calc('circle', 'perimeter', [5])
        self.assertAlmostEqual(result, 31.41592653589793)

    def test_circle_area(self):
        result = calc('circle', 'area', [5])
        self.assertAlmostEqual(result, 78.53981633974483)

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [5])
        self.assertEqual(result, 20)

    def test_square_area(self):
        result = calc('square', 'area', [5])
        self.assertEqual(result, 25)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'perimeter', [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc('circle', 'perimeter', [5, 10])

if __name__ == '__main__':
    unittest.main()