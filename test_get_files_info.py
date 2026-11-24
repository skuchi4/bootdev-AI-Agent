import os
from functions.get_files_info import get_files_info

tests = [("calculator", "."), ("calculator","pkg"), ("calculator","/bin"), ("calculator", "../")]

def test_get_files_info(*args):
    for test in tests:
        target_dir = test[1]
        if target_dir == ".":
            target_dir = "current"
        else:
            target_dir = f"\'{target_dir}\'"
        print(f"Result for {target_dir} directory:")
        print(get_files_info(*test))


test_get_files_info(tests)
