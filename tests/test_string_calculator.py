import pytest
from string_calculator.calculator import Calculator

def test_add_empty_string():
    calc = Calculator()
    result = calc.add("")
    assert result == 0 