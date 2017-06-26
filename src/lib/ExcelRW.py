#coding=utf-8
#######################################################
#filename:ExcelRW.py
#author:Jeff
#date:2015-4-27
#function:read or write excel file
#######################################################
import xlrd
import xlwt
import xlutils.copy
import os

class XlsEngine():
    """
    The XlsEngine is a class for excel operation
    Usage:
        xlseng = XlsEngine('filePath')
    """
    def __init__(self,xlsname):
        """
        define class variable
        """
        self.xls_name = xlsname  #file name
        self.xlrd_object = None  #workbook object
        self.isopentrue = False  #file open flag

    def open(self):
        """
        open a xls file
        Usage:
            xlseng.open()
        """
        try:
            self.xlrd_object = xlrd.open_workbook(self.xls_name)
            self.isopentrue = True
            #print('[%s,%s].'%(self.isopentrue,self.xlrd_object))
        except:
            self.isopentrue = False
            self.xlrd_object = None
            #print('open %s failed.'%self.xls_name)

    def sheets(self):
        """
        show xls file's sheets
        Usage:
            xlseng.sheets()
        """
        if self.isopentrue == True:
            return self.xlrd_object.sheet_names()
        else:
            #print('file %s is not open.'%self.xls_name)
            return -2

    def info(self,sheetname='Sheet1'):
        """
        show xls file information
        Usage:
            xlseng.info()
        """

        if self.isopentrue == True:
            if sheetname in self.xlrd_object.sheet_names():
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                #print('%s:(%d row,%d col).'%(sheetname,worksheet.nrows,worksheet.ncols))
                # return [worksheet.col_values,worksheet.row_values]
                return [worksheet.nrows,worksheet.ncols]
            else:
                #print('sheetname: %s is error.' % sheetname)
                return -3
        else:
            #print('file %s is not open.'%self.xls_name)
            return -2

    def readsheet(self,sheetname='Sheet1'):
        if self.isopentrue == True:
            if sheetname in self.xlrd_object.sheet_names():
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                rowns = worksheet.nrows
                # print 'rowns = ',rowns
                listsheet=[]
                for curr_row in range(rowns):
                    listsheet.append(worksheet.row_values(curr_row))
                    if curr_row == 0:
                        continue
                return listsheet
            else:
                return -3
        else:
            return -2

    def readcell(self,sheetname='Sheet1',rown=1,coln=1):
        """
        read file's a cell content
        Usage:
            xlseng.readcell('sheetname',rown,coln)
        """
        rown=rown-1
        coln=coln-1
        try:
            if self.isopentrue == True:
                worksheets = self.xlrd_object.sheet_names()
                if sheetname not in worksheets:
                    #print('%s is not exit.'%sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                cell = worksheet.cell_value(rown,coln)
                #print('[file:%s,sheet:%s,row:%s,col:%s]:%s.'%(self.xls_name,sheetname,rown,coln,cell))
                return cell
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('readcell is false! please check sheetn rown and coln is right.')
            return -1

    def readrow(self,sheetname='Sheet1',rown=1):
        """
        read file's a row content
        Usage:
            xlseng.readrow('sheetname',rown)
        """
        rown=rown-1
        try:
            if self.isopentrue == True:
                worksheets = self.xlrd_object.sheet_names()
                if sheetname not in worksheets:
                    #print('%s is not exit.'%sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                row = worksheet.row_values(rown)
                #print('[file:%s,sheet:%s,row:%s]:%s.'%(self.xls_name,sheetname,rown,row))
                return row
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('readrow is false! please check sheetn rown is right.')
            return -1

    def readcol(self,sheetname='Sheet1',coln=1):
        """
        read file's a col content
        Usage:
            xlseng.readcol('sheetname',coln)
        """
        coln=coln-1
        try:
            if self.isopentrue == True:
                worksheets = self.xlrd_object.sheet_names()
                if sheetname not in worksheets:
                    #print('%s is not exit.'%sheetname)
                    return False
                worksheet = self.xlrd_object.sheet_by_name(sheetname)
                col = worksheet.col_values(coln)
                #print('[file:%s,sheet:%s,col:%s]:%s.'%(self.xls_name,sheetname,coln,col))
                return col
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('readcol is false! please check sheetn coln is right.')
            return -1

    def writecell(self,value='',sheetn=1,rown=1,coln=1):
        """
        write a cell to file,other cell is not change
        Usage:
             xlseng.writecell('str',sheetn,rown，coln)
        """
        sheetn=sheetn-1
        rown=rown-1
        coln=coln-1
        try:
            if self.isopentrue == True:
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                worksheet = xlrd_objectc.get_sheet(sheetn)
                worksheet.write(rown,coln,value)
                xlrd_objectc.save(self.xls_name)
                #print('writecell value:%s to [sheet:%s,row:%s,col:%s] is ture.'%(value,sheetn,rown,coln))
                return 0
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('writecell is false! please check.')
            return -1

    def writerow(self,values=[],sheetn=1,rown=1,coln=1):
        """
        write a row to file,other row and cell is not change
        Usage:
            xlseng.writerow('str1,str2,str3...strn',sheetn,rown.coln)
        """
        sheetn=sheetn-1
        rown=rown-1
        coln=coln-1
        try:
            if self.isopentrue == True:
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                worksheet = xlrd_objectc.get_sheet(sheetn)
                values = values.split(',')
                for value in values:
                    worksheet.write(rown,coln,value)
                    coln += 1
                xlrd_objectc.save(self.xls_name)
                #print('writerow values:%s to [sheet:%s,row:%s,col:%s] is ture.'%(values,sheetn,rown,coln))
                return 0
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('writerow is false! please check.')
            return -1

    def writecol(self,values=[],sheetn=1,rown=1,coln=1):
        """
        write a col to file,other col and cell is not change
        Usage:
            xlseng.writecol('str1,str2,str3...',sheetn,rown.coln)
        """
        sheetn=sheetn-1
        rown=rown-1
        coln=coln-1
        try:
            if self.isopentrue == True:
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                worksheet = xlrd_objectc.get_sheet(sheetn)
                values = values.split(',')
                for value in values:
                    worksheet.write(rown,coln,value)
                    rown += 1
                xlrd_objectc.save(self.xls_name)
                #print('writecol values:%s to [sheet:%s,row:%s,col:%s] is ture.'%(values,sheetn,rown,coln))
                return 0
            else:
                #print('file %s is not open.'%self.xls_name)
                return -2
        except:
            #print('writecol is false! please check.')
            return -1


    def filecreate(self,sheetnames='Sheet1'):
        """
        create a empty xlsfile
        Usage:
            filecreate('sheetname1,sheetname2...')
        """
        try:
            if os.path.isfile(self.xls_name):
                #print('%s is exit.'%self.xls_name)
                return False
            workbook = xlwt.Workbook()
            sheetnames = sheetnames.split(',')
            for sheetname in sheetnames:
                workbook.add_sheet(sheetname,cell_overwrite_ok=True)
            workbook.save(self.xls_name)
            #print('%s is created.'%self.xls_name)
            return 0
        except:
            #print('filerator is false! please check.')
            return -1


    def addsheet(self,sheetnames='Sheet1'):
        """
        add sheets to a exit xlsfile
        Usage:
            addsheet('sheetname1,sheetname2...')
        """
        try:
            if self.isopentrue == True:
                worksheets = self.xlrd_object.sheet_names()
                xlrd_objectc = xlutils.copy.copy(self.xlrd_object)
                sheetnames = sheetnames.split(',')
                for sheetname in sheetnames:
                    if sheetname in worksheets:
                        #print('%s is exit.'%sheetname)
                        return False
                for sheetname in sheetnames:
                    xlrd_objectc.add_sheet(sheetname,cell_overwrite_ok=True)
                xlrd_objectc.save(self.xls_name)
                #print('addsheet is ture.')
                return 0
            else:
                #print("file %s is not open \n"%self.xls_name)
                return -2
        except:
            #print('addsheet is false! please check.')
            return -1

"""
        def chgsheet(self,sheetn,values):
        def clear(self):
"""


#测试
if __name__ == '__main__':
    casepath = os.path.abspath('../../TestCase/Excel/TestCase.xls')
    print ('用例路径',casepath)
    #初始化对象
    xlseng = XlsEngine(casepath)

    #新建文件，可以指定要新建的sheet页面名称，默认值新建Sheet1
    #print("\nxlseng.filecreate():")
    #xlseng.filecreate('neweSheet1,newesheet2,newesheet3')

    #打开文件
    print("xlseng.open():")
    xlseng.open()

    #添加sheet页
    #print("\nxlseng.addsheet():")
    #xlseng.addsheet('addSheet1,addsheet2,addsheet3')

    #输出文件信息
    print("\nxlseng.info():")
    print (xlseng.info())

    #读取Sheet1页第2行第1列单元格数据（默认读取Sheet1页第1行第1列单元格数据）
    print("\nxlseng.readcell():")
    print (xlseng.readcell('Sheet1',3,1))

    #读取Sheet1页第2行的数据（默认读取Sheet1页第1行的数据）
    print("\nxlseng.readrow():")
    print (xlseng.readrow('Sheet1',3))

    #读取Sheet1页第2列的数据（默认读取Sheet1页第1列的数据）
    print("\nxlseng.readcol():")
    print (xlseng.readcol('Sheet1',2))

    #向第一个sheet页的第2行第4列写字符串数据‘I am writecell writed’(默认向第一个sheet页的第1行第1列写空字符串)
    #print("\nxlseng.writecell():")
    #xlseng.writecell('I am writecell writed',0,2,4)

