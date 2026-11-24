import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        target_dir_contents: list[str] = os.listdir(target_dir)
        target_dir_file_data: list[str] = []
        for item in target_dir_contents:
            file_path: str = os.path.normpath(os.path.join(target_dir, item))
            file_size: int = os.path.getsize(file_path)
            is_dir: bool = os.path.isdir(file_path)
            file_data = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            target_dir_file_data.append(file_data)
        return "\n".join(target_dir_file_data)
