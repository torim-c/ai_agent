import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:


        absolute_path_wd = os.path.abspath(working_directory) #determines abs path from relative path via os.path.abspath(dir) using the execution place as its starting point

        target_dir = os.path.normpath(os.path.join(absolute_path_wd, directory))

        valid_dir = os.path.commonpath([absolute_path_wd, target_dir]) == absolute_path_wd

        if not valid_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        else:

            try: 
                dir_contents = os.listdir(target_dir)
                contents_details = []

                for item in dir_contents:

                    current_item_loc = os.path.normpath(os.path.join(target_dir, item))
                    item_details = f"- {item}: file_size={os.path.getsize(current_item_loc)}, is_dir={os.path.isdir(current_item_loc)}"
                    contents_details.append(item_details)
                return "\n".join(contents_details)

            except Exception as e:
                return f"Error: {e}"








        
    except Exception as e:
        return f"Error: {e}"

