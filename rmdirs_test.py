import unittest
import logging

import os
import sys
import shutil

import rmdirs




class LoggingTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
            super().setUp()
        
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(filename='test_log.txt',
                                format="[%(levelname)s] - %(asctime)s : %(message)s",
                                level = logging.DEBUG)
        
        
        
        
class DirectoryTestCase(unittest.TestCase):
    
    dir_paths = [
        'test_dirs/test_empty',
        'test_dirs/test_subdirs/1/',
        'test_dirs/test_subdirs/2/21',
        'test_dirs/test_subdirs/3/31',
        'test_dirs/test_subdirs/3/32/321',
        'test_dirs/test_subdirs/3/33',          
    ]
    
    file_contents = {
        'test_dirs/test_subdirs/1/empty' : None,
        'test_dirs/test_subdirs/1/cfg.txt' : '"python.testing.pytestEnabled": false',
        'test_dirs/test_subdirs/2/same_name.txt' : None,
        'test_dirs/test_subdirs/2/21/same_name.txt' : None,
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
        shutil.rmtree('test_dirs')
    
    
    
    
class TestRmdirs(LoggingTestCase, DirectoryTestCase):
    """ Test rmdirs utility."""
    
    def setUp(self) -> None:
        return super().setUp()
    
    
    def test_logging(self):
        
        self.assertTrue(self.logger is not None)
        self.logger.debug("Logged message.")
    
    
    def test_empty_dir(self):
        """ Test use of rmdirs on an empty directory. """
        
        self.assertTrue(os.path.exists('test_dirs/test_empty'))
        
    
    def test_remove_subdirs(self):
        """ Test """
        
        rmdirs.remove('test_dirs/test_subdirs')
        
        # self.assertTrue(not os.path.exists( PATH TO SUBDIRS ))
        self.assertTrue(os.path.exists('test_dirs/test_subdirs'))

        
if __name__ == "__main__":
    unittest.main()