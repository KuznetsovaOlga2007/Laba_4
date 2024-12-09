import pytest
from calculate import calc


def test_calc_circle_area():
    # Arrange
    fig = "circle"
    func = "area"
    size = [3]  # Радиус круга

    # Act
    result = calc(fig, func, size)

    # Assert
    assert pytest.approx(result, 0.01) == 28.27


def test_calc_square_perimeter():
    # Arrange
    fig = "square"
    func = "perimeter"
    size = [4]  # Сторона квадрата

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == 16


# Тесты для некорректных данных
def test_calc_invalid_figure():
    # Arrange
    fig = "triangle"
    func = "area"
    size = [3]

    # Act and Assert
    with pytest.raises(AssertionError, match="Unknown figure: triangle"):
        calc(fig, func, size)


def test_calc_invalid_function():
    # Arrange
    fig = "circle"
    func = "volume"
    size = [3]

    # Act and Assert
    with pytest.raises(AssertionError, match="Unknown function: volume"):
        calc(fig, func, size)


def test_calc_invalid_size_count():
    # Arrange
    fig = "square"
    func = "area"
    size = [4, 5]  # Лишний аргумент

    # Act and Assert
    with pytest.raises(AssertionError, match="Invalid size"):
        calc(fig, func, size)
