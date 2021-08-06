# 建立客户端连接的三种方法
import pymongo
from pymongo import MongoClient

import json
def mon_01():
  """链接数据库"""
  uri='mongodb://chv2:E5998o155@syhhdev1-pub.mongodb.rds.aliyuncs.com:3717,syhhdev2-pub.mongodb.rds.aliyuncs.com:3717/chv2?replicaSet=mgset-21756975'
  client = pymongo.MongoClient(uri)
  # mongodb: // 用户名：密码 @ 服务器IP或域名：端口
  db =client['chv2']
  collexction =db['ym_user']
  # collexxction=db['ym_hospital_port']
  # print(collexxction)

  # rows =collexxction.find({'mobile':'18829783382'})
  # rows = collexxction.find().limit(2)

  rows =collexction.find({"mobile": "18829783382","nickname": "简简单单就是我"})
  result = []
  for i in rows:
    result.append(i)
    print(i)
    print(i["_id"],i["mobile"])
    # print(i["mobile"])
    # print(result)

  # hah = result

  # for r1 in rows:
# ` hah = result['mobile']
#   print(hah)
    # print(r1 ["_id"])
    # print(r1 ["mobile"])
    # print(r1 ["nickname"])
    # print(r1)
    # return r1
  # result[1]
if __name__ == '__main__':
  mon_01()

