import pytest
from geometric_lib.square import area, perimeter

@pytest.mark.parametrize("side, expected_area", [
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_square_area(side, expected_area):
    # Arrange
    actual_area = None

    # Act
    actual_area = area(side)

    # Assert
    assert actual_area == expected_area

@pytest.mark.parametrize("side, expected_perimeter", [
    (1, 4),
    (2, 8),
    (3, 12)
])
def test_square_perimeter(side, expected_perimeter):
    # Arrange
    actual_perimeter = None

    # Act
    actual_perimeter = perimeter(side)

    # Assert
    assert actual_perimeter == expected_perimeter