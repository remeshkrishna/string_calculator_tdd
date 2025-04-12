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

def test_invalid_character():
    calc=Calculator()
    with pytest.raises(ValueError) as error_info:
        calc.add("?")
    assert str(error_info.value)=="Invalid string provided"