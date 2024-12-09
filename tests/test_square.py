from square import area, perimeter


def test_area():
    a = 4
    expected_area = a * a
    assert (
        area(a) == expected_area
    )


def test_perimeter():
    a = 4
    expected_perimeter = 4 * a
    assert (
        perimeter(a) == expected_perimeter
    )


def test_area_edge_case():
    a = 0  # Сторона квадрата равна 0
    assert area(a) == 0


def test_perimeter_edge_case():
    a = 0  # Сторона квадрата равна 0
    assert perimeter(a) == 0
