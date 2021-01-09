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

    def test_xueqiu_quote(self):
        cookie={
            "xq_a_token":"ad26f3f7a7733dcd164fe15801383e62b6033003"
        }
        headers={
            "host":"xueqiu.com",
            "User-Agent":"Jo"
        }
        r=requests.get("https://xueqiu.com/service/v5/stock/batch/quote?symbol=SH000001%2CSZ399001%2CSZ399006%2CSH000688&_=1610198308617",headers=headers,cookies=cookie)
        # logging.info(r)
        # logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))
        assert r.json()["data"]["items"][0]["quote"]["symbol"] =="SH000001"
