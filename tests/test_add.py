import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -4) == -6

def test_add_zero():
    assert add(0, 7) == 7
    assert add(7, 0) == 7

def test_add_mixed_signs():
    assert add(-3, 7) == 4
    assert add(10, -5) == 5

def test_add_large_numbers():
    assert add(10**8, 10**8) == 2 * 10**8
