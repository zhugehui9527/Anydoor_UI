# -*- coding:utf-8 -*-
#######################################################
#filename:Run_TestCase.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行操作处理
#######################################################
import unittest
class AssertExcel(unittest.TestCase):
    def __init__(self):
        super(AssertExcel,self).__init__()
        pass
    
    def assertTrue_excel(self, expr, msg1=None):
        return self.assertTrue(expr, msg=msg1)
    
    def assertFalse_excel(self, expr, msg1=None):
        return self.assertFalse(expr, msg=msg1)
    

if __name__ == "__main__":
   pass


