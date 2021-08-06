#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from weChart.config.VarConfig import *


# dataFilePath = parentDirPath + "\\datas\\126邮箱发送邮件.xlsx"

#读取json文件
class ReadJson(object):


    def __init__(self,filename):

        self.filepath= jsonPath+ filename
    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            return  json.load(f)
            # print(datas)

if __name__ == '__main__':

    data = ReadJson("autorizers.json").read_json()
    arrs = []
    arrs.append(
        (data.append("url"),
        data.append("expect_code")
    ))
    print( arrs)

