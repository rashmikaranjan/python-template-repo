import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add1(calculator):
    assert calculator.add(1, 2) == 3

def test_add2(calculator):
    assert calculator.add(-1, 2) == 1

def test_add3(calculator):
    assert calculator.add(1, 0) == 1

def test_subtract1(calculator):
    assert calculator.subtract(10, 3) == 7

def test_subtract2(calculator):
    assert calculator.subtract(10, -3) == 13

def test_subtract3(calculator):
    assert calculator.subtract(-10, 3) == -13

def test_multiply1(calculator):
    assert calculator.multiply(3, 3) == 9

def test_multiply2(calculator):
    assert calculator.multiply(3, -3) == -9

def test_multiply3(calculator):
    assert calculator.multiply(-3, -3) == 9

def test_divide1(calculator):
    assert calculator.divide(10, 2) == 5

def test_divide2(calculator):
    assert calculator.divide(10, -2) == -5

def test_divide3(calculator):
    assert calculator.divide(-10, -2) == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(6, 0)
