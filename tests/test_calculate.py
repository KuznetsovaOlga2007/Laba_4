import sys
import os
import pytest
from calculate import calc


sys.path.insert(0, os.path.abspath
(os.path.join(os.path.dirname(__file__), '../geometric_lib')))


def test_calc_circle_area():
    assert calc('circle', 'area', [3]) == pytest.approx(28.27, 0.01)


def test_calc_square_perimeter():
    assert calc('square', 'perimeter', [5]) == 20


def test_calc_triangle_area():
    assert calc('triangle', 'area', [3, 4, 5]) == 6


def test_calc_invalid_figure():
    with pytest.raises(AssertionError, match="Unknown figure: hexagon"):
        calc('hexagon', 'area', [5])


def test_calc_invalid_function():
    with pytest.raises(AssertionError, match="Unknown function: volume"):
        calc('circle', 'volume', [5])
