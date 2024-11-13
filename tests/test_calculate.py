import unittest
from calculate import calc, figs, funcs, sizes

class TestCalcFunction(unittest.TestCase):

    def test_circle_perimeter(self):
        result = calc('circle', 'perimeter', [5])
        self.assertAlmostEqual(result, 31.4159, places=4)  # Периферия круга = 2 * π * r

    def test_circle_area(self):
        result = calc('circle', 'area', [5])
        self.assertAlmostEqual(result, 78.5398, places=4)  # Площадь круга = π * r^2

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', [4])
        self.assertEqual(result, 16)  # Периметр квадрата = 4 * a

    def test_square_area(self):
        result = calc('square', 'area', [4])
        self.assertEqual(result, 16)  # Площадь квадрата = a^2

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'perimeter', [5])  # Некорректная фигура

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])  # Некорректная функция

    def test_invalid_arguments_count(self):
        with self.assertRaises(TypeError):
            calc('circle', 'perimeter', [5, 10])  # Избыточное количество аргументов

        with self.assertRaises(TypeError):
            calc('square', 'area', [])  # Недостаточное количество аргументов

if __name__ == '__main__':
    unittest.main()
