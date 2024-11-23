import pytest
from calculate import calc

# Позитивные тесты
def test_circle_area():
    """Проверка расчёта площади круга."""
    result = calc('circle', 'area', [3])
    assert pytest.approx(result, 0.01) == 28.27  # π * r^2

def test_circle_perimeter():
    """Проверка расчёта периметра круга."""
    result = calc('circle', 'perimeter', [3])
    assert pytest.approx(result, 0.01) == 18.85  # 2 * π * r

# Негативные тесты
def test_incorrect_size_count_circle():
    """Проверка обработки некорректного количества параметров для круга."""
    with pytest.raises(ValueError, match="Incorrect number of parameters for circle."):
        calc('circle', 'area', [3, 4])

def test_non_numeric_size_circle():
    """Проверка обработки нечислового параметра для круга."""
    with pytest.raises(TypeError, match="All size parameters must be numbers."):
        calc('circle', 'area', ['radius'])
