import pytest
from calculate import calc

# Позитивные тесты


def test_triangle_area():
    """Проверка расчёта площади треугольника."""
    result = calc(
        'triangle', 'area', [
            3, 4, 5])  # предполагается, что площадь по трём сторонам
    assert pytest.approx(result, 0.01) == 6  # по формуле Герона


def test_triangle_perimeter():
    """Проверка расчёта периметра треугольника."""
    result = calc('triangle', 'perimeter', [3, 4, 5])
    assert result == 12  # сумма сторон

# Негативные тесты


def test_incorrect_size_count_triangle():
    """Проверка некорректного количества параметров."""
    with pytest.raises(ValueError, match="Incorrect parameters for triangle. Expected 3, got 2."):
        calc('triangle', 'area', [3, 4])  # не хватает третьей стороны
	


def test_non_numeric_size_triangle():
    """Проверка обработки нечислового параметра для треугольника."""
    with pytest.raises(TypeError, match="Parameters must be numbers."):
        calc('triangle', 'area', ['side1', 'side2', 'side3'])
