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
         
        'test_dirs/test_renaming/',       
        'test_dirs/test_renaming/1/',    
    ]
    
    file_contents = {
        'test_dirs/test_subdirs/1/empty' : None,
        'test_dirs/test_subdirs/1/cfg.txt' : '"python.testing.pytestEnabled": false',
        'test_dirs/test_subdirs/2/same_name.txt' : None,
        'test_dirs/test_subdirs/2/21/same_name.txt' : None,

        'test_dirs/test_renaming/1_1.txt' : 'existing file',
        'test_dirs/test_renaming/1_1 (1).txt' : 'existing file',
        'test_dirs/test_renaming/1/1.txt' : 'renamed_file',          
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
        
    
    def test_renaming(self):
        """ Test """

        target_dir = 'test_dirs/test_renaming'

        self.assertTrue(os.path.exists(target_dir))
        
        rmdirs.remove(target_dir)
        
        
    def test_replace_chars(self):
        """ Test if a list of characters is correctly replaced in a string."""

        self.assertRaises(TypeError, rmdirs.replace_chars, (123456, ['1']))
        self.assertRaises(TypeError, rmdirs.replace_chars, ("123456", [1]))
              
        string = '1100110011'
        char_list = ['0']
        output = '11__11__11'
        self.assertEqual(rmdirs.replace_chars(string, char_list), output)
        
        string = '1100110011'
        char_list = ['0', '1']
        output = '__________'
        self.assertEqual(rmdirs.replace_chars(string, char_list), output)
        
        string = '1100110011'
        char_list = ['1']
        output = '0000000000'
        replacement = '0'
        self.assertEqual(rmdirs.replace_chars(string, char_list, replacement), output)
        
        string = 'C:\\Users\\Public/Libraries/file.ext'
        char_list = ['\\', '/']
        output = 'C:_Users_Public_Libraries_file.ext'
        self.assertEqual(rmdirs.replace_chars(string, char_list), output)
        

        
    def test_string_contains(self):
        """ Test if given string contains a character from a set of characters."""
        
        self.assertRaises(TypeError, rmdirs.string_contains, (-1, []))
        self.assertRaises(TypeError, rmdirs.string_contains, ("", [1]))
        self.assertRaises(TypeError, rmdirs.string_contains, ("1", [1]))
        
        self.assertTrue(rmdirs.string_contains("", []))
        self.assertFalse(rmdirs.string_contains("", ['a']))
        
        self.assertTrue(rmdirs.string_contains("a", ['a']))
        self.assertTrue(rmdirs.string_contains("ababba", ['a']))
        self.assertFalse(rmdirs.string_contains("a", ['b']))
        self.assertFalse(rmdirs.string_contains("ababba", ['c']))
        
        
if __name__ == "__main__":
    unittest.main()