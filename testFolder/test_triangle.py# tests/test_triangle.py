# tests/test_triangle.py

import pytest
import math
from triangle import area, perimeter


class TestTriangle:
    def test_area(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected = math.sqrt((6) * (6 - 3) * (6 - 4) * (6 - 5))  # s = 6

        # Act
        result = area(a, b, c)

        # Assert
        assert math.isclose(result, expected), f"Expected area {expected}, got {result}"

    def test_perimeter(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected = 12

        # Act
        result = perimeter(a, b, c)

        # Assert
        assert result == expected, f"Expected perimeter {expected}, got {result}"

    def test_negative_side_area(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            area(a, b, c)
        assert "positive" in str(exc_info.value)

    def test_negative_side_perimeter(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            perimeter(a, b, c)
        assert "positive" in str(exc_info.value)

    def test_invalid_sides_area(self):
        # Arrange
        a, b, c = 1, 2, 3  # Не удовлетворяет неравенству треугольника

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            area(a, b, c)
        assert "sum of any two sides" in str(exc_info.value)

    def test_invalid_sides_perimeter(self):
        # Arrange
        a, b, c = 1, 2, 3  # Не удовлетворяет неравенству треугольника

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            perimeter(a, b, c)
        assert "sum of any two sides" in str(exc_info.value)
