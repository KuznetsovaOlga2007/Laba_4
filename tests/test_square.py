import square


def test_square_area():
    # given
    a = 125

    # when
    result = square.area(a)

    # then
    assert result == 125 ** 2;


def test_square_perimeter():
    # given
    a = 125

    # when
    result = square.perimeter(a)

    # then
    assert result == 125 * 4
