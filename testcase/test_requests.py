#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2021/1/9 0009 15:15
# @Author     : Joey Jiang
# @File       : test_requests.py
# @Software   : PyCharm
# @Description: 接口测试库requests测试
import requests
import logging
import json


class TestRequests(object):
    url = "https://testerhome.com/api/v3/topics.json?limit=2"

    def test_get(self):
        r = requests.get(self.url)
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
