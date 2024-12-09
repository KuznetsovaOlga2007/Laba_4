import pytest
import math

from circle import area, perimeter


def test_area():
    # Пример радиуса
    r = 3
    expected_area = math.pi * r * r
    assert area(r) == pytest.approx(
        expected_area, rel=1e-9
    )


def test_perimeter():
    r = 3
    expected_perimeter = 2 * math.pi * r
    assert perimeter(r) == pytest.approx(
        expected_perimeter, rel=1e-9
    )


def test_area_edge_case():
    r = 0  # Радиус равен 0
    assert area(r) == 0


def test_perimeter_edge_case():
    r = 0  # Радиус равен 0
    assert perimeter(r) == 0
