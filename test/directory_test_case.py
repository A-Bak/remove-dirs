import unittest

import os
import shutil




class DirectoryTestCase(unittest.TestCase):
    
    dir_paths = [
        'test/test_dirs/test_empty',
        
        'test/test_dirs/test_subdirs/1/',
        'test/test_dirs/test_subdirs/2/21',
        'test/test_dirs/test_subdirs/3/31',
        'test/test_dirs/test_subdirs/3/32/321',
        'test/test_dirs/test_subdirs/3/33',  
         
        'test/test_dirs/test_renaming/',       
        'test/test_dirs/test_renaming/1/',    
    ]
    
    file_contents = {
        'test/test_dirs/test_subdirs/1/empty' : None,
        'test/test_dirs/test_subdirs/1/cfg.txt' : '"python.testing.pytestEnabled": false',
        'test/test_dirs/test_subdirs/2/same_name.txt' : None,
        'test/test_dirs/test_subdirs/2/21/same_name.txt' : None,

        'test/test_dirs/test_renaming/1_1.txt' : 'existing file',
        'test/test_dirs/test_renaming/1_1 (1).txt' : 'existing file',
        'test/test_dirs/test_renaming/1/1.txt' : 'renamed_file',          
    }
    
    def setUp(self) -> None:
                
        for dir in self.dir_paths:
            
            if not os.path.exists(dir):
                os.makedirs(dir)
        
        for file, content in self.file_contents.items():
            
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    if content is not None:
                        f.write(content)
            
    
    def tearDown(self) -> None:
        # shutil.rmtree('test_dirs')
        pass
    