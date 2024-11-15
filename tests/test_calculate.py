
import pytest
from calculate import calc


class TestCalc:
    def test_calc_invalid_figure(self):
        fig = "hexagon"
        func = "area"
        size = [6]
        with pytest.raises(ValueError) as exc_info:
            calc(fig, func, size)
        assert "Figure 'hexagon' is not supported." in str(exc_info.value)

    def test_calc_invalid_function(self):
        fig = "circle"
        func = "volume"
        size = [5]
        with pytest.raises(ValueError) as exc_info:
            calc(fig, func, size)
        assert "Function 'volume' is not supported." in str(exc_info.value)

    def test_calc_invalid_size(self):
        fig = "triangle"
        func = "area"
        size = [3, 4]
        with pytest.raises(TypeError) as exc_info:
            calc(fig, func, size)
        assert (
            "area() missing 1 required positional argument: 'c'"
            in str(exc_info.value)
        )
