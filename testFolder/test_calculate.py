
import pytest
from calculate import calc

class TestCalc:
    def test_calc_with_positive_numbers(self):
        # Arrange
        args = (1, 2, 3)
        expected = 6

        # Act
        result = calc(*args)

        # Assert
        assert result == expected, f"Expected {expected}, got {result}"

    def test_calc_with_no_arguments(self):
        # Arrange & Act & Assert
        with pytest.raises(ValueError) as exc_info:
            calc()
        assert "No arguments provided" in str(exc_info.value)

    def test_calc_with_negative_numbers(self):
        # Arrange
        args = (-1, -2, -3)
        expected = -6

        # Act
        result = calc(*args)

        # Assert
        assert result == expected, f"Expected {expected}, got {result}"

    def test_calc_with_non_numeric_input(self):
        # Arrange
        args = (1, 'a', 3)

        # Act & Assert
        with pytest.raises(TypeError) as exc_info:
            calc(*args)
        assert "numbers" in str(exc_info.value)
