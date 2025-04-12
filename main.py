import sys
from string_calculator.calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    if len(sys.argv) > 1:
        input_string = sys.argv[1].replace("\\n", "\n")
    else:
        input_string = input("Enter your string of numbers:\n")
    try:
        result = calc.add(input_string)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
