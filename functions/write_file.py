import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:


        absolute_path_wd = os.path.abspath(working_directory) #determines abs path from relative path via os.path.abspath(dir) using the execution place as its starting point

        target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))

        valid_dir = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd

        if not valid_dir:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
           return f'Error: Cannot write to "{file_path}" as it is a directory'


        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"