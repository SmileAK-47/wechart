#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import unittest


class Test_getusercumulate(unittest.TestCase):
    def test_getusercumulate(self):
        url = "https://ym-be-wechat-admin-dev.baobaohehu.com/test?url=getusercumulate&end_at=2021-07-07&start_at=2021-07-07"

        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8"
        }

        reques = requests.get(url=url, headers=headers)
        print(reques.json())


if __name__ == '__main__':
    unittest.main()
