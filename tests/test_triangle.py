
import pytest
from triangle import perimeter


class TestTriangle:
    def test_invalid_sides_perimeter(self):
        a, b, c = 1, 2, 3
        with pytest.raises(ValueError) as exc_info:
            perimeter(a, b, c)
        assert (
            "The sum of any two sides must be greater than the third side."
            in str(exc_info.value)
        )
