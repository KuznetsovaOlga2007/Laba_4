import pytest
from calculate import calc

# Позитивные тесты


def test_square_area():
    """Проверка расчёта площади квадрата."""
    result = calc('square', 'area', [4])
    assert result == 16  # side^2


def test_square_perimeter():
    """Проверка расчёта периметра квадрата."""
    result = calc('square', 'perimeter', [4])
    assert result == 16  # 4 * side

# Негативные тесты


def test_incorrect_size_count_square():
    """Проверка обработки некорректного количества параметров для квадрата."""
    with pytest.raises(ValueError, match="Wrong parameters."):
        calc('square', 'perimeter', [])


def test_non_numeric_size_square():
    """Проверка обработки нечислового параметра для квадрата."""
    with pytest.raises(TypeError, match="Parameters must be numbers."):
        calc('square', 'area', ['side'])
