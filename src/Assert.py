# -*- coding:utf-8 -*-
#######################################################
#filename:Run_TestCase.py
#author:Jeff
#date:2016-09-21
#function:对运行用例进行操作处理
#######################################################

def Assert_Equal(ExpectResult, ActualResult):
    if ExpectResult == ActualResult:
        print 'PASS'
        Case_Result = 'PASS'
    else:
        print 'FAIL'
        Case_Result = 'FAIL'

    return Case_Result


def Assert_In(ExpectResult, ActualResult):
    if ExpectResult in ActualResult:
        print 'PASS'
        Case_Result = 'PASS'
    else:
        print 'FAIL'
        Case_Result = 'FAIL'

    return Case_Result

def Assert_True(ActualResult):
    if ActualResult == True:
        print 'PASS'
        Case_Result = 'PASS'
    else:
        print 'FAIL'
        Case_Result = 'FAIL'
    return Case_Result



if __name__ == "__main__":
    ExpectResult = "1"
    ActualResult = "2"
    result = True
    Assert_Equal(ExpectResult, ActualResult)
    Assert_In(ExpectResult, ActualResult)
    Assert_True(result)


