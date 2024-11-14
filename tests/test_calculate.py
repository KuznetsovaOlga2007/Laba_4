from geometric_lib.calculate import calc
import pytest


def test_calc_circle_area():
    # Проверка вычисления площади круга
    assert calc('circle', 'area', [3]) == pytest.approx(28.27, 0.01)


def test_calc_square_perimeter():
    # Проверка вычисления периметра квадрата
    assert calc('square', 'perimeter', [5]) == 20


def test_calc_triangle_area():
    # Проверка вычисления площади треугольника
    assert calc('triangle', 'area', [3, 4, 5]) == 6


def test_calc_invalid_figure():
    # Проверка, что некорректная фигура вызывает AssertionError
    with pytest.raises(AssertionError, match="Unknown figure: hexagon"):
        calc('hexagon', 'area', [5])


def test_calc_invalid_function():
    # Проверка, что некорректная функция вызывает AssertionError
    with pytest.raises(AssertionError, match="Unknown function: volume"):
        calc('circle', 'volume', [5])
