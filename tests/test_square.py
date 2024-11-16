import pytest
from square import area, perimeter


def test_area():
    result = area(3)
    expected_result = 3 ** 2
    assert result == expected_result


def test_perimeter():
    result = perimeter(3)
    expected_result = 3 * 4
    assert result == expected_result


def test_area_invalid():
    with pytest.raises(TypeError):
        area("three")


def test_invalid_size_area():
    with pytest.raises(TypeError):
        area(1, 52)

        
def test_invalid_size_perimeter():
    with pytest.raises(TypeError):
        perimeter(1, 52)
