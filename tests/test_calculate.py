import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculate import (
    area_circle, perimeter_circle,
    area_square, perimeter_square,
    area_triangle, perimeter_triangle,
    calc
)

# Тесты для круга
def test_area_circle():
    assert area_circle(1) == pytest.approx(3.14159, 0.0001)
    assert area_circle(0) == 0
    assert area_circle(2) == pytest.approx(12.56637, 0.0001)


def test_perimeter_circle():
    assert perimeter_circle(1) == pytest.approx(6.28318, 0.0001)
    assert perimeter_circle(0) == 0
    assert perimeter_circle(2) == pytest.approx(12.56637, 0.0001)

# Тесты для квадрата
def test_area_square():
    assert area_square(2) == 4
    assert area_square(0) == 0
    assert area_square(5) == 25


def test_perimeter_square():
    assert perimeter_square(2) == 8
    assert perimeter_square(0) == 0
    assert perimeter_square(5) == 20

# Тесты для треугольника
def test_area_triangle():
    assert area_triangle(3, 4, 5) == pytest.approx(6, 0.0001)
    assert area_triangle(6, 8, 10) == pytest.approx(24, 0.0001)


def test_perimeter_triangle():
    assert perimeter_triangle(3, 4, 5) == 12
    assert perimeter_triangle(6, 8, 10) == 24

# Тесты для функции calc
def test_calc_circle():
    result = calc("circle", 1)
    assert result["area"] == pytest.approx(3.14159, 0.0001)
    assert result["perimeter"] == pytest.approx(6.28318, 0.0001)


def test_calc_square():
    result = calc("square", 4)
    assert result["area"] == 16
    assert result["perimeter"] == 16


def test_calc_triangle():
    result = calc("triangle", 3, 4, 5)
    assert result["area"] == pytest.approx(6, 0.0001)
    assert result["perimeter"] == 12


def test_calc_invalid_args():
    with pytest.raises(ValueError):
        calc("circle", 1, 2)
    with pytest.raises(ValueError):
        calc("triangle", 1, 2)
    with pytest.raises(ValueError):
        calc("unknown_shape", 1)
