# -*- coding:utf-8 -*-
#######################################################
#filename:Run_TestCase.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行操作处理
#######################################################
import unittest
from src.lib.Element import Element
from conf.Run_conf import read_config
class AssertExcel(unittest.TestCase):
    def __init__(self):
        super(AssertExcel,self).__init__()
        self.driver = Element()
        self.screenshot_path =read_config('screenshot','screen_shot_path')
        self.screen_shot_isTrue = bool(read_config('testcase', 'screen_shot_isTrue'))
    
    def assertTrue_screenshot(self, expr,casename, msg1=None):
        if self.screen_shot_isTrue:
            self.screenshot_path = self.screenshot_path.format(casename)
            if expr:
                self.driver.screenshot_as_file(self.screenshot_path)
            
        return self.assertTrue(expr, msg=msg1)
    
    def assertFalse_screenshot(self, expr,casename, msg1=None):
        if self.screen_shot_isTrue:
            self.screenshot_path = self.screenshot_path.format(casename)
            if not expr:
                self.driver.screenshot_as_file(self.screenshot_path)
        return self.assertFalse(expr, msg=msg1)
    

if __name__ == "__main__":
   pass


