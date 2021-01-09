#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2021/1/9 0009 15:15
# @Author     : Joey Jiang
# @File       : test_requests.py
# @Software   : PyCharm
# @Description: 接口测试库requests测试
import requests
import logging
import pytest
class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    def test_get(self):
        # r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        r=requests.get("https://www.baidu.com/")
        logging.info(r)
        logging.info(r.text)
        logging.info(r.json())