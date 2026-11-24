import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites a file at a specified path",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write to, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "The string that will be written at the specified file path",
                }
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file: bool = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

    if os.path.isdir(target_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    else:
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
