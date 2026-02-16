import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7

def test_subtract_negative_numbers():
    assert subtract(-5, -2) == -3

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_mixed_signs():
    assert subtract(-3, 7) == -10
    assert subtract(10, -5) == 15

def test_subtract_large_numbers():
    assert subtract(10**8, 10**7) == 9 * 10**7
