import os



def get_files_info(working_directory: str, directory: str = ".") -> str:



    absolute_path_wd = os.path.abspath(working_directory)

    target_dir = os.path.normpath(os.path.join(absolute_path_wd, directory))

    valid_dir = os.path.commonpath([absolute_path_wd, target_dir]) == absolute_path_wd

    if not valid_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    else:
        return f'Success: "{directory}" is within the working directory'
    