from geometric_lib.triangle import area, perimeter
import pytest


def test_triangle_area():
    # Тест для корректного вычисления площади треугольника
    assert area(3, 4, 5) == 6
    assert area(5, 5, 6) == pytest.approx(12, 0.1)


def test_triangle_perimeter():
    # Тест для корректного вычисления периметра треугольника
    assert perimeter(3, 4, 5) == 12
    assert perimeter(5, 5, 6) == 16
