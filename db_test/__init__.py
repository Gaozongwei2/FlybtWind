import pymysql
# # 声明连接对象
# connect = pymysql.connect(host = "localhost", port = 3306, user = "root", password = "123456", db = "travel")
#
# # 获取操作游标
# cursor = connect.cursor()
#
# # 创建sql语句
# sql = "select * from user"
#
# # 通过游标进行操作，execute（）执行sql语句
# cursor.execute(sql)
# # 获取第一条数据
# data = cursor.fetchone()
#
# print(data)
#
#
# # 新建表
# try:
#     db = None
#     cursor = None
#     db = pymysql.connect(host = "localhost", user = "root", password = "123456", db = "travel" )
#     cursor = db.cursor()
#     sql = ""
#     cursor.execute(sql)
# except Exception as ex:
#     print(ex)
# finally:
#     if db:
#         db.close()
#     if cursor:
#         cursor.close()
#
# # 事务
# # 提交， 数据才被真正写到了数据库中
# cursor.commit()
#
# # 回滚操作，相当于没有进行操作
# db.rollback()
#
#
# #--------------------------------------------
# # 插入数据
# data = {
#     "id":"23233",
#     "name":"Bod",
#     "age":20
# }
# table = "student"
# keys = ",".join(data.keys())
# values = ",".join(['%s']*len(data))
# sel = "insert into {table}({keys}) values ({values})".format(table = table,keys = keys, values = values)
# try:
#     db = pymysql.connect(host = "localhost", port = 3306, password = "123456", user = "root", db = "travel")
#     cursor = db.cursor()
#     if cursor.execute(sql,tuple(data.values())):
#         print("successful")
#         db.commit()
# except:
#     print("filed")
#     db.rollback()
# finally:
#     db.close()
#
# # 获取自动增长列的值
# id = connect.insert_id()
#
# print(connect.affected_rows())


#---------------------------------
# 查询
db = pymysql.connect(host = "localhost", port = 3306, user = "root", password = "123456", db = "school")

cursor = db.cursor()
sql = "select * from student where sname = '{0}'".format('李丽丽')
cursor.execute(sql)
print(cursor)
print("count：",cursor.rowcount) # 获取查询结果的条数
one = cursor.fetchone() # 获取第一行数据
print("one:",one)
for uu in one:
    print(uu)
row_2 = cursor.fetchmany(3) # 获取前3行数据
result = cursor.fetchall() # 获取所有数据


db.close()
cursor.close()