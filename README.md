# string_calculator_tdd
Implement a calculator that handles numbers inside a string and using Test-Driven-Development approach

# Steps
- create virtual environment
    python -m venv mycalcvenv
- Activate virtual environment 
    .\mycalcvenv\Scripts\Activate.ps1
- create requirements.txt with configuration
    pytest
- install pytest by running requirements.txt
    pip install -r requirements.txt
- Create test_string_calculator.py under ./tests
- Create pytest.ini and specify test folder
- Create string_calculator folder under the root folder and add __init__.py to import as module
- Create a calculator.py under string_calculator folder with an empty Calculator class
- Configure Python: Configure Tests in vscode

# TestCases
- handle empty string : function should return 0
- handle addition of one number: function should return number itself

