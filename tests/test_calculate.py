import unittest
import circle
import square

class TestCalculate(unittest.TestCase):
    def test_valid_square_area(self):
        # Проверка корректного вычисления площади квадрата
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_valid_square_perimeter(self):
        # Проверка корректного вычисления периметра квадрата
        self.assertEqual(calc("square", "perimeter", [4]), 16)

    def test_valid_circle_area(self):
        # Проверка корректного вычисления площади круга
        self.assertAlmostEqual(calc("circle", "area", [3]), 28.274333882308138)

    def test_valid_circle_perimeter(self):
        # Проверка корректного вычисления периметра круга
        self.assertAlmostEqual(calc("circle", "perimeter", [3]), 18.84955592153876)

    def test_invalid_figure(self):
        # Проверка некорректной фигуры
        with self.assertRaises(AssertionError):
            calc("triangle", "area", [3])

    def test_invalid_function(self):
        # Проверка некорректной функции
        with self.assertRaises(AssertionError):
            calc("circle", "volume", [3])

    def test_invalid_size_length_square(self):
        # Проверка некорректного числа параметров для квадрата
        with self.assertRaises(ValueError):
            calc("square", "area", [4, 5])

    def test_invalid_size_length_circle(self):
        # Проверка некорректного числа параметров для круга
        with self.assertRaises(ValueError):
            calc("circle", "perimeter", [3, 5])


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
