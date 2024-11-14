from square import area, perimeter


def test_square_area():
    # Тест для корректного вычисления площади квадрата
    assert area(5) == 25
    assert area(0) == 0
    assert area(1) == 1


def test_square_perimeter():
    # Тест для корректного вычисления периметра квадрата
    assert perimeter(5) == 20
    assert perimeter(0) == 0
    assert perimeter(1) == 4
