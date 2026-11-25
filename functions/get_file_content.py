import os, io
from config import *

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns a string containing the text of the file at a specified file path, up to a character limit of 10,000",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to return the string from, relative to the working directory (default is the working directory itself)",
                },
            },
            "required": ["file_path"],
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file: bool = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    else:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string
