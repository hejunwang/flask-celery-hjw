#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: pytest_run.py
@time: 2021-04-25 0:21
@desc:
'''


import  pytest
class StartRun:

    def runcase(self):
        print("开始执行pytest !")
        pytest.main(["/root/flask-celery-hjw/flask-celery/pytest_pkg/test_case"])



if __name__ == '__main__':
    filename = 'xiaolvren_testcase.py'
    StartRun().runcase()
