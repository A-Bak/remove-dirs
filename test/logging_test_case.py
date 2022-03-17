import unittest
import logging

import os




class LoggingTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
            super().setUp()
        
            self.logger = logging.getLogger(__name__)
            
            dir_name = 'test'
            log_file_name = 'test_log.txt'       
            
            self.log_file_path = os.path.join(dir_name, log_file_name)
                 
            logging.basicConfig(filename= self.log_file_path,
                                format="[%(levelname)s] - %(asctime)s : %(message)s",
                                level = logging.DEBUG)