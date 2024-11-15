import pytest
from calculate import calc


class TestCalc:
    def test_calc_perimeter_circle(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [5]
        expected = 2 * 3.141592653589793 * 5  # 2πr

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == pytest.approx(
            expected
        ), f"Expected perimeter {expected}, got {result}"

    def test_calc_area_circle(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [5]
        expected = 3.141592653589793 * 5 * 5  # πr²

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == pytest.approx(
            expected
        ), f"Expected area {expected}, got {result}"

    def test_calc_perimeter_square(self):
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [4]
        expected = 4 * 4  # 4a

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == expected, f"Expected {expected}, got {result}"

    def test_calc_area_square(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [4]
        expected = 4 * 4  # a²

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == expected, f"Expected area {expected}, got {result}"

    def test_calc_perimeter_triangle(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]
        expected = 3 + 4 + 5  # a + b + c

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == expected, f"Expected  {expected}, got {result}"

    def test_calc_area_triangle(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        s = (3 + 4 + 5) / 2
        expected = (s * (s - 3) * (s - 4) * (s - 5)) ** 0.5

        # Act
        result = calc(fig, func, size)

        # Assert
        assert result == pytest.approx(
            expected
        ), f"Expected area {expected}, got {result}"

    def test_calc_invalid_figure(self):
        # Arrange
        fig = "hexagon"
        func = "area"
        size = [6]

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            calc(fig, func, size)
        assert "Figure 'hexagon' is not supported." in str(exc_info.value)

    def test_calc_invalid_function(self):
        # Arrange
        fig = "circle"
        func = "volume"
        size = [5]

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            calc(fig, func, size)
        assert "Function 'volume' is not supported." in str(exc_info.value)

    def test_calc_invalid_size(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4]  # Insufficient arguments

        # Act & Assert
        with pytest.raises(TypeError) as exc_info:
            calc(fig, func, size)
        assert "area() missing 1 argument" in str(exc_info.value)
