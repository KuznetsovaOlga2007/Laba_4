import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):

    # Положительные тесты для площади квадрата
    def test_square_area(self):
        # Arrange
        side = 4
        expected_area = side * side  # 4 * 4 = 16
        
        # Act
        result = area(side)
        
        # Assert
        self.assertEqual(result, expected_area)

        # Arrange
        side = 5
        expected_area = side * side  # 5 * 5 = 25
        
        # Act
        result = area(side)
        
        # Assert
        self.assertEqual(result, expected_area)

    # Положительные тесты для периметра квадрата
    def test_square_perimeter(self):
        # Arrange
        side = 4
        expected_perimeter = 4 * side  # 4 * 4 = 16
        
        # Act
        result = perimeter(side)
        
        # Assert
        self.assertEqual(result, expected_perimeter)

        # Arrange
        side = 5
        expected_perimeter = 4 * side  # 4 * 5 = 20
        
        # Act
        result = perimeter(side)
        
        # Assert
        self.assertEqual(result, expected_perimeter)

    # Тест для нулевого значения (ожидаем ValueError)
    def test_zero_square(self):
        # Arrange
        side = 0
        
        # Act and Assert
        with self.assertRaises(ValueError):
            area(side)
        with self.assertRaises(ValueError):
            perimeter(side)

    # Негативные тесты для отрицательного значения (ожидаем ValueError)
    def test_negative_square(self):
        # Arrange
        side = -4
        
        # Act and Assert
        with self.assertRaises(ValueError):
            area(side)
        with self.assertRaises(ValueError):
            perimeter(side)

if __name__ == '__main__':
    unittest.main()
