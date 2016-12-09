# -*- coding: utf-8 -*-
__author__ = 'Jeff'

"""
@author:Jeff
@time: 29/11/16 下午3:25
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='Anydoor_UI',
    keywords='',
    version=1.0,
    url='',
    license='MIT',
    author='Jeff',
    author_email='2571226011@qq.com',
    description='',
    install_requires=[
        'xlrd','xlwt','Appium-Python-Client','selenium','xlutils','PyH','ConfigParser','Pytest','pytest-html','pytest-rerunfailures'
    ]
)
