import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    absolute_path_wd = os.path.abspath(working_directory) #determines abs path from relative path via os.path.abspath(dir) using the execution place as its starting point
    
    target_file = os.path.normpath(os.path.join(absolute_path_wd, file_path))
    
    valid_dir = os.path.commonpath([absolute_path_wd, target_file]) == absolute_path_wd #attributes bool value true if target_file common path /w abs_path the same as abspath
                                                                                        #serves to help check if the target is within the working directory path
    
    if not valid_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file):
        return f'Error: Cannot execute to "{file_path}" as it is a directory'

    if not os.path.isfile(target_file): #accidentally wrote working_directory instead, which resulted in pkg not opening in test/always check filepaths
        return f'"{file_path}" does not exist or is not a regular file'

    if not target_file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]

    if args:
        command.extend(args)

    process_var =  subprocess.run(command, capture_output = True, text=True, check = True, cwd = absolute_path_wd, timeout = 30)

    exit_code = process_var.returncode

    exit_string = ""

    if exit_code != 0:
        exit_string += f"Process exited with code {exit_code}\n"
    if process_var.stdout == "" and process_var.stderr == "":
        exit_string += "No output produced\n"
    else:
        if process_var.stdout != "":
            exit_string += f"STDOUT:{process_var.stdout}\n"
        if process_var.stderr != "":
            exit_string += f"STDERR:{process_var.stderr}\n"

    return exit_string
