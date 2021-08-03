#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: xiaolvren_testcase.py
@time: 2021-04-24 22:15
@desc:
'''
import pytest


class Test_Xlr002():

    def test_1(self):
        print('测试结果:Test_Xlr002_1')

    def test_2(self):
        print('测试结果 :Test_Xlr002_1')



if __name__ == '__main__':
    pytest.main(['-s','xiaolvren_testcase.py'])
