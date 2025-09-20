# Playwright test automation

## Navigation
A list of all test cases is located in the `test-cases.txt` file in the root folder alongside with the `test_booked_dates.py` test file to check book date status. Tests to check valid data are placed in the `test_valid_data` folder. Tests to check invalid data are placed in the `test_invalid_data` folder. Files in the folders are named after test cases ids described in the "test-cases.txt".

## Run the tests
To run the tests, execute the following steps:
1. Install Python programming language from the [official page](https://www.python.org/downloads/).
2. Verify Python and pip version with the following commands:\
`python --version`\
`pip --version`
5. Create a Python virtual nvironment in the playwrght folder:\
`python -m venv env`
6. Activate the virtual environment with the following command (on Windows):\
`.\env\Scripts\activate`
7. Install Playwright and its pytest plugin using pip inside the activated virtual environment:\
`pip install pytest-playwright`
8. Install Playwright browsers:\
`playwright install`
9. Launch the files with `python file_name.py` from the terminal.


 
