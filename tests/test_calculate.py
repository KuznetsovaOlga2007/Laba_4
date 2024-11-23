import pytest
from calculate import calc

def test_calc_circle_area():
    assert round(calc('circle', 'area', [3]), 3) == 28.274

def test_calc_circle_perimeter():
    assert round(calc('circle', 'perimeter', [3]), 3) == 18.850

def test_calc_square_area():
    assert calc('square', 'area', [4]) == 16

def test_calc_square_perimeter():
    assert calc('square', 'perimeter', [4]) == 16

def test_invalid_figure():
    with pytest.raises(ValueError, match="Invalid figure 'triangle'"):
        calc('triangle', 'area', [3])

def test_invalid_function():
    with pytest.raises(ValueError, match="Invalid function 'volume'"):
        calc('circle', 'volume', [3])

def test_incorrect_size_count():
    with pytest.raises(ValueError, match="Incorrect number of parameters for circle"):
        calc('circle', 'area', [3, 4])

def test_non_numeric_size():
    with pytest.raises(TypeError):
        calc('square', 'area', ['side'])
