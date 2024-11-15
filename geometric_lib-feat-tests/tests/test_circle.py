import pytest
import math
from circle import area, perimeter


class TestCircle:
    def test_circle_area_positive_radius(self):
        # Arrange
        radius = 5
        expected = math.pi * radius**2

        # Act
        result = area(radius)

        # Assert
        assert result == pytest.approx(
            expected
        ), f"Expected area {expected}, got {result}"

    def test_circle_perimeter_positive_radius(self):
        # Arrange
        radius = 5
        expected = 2 * math.pi * radius

        # Act
        result = perimeter(radius)

        # Assert
        assert result == pytest.approx(
            expected
        ), f"Expected perimeter {expected}, got {result}"

    def test_circle_area_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            area(radius)
        assert "must be positive" in str(exc_info.value)

    def test_circle_perimeter_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            perimeter(radius)
        assert "must be positive" in str(exc_info.value)
