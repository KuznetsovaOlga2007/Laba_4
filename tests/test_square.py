import pytest
from square import area, perimeter


class TestSquare:
    def test_square_area_positive_side(self):
        # Arrange
        side = 4
        expected = 4 * 4  # a^2

        # Act
        result = area(side)

        # Assert
        assert result == expected, f"Expected area {expected}, got {result}"

    def test_square_perimeter_positive_side(self):
        # Arrange
        side = 4
        expected = 4 * 4  # 4a

        # Act
        result = perimeter(side)

        # Assert
        assert result == expected, f"Expected  {expected}, got {result}"

    def test_square_area_negative_side(self):
        # Arrange
        side = -4

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            area(side)
        assert "must be positive" in str(exc_info.value)

    def test_square_perimeter_negative_side(self):
        # Arrange
        side = -4

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            perimeter(side)
        assert "must be positive" in str(exc_info.value)
