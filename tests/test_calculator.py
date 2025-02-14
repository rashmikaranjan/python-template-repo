"""Unit tests for Calculator module."""

import pytest

from src.calculator import Calculator

# Constants for testing
TWO = 2
THREE = 3
FIVE = 5
SIX = 6

@pytest.fixture
def calculator() -> Calculator:
    """Fixture to create a Calculator instance."""
    return Calculator()

def test_add(calculator: Calculator) -> None:
    """Test addition of two numbers."""
    assert calculator.add(TWO, THREE) == FIVE

def test_subtract(calculator: Calculator) -> None:
    """Test subtraction of two numbers."""
    assert calculator.subtract(FIVE, THREE) == TWO

def test_multiply(calculator: Calculator) -> None:
    """Test multiplication of two numbers."""
    assert calculator.multiply(TWO, THREE) == SIX
