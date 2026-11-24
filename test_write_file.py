import os
from functions.write_file import write_file

tests = [("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), ("calculator","/tmp/temp.txt", "this should not be allowed")]

def test_write_file(*args):
    for test in tests:
        working_directory = test[0]
        file_path = test[1]
        file_content = test[2]
        result = write_file(working_directory, file_path, file_content)
        print(result)

test_write_file(tests)
