import os, subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs the python file at a specified file path, with optional arguments to feed into the function at that path",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the python file that should be executed, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "Optional: A list of string(s) or None. The default value is None.",
                    "description": "If a list of string(s) is provided, it contains the argument(s) that will be used in the specified function",
                }
            },
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file: bool = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs

    if not os.path.isfile(target_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    else:
        try:
            command = ["python", target_file_path]
            if args is not None:
                command.extend(args)
            completed_process = subprocess.run(command, capture_output=True, timeout=30.0, text=True)
            output: str = ""
            if completed_process.returncode != 0:
                output = output + f"Process exited with code {completed_process.returncode}"
            if completed_process.stdout == "" and completed_process.stderr == "":
                output = output + "No output produced"
            else:
                output = output + f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
            return output
        except Exception as e:
            return f"Error: executing Python file: {e}"
