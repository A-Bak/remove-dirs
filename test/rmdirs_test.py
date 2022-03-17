import unittest

import os
import rmdirs

from logging_test_case import LoggingTestCase
from directory_test_case import DirectoryTestCase




class TestRmdirs(LoggingTestCase, DirectoryTestCase):
    """ Test rmdirs utility."""
    
    def setUp(self) -> None:
        
        self.dir_paths = [
            'test/test_dirs/test_empty',
            'test/test_dirs/test_empty/empty_dir',
            'test/test_dirs/test_empty/dir/1',
            'test/test_dirs/test_empty/dir/2',
            'test/test_dirs/test_empty/dir/3',
            
            'test/test_dirs/test_subdirs/1/',
            'test/test_dirs/test_subdirs/2/21',
            'test/test_dirs/test_subdirs/3/31',
            'test/test_dirs/test_subdirs/3/32/321',
            'test/test_dirs/test_subdirs/3/33',  
            
            'test/test_dirs/test_renaming/',       
            'test/test_dirs/test_renaming/1/',    
            
        ]
    
        self.file_contents = {
            'test/test_dirs/test_subdirs/1/empty' : None,
            'test/test_dirs/test_subdirs/1/cfg.txt' : '"python.testing.pytestEnabled": false',
            'test/test_dirs/test_subdirs/2/same_name.txt' : None,
            'test/test_dirs/test_subdirs/2/21/same_name.txt' : None,

            'test/test_dirs/test_renaming/1_1.txt' : 'existing file',
            'test/test_dirs/test_renaming/1_1 (1).txt' : 'existing file',
            'test/test_dirs/test_renaming/1/1.txt' : 'renamed_file',          
        }
        
        return super().setUp()
    
    
    def test_logging(self):
        
        self.assertTrue(self.logger is not None)
        self.logger.debug("Logged message.")
        
        self.assertTrue(os.path.exists(self.log_file_path))

    
    def test_empty_dir(self):
        """ Test use of rmdirs on an empty directory. """
        
        dir_path = 'test/test_dirs/test_empty'
        
        self.assertTrue(os.path.exists(dir_path))
        
        _, dirs, files = next(os.walk(dir_path))
        self.assertNotEqual(dirs, [])
        self.assertEqual(files, [])
        
        rmdirs.remove(dir_path)
        
        _, dirs, files = next(os.walk(dir_path))
        self.assertEqual(dirs, [])
        self.assertEqual(files, [])
        
        
    
    def test_remove_subdirs(self):
        """ Test """
        
        target_dir = 'test/test_dirs/test_subdirs'
        self.assertTrue(os.path.exists(target_dir))
        
        _, subdirs, _ = next(os.walk(target_dir))
        self.assertEqual(subdirs, ['1', '2', '3'])
        
        rmdirs.remove(target_dir)
        
        _, subdirs, _ = next(os.walk(target_dir))
        self.assertEqual(subdirs, [])
        
        
    def test_renaming(self):
        """ Test """

        target_dir = 'test/test_dirs/test_renaming'
        self.assertTrue(os.path.exists(target_dir))

        _, _, files = next(os.walk(target_dir))
        self.assertEqual(sorted(files), ['1_1 (1).txt', '1_1.txt'])
        
        rmdirs.remove(target_dir)

        _, _, files = next(os.walk(target_dir))
        self.assertEqual(sorted(files), ['1_1 (1).txt', '1_1 (2).txt', '1_1.txt'])
        
    
  
        
if __name__ == "__main__":
    unittest.main()