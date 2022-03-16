import unittest

import os
import rmdirs

from logging_test_case import LoggingTestCase
from directory_test_case import DirectoryTestCase




class TestRmdirsStringUtil(LoggingTestCase, DirectoryTestCase):
    """ Test rmdirs utility."""
    
    
    def setUp(self) -> None:
        return super().setUp()
    
    
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
        