import unittest

import os
import shutil




class DirectoryTestCase(unittest.TestCase):
     
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
        shutil.rmtree('test/test_dirs')
    