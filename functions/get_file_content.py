import os
from functions.config import FILE_CHAR_LIMIT

def get_file_content(working_directory, file_path):
    
    full_path = os.path.join(working_directory, file_path)
    
    full_path_abs = os.path.abspath(full_path)
    working_directory_abs = os.path.abspath(working_directory)
    
    if not full_path_abs.startswith(working_directory_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" is not a file'
    
    with open(full_path, 'r') as file:
        file_content = file.read()
    
    if len(file_content) > FILE_CHAR_LIMIT:
        file_content = f'{file_content[:FILE_CHAR_LIMIT]}[...File {file_path} truncated at {FILE_CHAR_LIMIT} characters]'
    
    return file_content
    
    return