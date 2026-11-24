import os
from functions.run_python_file import run_python_file

tests = [("calculator", "main.py"), ("calculator", "main.py", ["3 + 5"]), ("calculator", "tests.py"), ("calculator", "../main.py"), ("calculator", "nonexistent.py"), ("calculator", "lorem.txt")]

def test_run_python_file(*args):
    for test in tests:
        result = run_python_file(*test)
        print(result)

test_run_python_file(tests)
