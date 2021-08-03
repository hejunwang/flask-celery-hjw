#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: settings.py
@time: 2021-03-25 23:24
@desc:
'''

import os

class Config(object):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = False



# 配置worker
# 配置backend
class ProjectConfig(Config):
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
