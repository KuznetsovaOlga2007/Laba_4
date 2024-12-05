import pytest
from geometric_lib.circle import area, perimeter

@pytest.mark.parametrize("radius, expected_area", [
    (1, pytest.approx(3.14159)),
    (2, pytest.approx(12.56637))
])
def test_circle_area(radius, expected_area):
    # Arrange
    actual_area = None

    # Act
    actual_area = area(radius)

    # Assert
    assert actual_area == expected_area

@pytest.mark.parametrize("radius, expected_perimeter", [
    (1, pytest.approx(6.28319)),
    (2, pytest.approx(12.56637))
])
def test_circle_perimeter(radius, expected_perimeter):
    # Arrange
    actual_perimeter = None

    # Act
    actual_perimeter = perimeter(radius)

    # Assert
    assert actual_perimeter == expected_perimeter