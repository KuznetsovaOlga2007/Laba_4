from circle import area, perimeter
import pytest
import math


def test_circle_area():
    # Тест для корректного вычисления площади круга
    assert area(3) == pytest.approx(28.27, 0.01)
    assert area(0) == 0


def test_circle_perimeter():
    # Тест для корректного вычисления длины окружности
    assert perimeter(3) == pytest.approx(18.85, 0.01)
    assert perimeter(0) == 0
