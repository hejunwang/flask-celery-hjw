#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: tasks.py
@time: 2021-03-25 23:24
@desc:
'''

# task：任务
# broker（中间人）：存储任务的队列
# worker：真正执行任务的工作者
# backend：用来存储任务执行后的结果

import time

from celery import Celery

from com_pkg.comm import *
from pytest_pkg.pytest_run import *
# 创建celery对象
celery = Celery("tasks",
                broker="redis://localhost:6379/0",
                backend="redis://localhost:6379/1")


# 定义任务
@celery.task               #加上此装饰器，这个函数就变成celery任务了(task)
def send_mail():
    print('邮件开始发送....')
    for i in range(20):
        print('this is a flask send email-test:{}'.format(i))
        time.sleep(1)
    print('邮件发送结束！')

@celery.task
def second_test():
    print("API接口自动化测试")
    StartRun().runcase()

@celery.task
def mysql_select(sql_str=None):
    # 读取配置文件
    db=Comm()._ret_db('./config/cfg.ini', 'mysql')

    sql = 'SELECT * from t_charge_deal ORDER BY dealId DESC limit 20;'
    if sql_str==None:
        print('参数为空')
        db.sel_sql(sql_string=sql)
        db.close_()
    else:
        print("参数不为空")
        db.sel_sql(sql_string=sql_str)
        db.close_()


@celery.task
def newtask():
    print('我是新功能测试  newtask....')