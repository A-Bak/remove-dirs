from genericpath import samefile
from tkinter.ttk import Separator
from typing import List, Tuple

import os
import shutil
import logging


Char = str

FilePath = str
FileName = str


def remove(root_dir: FilePath, separator: Char='_') -> None:
    """ 
    Docstring
    """
    if not os.path.exists(root_dir):
        raise ValueError("Invalid path to directory.")
    
    # First directory returned by os.walk() is the root_dir
    # => Skip as there is no need to copy files
    dirtree_iter = os.walk(root_dir)
    next(dirtree_iter, None)
    
    for current_dir, _, files in dirtree_iter:
        
        if files:
            for file_name in files:
                
                source_file_path = os.path.join(current_dir, file_name)
                target_file_path = new_file_name(file_name, current_dir, root_dir, separator)
                
                shutil.move(source_file_path, target_file_path)
                
                logging.debug(f'New name is "{target_file_path}".')
    
    
def new_file_name(file_name: FileName, current_dir: FilePath, root_dir: FilePath, separator: Char='_'):
    """ 
    Docstring
    """
    new_file_name = os.path.join(os.path.relpath(current_dir, start=root_dir), file_name)
    new_file_name = replace_chars(new_file_name, ['\\', '/'], separator)    
    new_file_name = rename_if_exists(os.path.join(root_dir, new_file_name))
    
    return new_file_name

        
def rename_if_exists(target_file_path: FilePath) -> FilePath:
    
    if os.path.exists(target_file_path):
        
        # Split off extension from target_file_path and add index (i) to distinguish the file
        # 'target/file/path.ext' -> 'target/file/path' + ' (i)' + .ext' ->  'target/file/path (i).ext'
        
        i = 1
        new_file_path = '{1} ({0}){2}'.format(i, *os.path.splitext(target_file_path))
        
        while os.path.exists(new_file_path):
            i += 1
            new_file_path = '{1} ({0}){2}'.format(i, *os.path.splitext(target_file_path))
        
        return new_file_path
                       
    else:
        return target_file_path    
        
        
def replace_chars(string: str, char_list: List[Char], replacement: str='_') -> str:
    """ Docstring """
    if not char_list:
        raise ValueError('Argument char_list is an empty list.')
    
    new_string = string
    
    if string_contains(string, char_list):
        for ch in char_list:
            new_string = new_string.replace(ch, replacement)

    return new_string


def string_contains(string: str, char_list: List[Char]) -> bool:     
    """ Docstring """
    if not isinstance(string, str):
        raise TypeError('String argument is not of type str.')
    
    if not char_list:
        return True
    
    if any([not isinstance(ch, str) for ch in char_list]):
        raise TypeError(('All elements of char_list must be of type str.'))
    
    return any([ch in string for ch in char_list])