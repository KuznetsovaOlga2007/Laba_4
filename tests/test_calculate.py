# tests/test_calculate.py
import pytest
from calculate import calc

# Тест для некорректной фигуры
def test_invalid_figure():
    with pytest.raises(ValueError):
        calc('triangle', 'area', [3])  # Нужно передать 3 стороны для треугольника

# Тест для некорректного количества параметров для круга
def test_invalid_size_circle():
    with pytest.raises(ValueError):
        calc('circle', 'area', [1, 2])  # Ошибка: Круг требует только 1 параметр (радиус)

# Тест для некорректного количества параметров для квадрата
def test_invalid_size_square():
    with pytest.raises(ValueError):
        calc('square', 'area', [1, 2])  # Ошибка: Квадрат требует только 1 параметр (сторона)

# Тест для некорректного количества параметров для треугольника (площадь)
# Тест для некорректного количества параметров для треугольника (площадь)
def test_invalid_size_triangle_area():
    with pytest.raises(ValueError):
        calc('triangle', 'area', [3])  # Ошибка: нужно передать 3 стороны для треугольника
  # Нужно передать 3 стороны для треугольника

# Тест для некорректного количества параметров для треугольника (периметр)
def test_invalid_size_triangle_perimeter():
    with pytest.raises(ValueError):
        calc('triangle', 'perimeter', [3])  # Нужно передать 3 стороны для периметра

# Тест для неправильной функции
# Тест для неправильной функции
def test_invalid_function():
    with pytest.raises(ValueError):
        calc('circle', 'volume', [3])  # Ошибка, так как функции "volume" нет для круга
