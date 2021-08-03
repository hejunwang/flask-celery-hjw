#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Introduce :
@File      : conftest___1.py
@Time      : 2021/5/8 11:16
@Author    : toby
"""

import pytest,json
from api_interface.interface import Interface_api
import configparser

# @pytest.fixture(scope="session", autouse=True)
def token():
    print("执行conftest文件")

    cf = configparser.ConfigParser()
    cf.read('param.ini', encoding='utf-8')
    _url = cf.get('conf', 'url')
    _username = cf.get('conf', 'username')
    _password = cf.get('conf', 'password')
    _conttype = cf.get('conf', 'Content-Type')
    _uagent = cf.get('conf', 'User-Agent')
    _dt={}
    _headers={}
    _dt['username']=_username
    _dt['password']=_password
    _headers['Content-Type']=_conttype
    _headers['User-Agent']=_uagent

    print(_url)
    print(_dt)
    print(_headers)

    res = Interface_api(url=_url).post_interface(data=json.dumps(_dt),headers=_headers)
    print('*' * 50)
    ress = json.loads(res.text)
    print(json.loads(res.text))
    print('测试结果:{}'.format(ress))

    assert ress['errorCode'] == 0
    print('*' * 50)
    token = ress['data']['token']
    return token


if __name__ == '__main__':
    token = token()
    print(token)