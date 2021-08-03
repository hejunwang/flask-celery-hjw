#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: create_task.py
@time: 2021-03-25 23:24
@desc:
'''


from flask import Blueprint

from celery_task.tasks import send_mail,second_test,mysql_select,newtask

task = Blueprint('task',__name__)

@task.route('/add_task',methods=['GET','POST'])
def add_task():
    """
    添加任务
    :return:
    """
    result = send_mail.delay()

    return '测试成功 ！！！'

@task.route('/second',methods=['GET'])
def second():
    second_test.delay()

    return '测试成功 ！！！'


@task.route('/select',methods=['GET'])
def sql():
    mysql_select.delay()

    return "测试成功 ！！！"

@task.route('/newfun',methods=['GET','POST'])
def newfun():
    newtask.apply_async()
    return 'OK'


