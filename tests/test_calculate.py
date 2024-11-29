import pytest
import re
from calculate import calc  # Замените на имя вашего файла

# Проверка на ошибку, если переданы некорректные данные
@pytest.mark.parametrize("fig, func, size, exception, message", [
    ('circle', 'area', [0], ValueError, "Parameters must be positive numbers"),
    ('square', 'perimeter', [-1], ValueError, "Parameters must be positive numbers"),
    ('triangle', 'area', [3, 4], ValueError, "Wrong parameters. Expected 3,got 2"),
    ('square', 'area', ['a'], TypeError, "Parameters must be numbers"),
])
def test_invalid_calculations(fig, func, size, exception, message):
    with pytest.raises(exception) as excinfo:
        calc(fig, func, size)
    
    # Проверяем, что сообщение об ошибке содержит ожидаемую строку, игнорируя пробелы
    assert re.search(message, str(excinfo.value), re.DOTALL) is not None
