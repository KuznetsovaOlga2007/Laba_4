import pytest
import math
from triangle import area, perimeter


class TestTriangle:
    def test_area(self):
        # Arrange
        a, b, c = 3, 4, 5
        s = (a + b + c) / 2
        expected = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Act
        result = area(a, b, c)

        # Assert
        assert math.isclose(result, expected), f"Exp {expected}, got {result}"

    def test_perimeter(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected = 12

        # Act
        result = perimeter(a, b, c)

        # Assert
        assert result == expected, f"Exp {expected}, got {result}"

    def test_negative_side_area(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            area(a, b, c)
        assert "must be positive" in str(exc_info.value)

    def test_negative_side_perimeter(self):
        # Arrange
        a, b, c = -3, 4, 5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            perimeter(a, b, c)
        assert "must be positive" in str(exc_info.value)

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
