from tkinter.ttk import Separator
from typing import List, Tuple

import os
import logging




FilePath = str
FileName = str


def remove(root_dir: FilePath, separator: chr='_') -> None:
    
    if not os.path.exists(root_dir):
        raise ValueError("Error: Invalid path to directory.")
    
    for current_dir, _, files in os.walk(root_dir):
        
        if files:
            move_files(files, current_dir, root_dir, separator)
                
        
def move_files(files: List[FileName], current_dir: FilePath, root_dir: FilePath, separator: chr='_') -> None:
    
    # TODO Find new file name => (current_dir - root_dir) + file_name
    # TODO Move/copy the file to root_dir
    
    for file_name in files:
        
        new_file_name = os.path.join(os.path.relpath(current_dir, start=root_dir),
                                     file_name)
        
        backslashes = ['\\', '/']
        
        if contains(new_file_name, backslashes):
            for ch in backslashes:
                new_file_name = new_file_name.replace(ch, separator)

        logging.debug(f'Moved file {file_name}, new name {new_file_name}.')


def contains(string: str, char_list: List[chr]) -> bool:     
    return any([ch in string for ch in char_list])