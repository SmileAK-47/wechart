#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import requests
import  unittest
from parameterized import parameterized
from weChart.tools.reed_data import ReadJson
from weChart.API.api_autorizers import Api_autorizers

def get_data():
    data = ReadJson("autorizers.json").read_json()
    arrs = []
    arrs.append((
        data.get("url"),
        data.get("expect_code")
    ))
    return  arrs
class Test_autorizers(unittest.TestCase):
    @parameterized.expand(get_data())

    def test_autorizers(self,url,expect_code):
        # url ="https://ym-be-wechat-admin-dev.baobaohehu.com/api/autorizers?page=1&pageSize=10"
        # headers = {
        #               "accept": "application/json, text/plain, */*",
        #                 "accept-encoding": "gzip, deflate, br",
        #                 "accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
        #                 "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXlsb2FkIjp7ImlkIjoiNTEiLCJyb2xlIjoiYWRtaW4iLCJjb2RlIjoiNTE6ZmQwMTBlYTZhZmM5In0sImlhdCI6MTYyMzMxMDI4MCwiZXhwIjoxNjU0ODQ2MjgwfQ.GDae-ST9tao5cxPlm7qGnS8lIF_E9uS5rhBy4AycSbY"
        #             }
        # request = requests.get(url= url , headers= headers)
        # print(request.json())
        reques = Api_autorizers().api_get_autorizers(url )
        print(reques.json())

if __name__ == '__main__':
    unittest.main()