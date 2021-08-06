#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import requests

#公众号列表
class Api_autorizers(object):
    # 公众号列表
    def api_get_autorizers(self,url):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjp7ImlkIjoiNTEiLCJyb2xlIjoiYWRtaW4iLCJjb2RlIjoiNTE6ZmQwMTBlYTZhZmM5In0sImlhdCI6MTYyMzMxMDI4MCwiZXhwIjoxNjU0ODQ2MjgwfQ.GDae-ST9tao5cxPlm7qGnS8lIF_E9uS5rhBy4AycSbY"
        }

        return  requests.get(url, headers= headers )