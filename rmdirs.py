from genericpath import samefile
from tkinter.ttk import Separator
from typing import List, Tuple

import os
import shutil
import logging




FilePath = str
FileName = str


def remove(root_dir: FilePath, separator: chr='_') -> None:
    """ 
    Docstring
    """
    if not os.path.exists(root_dir):
        raise ValueError("Error: Invalid path to directory.")
    
    # First directory returned by os.walk() is the root_dir
    # => Skip as there is no need to copy files
    dir_iterator = os.walk(root_dir)
    next(dir_iterator, None)
    
    for current_dir, _, files in dir_iterator:
        
        if files:
            for file_name in files:
                move_file(file_name, current_dir, root_dir, separator)
                
        
def move_file(file_name: FileName, current_dir: FilePath, root_dir: FilePath, separator: chr='_') -> None:
    """ 
    Docstring
    """
    new_file_name = os.path.join(os.path.relpath(current_dir, start=root_dir),
                                 file_name)
    new_file_name = replace_chars(new_file_name, ['\\', '/'], separator)

    source_file_path = os.path.join(current_dir, file_name)
    target_file_path = os.path.join(root_dir, new_file_name)
    
    if not os.path.exists(target_file_path):
        shutil.copyfile(source_file_path, target_file_path)
        
    else:
        i = 1
        file_path, extension = os.path.splitext(target_file_path)
        
        while os.path.exists(f'{file_path} ({i}){extension}'):
            i += 1
            
        shutil.copy(source_file_path, f'{file_path} ({i}){extension}')
        
        logging.debug(f'New name is "{file_path} ({i}){extension}"')
        
        
def replace_chars(file_name: FileName, char_list: List[chr], separator: chr='_') -> FileName:
    """ Docstring """
    new_file_name = file_name
    
    if contains(file_name, char_list):
        for ch in char_list:
            new_file_name = new_file_name.replace(ch, separator)

    return new_file_name


def contains(string: str, char_list: List[chr]) -> bool:     
    """ Docstring """
    return any([ch in string for ch in char_list])