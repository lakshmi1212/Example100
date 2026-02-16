import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a,b,expected", [
    (2, 1, 1),
    (1, -1, 2),
    (0, 0, 0),
    (200, 100, 100),
    (-7, -5, -2),
    (5.5, 2.5, 3.0),
    (1e10, 1e10, 0)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 1)
