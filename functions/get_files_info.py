import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory) if directory else working_directory
    
    full_path_abs = os.path.abspath(full_path)
    working_directory_abs = os.path.abspath(working_directory)
    
    if not full_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    dir_content = os.listdir(full_path)
        
    files_string = ''
    for el in dir_content:
        is_dir = os.path.isdir(os.path.join(full_path, el))
        file_size = os.path.getsize(os.path.join(full_path, el))
        files_string += f'{el}: file_size={file_size} bytes, is_dir={is_dir}\n'
    
    return files_string
    
