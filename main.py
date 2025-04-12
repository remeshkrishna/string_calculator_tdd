from string_calculator.calculator import Calculator

if __name__ == "__main__":
    calc = Calculator()
    input_string = input("Enter your string of numbers: ")
    try:
        result = calc.add(input_string)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
