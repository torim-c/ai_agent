import os
from config import *

def get_file_content(working_directory: str, file_path: str) -> str:
    try:


        absolute_path_wd = os.path.abspath(working_directory) #determines abs path from relative path via os.path.abspath(dir) using the execution place as its starting point

        target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))

        valid_dir = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd

        if not valid_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
            
        else:
            try:
                file_content_string = ""
                with open(target_file, "r") as f:
                    file_content_string = f.read(char_limit)
                    if f.read(1):
                        file_content_string += f'[...File "{file_path}" truncated at {char_limit} characters]'
                return file_content_string
            except Exception as e:
                return f"Error: {e}"


    except Exception as e:
        return f"Error: {e}"