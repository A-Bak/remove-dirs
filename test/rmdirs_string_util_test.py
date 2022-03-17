import unittest

import os
import rmdirs

from logging_test_case import LoggingTestCase
from directory_test_case import DirectoryTestCase




class TestRmdirsStringUtil(LoggingTestCase, DirectoryTestCase):
    """ Test rmdirs utility. """
    
    
    def setUp(self) -> None:
        
        self.dir_paths = [            
            'test/test_dirs/test_rename_if_exists/',       
            
        ]
    
        self.file_contents = {
            'test/test_dirs/test_rename_if_exists/(1)' : None,         
            'test/test_dirs/test_rename_if_exists/(0).ext' : None,          
            'test/test_dirs/test_rename_if_exists/file.txt' : None,       
            'test/test_dirs/test_rename_if_exists/file_file.txt' : None,       
            'test/test_dirs/test_rename_if_exists/file_file (1).txt' : None,       
            'test/test_dirs/test_rename_if_exists/file_file (2).txt' : None,       
        }
        
        return super().setUp()
    
    
    def test_rename_if_exists(self):
        """ Test if file names are renamed to avoid naming conflicts. """
        
        file_path = 'test/test_dirs/test_rename_if_exists/(1)'
        result = os.path.basename(rmdirs.rename_if_exists(file_path)) 
        expected = '(1) (1)'
        self.assertEquals(result, expected)
        
        file_path = 'test/test_dirs/test_rename_if_exists/(2)'
        result = os.path.basename(rmdirs.rename_if_exists(file_path)) 
        expected = os.path.basename(file_path)
        self.assertEquals(result, expected)
        
        file_path = 'test/test_dirs/test_rename_if_exists/(0).ext'
        result = os.path.basename(rmdirs.rename_if_exists(file_path)) 
        expected = '(0) (1).ext'
        self.assertEquals(result, expected)

        file_path = 'test/test_dirs/test_rename_if_exists/file.txt'
        result = os.path.basename(rmdirs.rename_if_exists(file_path)) 
        expected = 'file (1).txt'
        self.assertEquals(result, expected)
        
        file_path = 'test/test_dirs/test_rename_if_exists/file_file.txt'
        result = os.path.basename(rmdirs.rename_if_exists(file_path)) 
        expected = 'file_file (3).txt'
        self.assertEquals(result, expected)
        
        
        
    def test_replace_chars(self):
        """ Test if a list of characters is correctly replaced in a string. """

        self.assertRaises(TypeError, rmdirs._replace_chars, (123456, ['1']))
        self.assertRaises(TypeError, rmdirs._replace_chars, ("123456", [1]))
              
        string = '1100110011'
        char_list = ['0']
        output = '11__11__11'
        self.assertEqual(rmdirs._replace_chars(string, char_list), output)
        
        string = '1100110011'
        char_list = ['0', '1']
        output = '__________'
        self.assertEqual(rmdirs._replace_chars(string, char_list), output)
        
        string = '1100110011'
        char_list = ['1']
        output = '0000000000'
        replacement = '0'
        self.assertEqual(rmdirs._replace_chars(string, char_list, replacement), output)
        
        string = 'C:\\Users\\Public/Libraries/file.ext'
        char_list = ['\\', '/']
        output = 'C:_Users_Public_Libraries_file.ext'
        self.assertEqual(rmdirs._replace_chars(string, char_list), output)
        

        
    def test_string_contains(self):
        """ Test if given string contains a character from a set of characters. """
        
        self.assertRaises(TypeError, rmdirs._string_contains, (-1, []))
        self.assertRaises(TypeError, rmdirs._string_contains, ("", [1]))
        self.assertRaises(TypeError, rmdirs._string_contains, ("1", [1]))
        
        self.assertTrue(rmdirs._string_contains("", []))
        self.assertFalse(rmdirs._string_contains("", ['a']))
        
        self.assertTrue(rmdirs._string_contains("a", ['a']))
        self.assertTrue(rmdirs._string_contains("ababba", ['a']))
        self.assertFalse(rmdirs._string_contains("a", ['b']))
        self.assertFalse(rmdirs._string_contains("ababba", ['c']))
        