import pymysql
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456789',
    db='world',
    charset='utf8'
)
cursor = connect.cursor()

# sql = "SELECT name,saving FROM trade WHERE account = '%s' "
# sql = "SELECT LocalName FROM country WHERE LocalName='Belarus'"
sql ="SELECT * FROM country, city " \
     "/WHERE country.GNP>8000000 " \
     "AND city.ID>4000  ORDER BY ID DESC LMIT 10"
# data = ('13512345678',)
# cursor.execute(sql % data)
cursor.execute(sql )
data = cursor

print("Database version : %s " % data)
# for row in cursor.fetchall():
#     print("Name:%s\tSaving:%.2f" % row)

# print('共查找出', cursor.rowcount, '条数据')
# print('共查找出',sql, '条数据')

# db = pymysql.connect("localhost", "root", "123456789", "local-test")
# cursor = db.cursor()
#
# cursor.execute("SELECT SELECT COUNT(*) FROM city")
# data = cursor.fetchone()
# print("Database version : %s " % data)

# 关闭连接
cursor.close()
connect.close()
