import pytest
from string_calculator.calculator import Calculator

def test_add_empty_string():
    calc = Calculator()
    result = calc.add("")
    assert result == 0 

def test_add_one_number():
    calc = Calculator()
    result = calc.add("1")
    assert result == 1 