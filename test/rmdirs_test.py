import unittest

import os
import rmdirs

from logging_test_case import LoggingTestCase
from directory_test_case import DirectoryTestCase




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