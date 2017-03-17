# -*- coding:utf-8 -*-
from PIL import Image
import math
import operator

def pil_image_similarity(filepath1, filepath2):
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)
    h1 = image1.histogram()
    print h1
    h2 = image2.histogram()
    print h2
    print list(map(lambda a,b: (a-b)**2, h1, h2))
    print reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1)
    rms = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return rms

# print pil_image_similarity('/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/32E6D124-29B6-48A2-9B38-0A9D54121E10/screen/PA01100000003_02_WDCX.png',
#                            '/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/32E6D124-29B6-48A2-9B38-0A9D54121E10/screen/PA02500000000_02_TZLC.png')
#
# # import os,tempfile
# # # PATH方法获取绝对路径
# # PATH = lambda p:os.path.abspath(p)
# # # 获取临时截图目录的绝对路径
# # temp_file = PATH(tempfile.gettempdir()+'temp_screen.png')
# # print '临时截图路径: ',temp_file
#
# imgs = Image.open('/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/32E6D124-29B6-48A2-9B38-0A9D54121E10/screen/checkplugin_PA01100000000_02_HDJHY_0.png')
# width = imgs.size[0]
# height = imgs.size[1]
# print 'width =',width
# print  'height =',height
# box = (width/10,height/10,width,height/2)
# newimage = imgs.crop(box)
# newimage.save('/Users/zengyuanchen/Documents/SVN/ShareFromCloud/share/Project/Anydoor_UI/output/32E6D124-29B6-48A2-9B38-0A9D54121E10/screen/2.png')

import pytest
plugin = [('PA01100000000_02_PAZB1', u'加油站'),
          ('PA01100000000_02_PAZB2', u'加油站')
          ]

plugin2 = ['PA01100000000_02_PAZB1','PA01100000000_02_PAZB3','PA01100000000_02_PAZB4']
for i,x in enumerate(plugin):
    if x[0] not in plugin2:
        plugin.pop(i)
print plugin
