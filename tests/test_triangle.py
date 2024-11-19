import unittest
from triangle import area, perimeter
import math


class TestTriangle(unittest.TestCase):
    # Тесты на корректные значения для площади
    def test_triangle_area(self):
        # Arrange
        a, b, c = 3, 4, 5  # Прямоугольный треугольник

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, 6.0)

        # Arrange
        a, b, c = 7, 10, 5  # Произвольный треугольник

        # Act
        result = area(a, b, c)

        # Assert
        self.assertAlmostEqual(result, 16.24807680927192)

    # Тесты на корректные значения для периметра
    def test_triangle_perimeter(self):
        # Arrange
        a, b, c = 3, 4, 5  # Прямоугольный треугольник

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, 12)

        # Arrange
        a, b, c = 7, 10, 5  # Произвольный треугольник

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, 22)

    # Тесты для нулевых значений (ожидаем ValueError)
    def test_zero_sides(self):
        # Arrange
        a, b, c = 0, 4, 5

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    # Тесты для отрицательных значений (ожидаем ValueError)
    def test_negative_sides(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    # Тесты для невозможных треугольников (ожидаем ValueError)
    def test_invalid_triangle(self):
        # Arrange
        a, b, c = 1, 2, 3  # Не выполняется неравенство треугольника

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

        # Arrange
        a, b, c = 10, 1, 1  # Не выполняется неравенство треугольника

        # Act and Assert
        with self.assertRaises(ValueError):
            area(a, b, c)
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == '__main__':
    unittest.main()
