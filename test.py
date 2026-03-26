def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



# 

import pytest
from calculator import add, subtract, multiply, divide

# ─── ADD ───────────────────────────────────────────
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -4) == -5

def test_add_zero():
    assert add(0, 5) == 5

# ─── SUBTRACT ──────────────────────────────────────
def test_subtract_positive():
    assert subtract(5, 3) == 2

def test_subtract_negative():
    assert subtract(3, 5) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

# ─── MULTIPLY ──────────────────────────────────────
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(5, 0) == 0

# ─── DIVIDE ────────────────────────────────────────
def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_negative():
    assert divide(-9, 3) == -3.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)