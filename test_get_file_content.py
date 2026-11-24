import os
from functions.get_file_content import get_file_content
from config import *

tests = [("calculator", "lorem.txt"), ("calculator", "main.py"), ("calculator","pkg/calculator.py"), ("calculator","/bin/cat"), ("calculator", "pkg/does_not_exist.py")]

def test_get_file_contents(*args):
    for test in tests:
        target_file = test[1]
        result = get_file_content("calculator", target_file)
        if result.startswith("Error:"):
            print(result)
        else:
            if not ('truncated' in result):
                print(result)
            print(f"{target_file} length: {len(result)}")
            print(f"{target_file} truncated: {'truncated' in result}")


test_get_file_contents(tests)
