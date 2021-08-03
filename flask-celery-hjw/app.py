#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@126.com
@software: pycharm
@file: app.py
@time: 2021-03-25 23:21
@desc:
'''
import os,time,random

from flask import Flask,render_template,request,jsonify,send_from_directory,redirect,session,flash,url_for
from api.create_task import task
from celery import Celery
from com_pkg.comm import Comm
from celery_task.tasks import send_mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
UPLOAD_FOLDER = 'testcase-data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF','pdf'])


# ------------------------------------------------

# Celery configuration   要存储 Celery 任务的状态或运行结果时就必须要配置
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#
# # Initialize Celery 初始化Celery
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# # 将Flask中的配置直接传递给Celery
# celery.conf.update(app.config)

# ------------------重构------------------------------

@app.route('/',methods=['GET','POST'])
def index():
    print('11111111111111111')

    return render_template('index.html')


@app.route('/lay')
def layadmin():
    return render_template('lay2.html')

# @celery.task
# def send_mail():
#     """Background task that runs a long function with progress reports."""
#     verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
#     print('邮件开始发送....')
#     for i in range(20):
#         print('this is a flask send email-test:{}'.format(i))
#         time.sleep(1)
#     print('邮件发送结束！')
#     return {'current':100,'status':"completed"}

@app.route('/newfun',methods=['GET'])
def newfun():
    print('newfun..............')
    task = send_mail.apply_async()
    print("task_id:{}".format(task.id))
    return {'location':url_for('taskstatus',task_id= task.id)}
    # return redirect(url_for(index))

# 任务状态
@app.route('/status/<task_id>')
def taskstatus(task_id):
    task= send_mail.AsyncResult(task_id)
    if task.state=="PENDING":
        response={
            "state":task.state
        }
    else:
        response = {
            "state": task.state
        }

    return jsonify(response)




# 判断文件的后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 下载文件 ,这个文件必须存在static下
@app.route('/api/download', methods=['GET'])
def api_download():
    filepath = os.path.join(basedir,'static/test_report/')
    print(filepath)
    if filepath:
        return send_from_directory(filepath, '1.png', as_attachment=True)
    else:
        return jsonify({"errormsg": "下载失败！"})

# sql 查询下载文件
@app.route('/sql/download', methods=['GET'])
def sql_download():
    filepath = os.path.join(basedir,'static/sql_report/')
    print(filepath)
    print('filepath-->{}'.format(filepath))
    pd =Comm()._find_new_file(filepath)
    print(pd[0],pd[1])
    if filepath:
        return send_from_directory(filepath, pd[1], as_attachment=True)
    else:
        return render_template('result.html',errormsg="下载失败！")

# 上传文件
@app.route('/api/upload', methods= ['POST'], strict_slashes=False)
def api_upload():
    print(basedir)
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    file_name = f.filename

    if f and allowed_file(f.filename):
        # fname = secure_filename(f.filename)
        # print(fname)
        # ext = fname.rsplit('.', 1)[1]
        # unix_time = int(time.time())
        # new_filename = str(unix_time) + '.' + ext
        f.save(os.path.join(file_dir, file_name))
    #     return jsonify({"errno": 0, "errmsg": "上传成功"})
        return render_template('result.html', file_name=file_name, errormsg="上传成功")
    else:
        return render_template('result.html', file_name=file_name, errormsg="上传失败")



if __name__ == '__main__':
    print('url Rule地址 ：-------------------\n')
    print(app.url_map)
    print('url Rule地址 ：-------------------\n')
    app.run(host='0.0.0.0',debug=True)

