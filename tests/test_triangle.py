import triangle


def test_triangle_area():
    # given
    a, b, c = 15, 20, 23

    # when
    result = triangle.area(a, b, c)

    # then
    assert result == 148.06755215103678


def test_triangle_perimeter():
    # given
    a, b, c = 15, 20, 23

    # when
    result = triangle.perimeter(a, b, c)

    # then
    assert result == 58
