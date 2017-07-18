# -*- coding:utf-8 -*-
#######################################################
#filename:Assert.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行断言
#######################################################
import unittest
from src.lib.Element import Element
from conf.Run_conf import read_config
BOOL = lambda p: True if p == 'True' or p == 'true' else False

class AssertClass(unittest.TestCase):
    '''
    预留断言类,目前暂未使用,断言API已经封装在excel支持的api中
    '''
    def __init__(self,driver):
        super(AssertClass,self).__init__()
        self.driver = Element(driver)
        self.screenshot_path =read_config('screenshot','screen_shot_path')
        self.screen_shot_isTrue = BOOL(read_config('testcase', 'screen_shot_isTrue'))
    
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
    
    def _assertTrue(self,expr,msg=None):
        return self.assertTrue(expr,msg=msg)
    

if __name__ == "__main__":
   pass


