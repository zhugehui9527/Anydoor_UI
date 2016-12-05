# -*- coding:utf-8 -*-
import re,sys
import os,logging
import pytest_html
'''
filepath = '/Users/zengyuanchen/test2.log'
#adb shell logcat > c:\data\1.txt
# os.system('adb shell logcat >'+filepath)
try:
	openfile = open(filepath,'r')
	context = openfile.read()
except Exception:
	raise
finally:
	openfile.close()

print ' '
info ={'INFO':[],'ERROR':[]}
lists =['d1=registration_connect_to_family','ea=Connect To Family','ec=Registration']
for x in range(len(lists)):
	list_n = re.findall(lists[x],context)
	if list_n :
		# print '[ INFO ] : find %s' % list_n
		info['INFO'].append(list_n)
	else:
		# print '[ ERROR ] : not find string: [ %s ]' % lists[x]
		info['ERROR'].append(list_n)

if len(info['ERROR']) == 0:
	print 'pass'
else:
	print 'fail'


# 将字符串当成有效Python表达式来求值，并返回计算结果
print '[ INFO ] : eval :',eval('1+2')
# 将Python的变量和表达式转换为字符串表示
print '[ INFO ] : eval :',repr(1==2)

print 'log level :',logging.DEBUG
console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
logger.addHandler(console)

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')


paths = os.path.split(os.path.realpath(sys.argv[0]))[0]
print paths
print os.path.realpath(sys.argv[0])

#
# rootdir='/Users/zengyuanchen/Documents/Android'
# for parent,dirnames,filenames in os.walk(rootdir):
#     for dirname in  dirnames:
#         print "parent is:" + parent
#         print  "dirname is" + dirname
#
#     for filename in filenames:
#         print "parent is:"+ parent
#
#         print "filename is:" + filename
#         print "the full name of the file is:" + os.path.join(parent,filename)
#         print '-------------'
#

'''
print '*'*40
import os
path1 = 'niiwoo.apk'
path2 = 'C:\\niiwoo\\apk\\'
path33 = path2 +path1
path4= os.path.join('',path33)
print path4,type(path4)
path3 = os.path.join(path2,path1)
print os.path.abspath(path3)
print '*'*40