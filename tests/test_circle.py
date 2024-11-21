import math

import circle


def test_circle_area():
    # given
    r = 15

    # when
    result = circle.area(r)

    # then
    assert result == math.pi * r * r;


def test_circle_perimeter():
    # given
    r = 15
    # when
    result = circle.perimeter(r)
    # then
    assert result == 2 * math.pi * r;
