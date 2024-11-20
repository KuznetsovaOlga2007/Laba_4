import unittest
from calculate import calc
import circle
import square


class TestCalcFunction(unittest.TestCase):

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(5), 31.4)
        self.assertEqual(circle.perimeter(71), 446.1)
        self.assertEqual(circle.perimeter(1456), 9148.3)

    def test_circle_area(self):
        self.assertEqual(circle.area(5), 78.5)
        self.assertEqual(circle.area(100), 31415.9)
        self.assertEqual(circle.area(1230), 4752915.5)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(123), 492)
        self.assertEqual(square.perimeter(1140), 4560)

    def test_square_area(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(34), 1156)
        self.assertEqual(square.area(1156), 1336336)



    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'area', [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', [5, 10])

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [-5])


if __name__ == '__main__':
    unittest.main()