from triangle import area, perimeter


def test_area():
    a, b, c = 3, 4, 5
    expected_area = (a + b + c) / 2
    assert (
        area(a, b, c) == expected_area
    )


def test_perimeter():
    a, b, c = 3, 4, 5
    expected_perimeter = a + b + c
    assert (
        perimeter(a, b, c) == expected_perimeter
    )


def test_area_edge_case():
    a, b, c = 0, 0, 0
    assert area(a, b, c) == 0


def test_perimeter_edge_case():
    a, b, c = 0, 0, 0
    assert (
        perimeter(a, b, c) == 0
    )
