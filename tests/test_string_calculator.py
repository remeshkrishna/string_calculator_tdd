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

def test_add_comma_seperated_numbers():
    calc=Calculator()
    result=calc.add("1,2,3")
    assert result==6

def test_add_newline_with_comma():
    calc=Calculator()
    result=calc.add("1\n2,3")
    assert result==6

def test_add_with_custom_delimiter():
    calc=Calculator()
    result=calc.add("//;\n1;2")
    assert result==3

def test_add_negative_numbers():
    calc=Calculator()
    with pytest.raises(Exception) as err_info:
        calc.add("-10,-5")
    assert str(err_info.value) == "negatives not allowed: -10,-5"

def test_add_faulty_custom_delimiter():
    calc=Calculator()
    with pytest.raises(ValueError) as error_info:
        calc.add("//;;\n1;;2")
    assert str(error_info.value) == "Invalid string provided"

def test_add_multiple_charater_delimiters():
    calc = Calculator()
    result = calc.add("//[***]\n1***2***3")
    assert result == 6