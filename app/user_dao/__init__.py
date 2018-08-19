import pymysql

# 建立数据库连接
def createconnect():
    db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="travel")
    return db
# 用来进行异常处理的方法
def check(func):
    def inner(*args):
        try:
            connect = None
            func(*args)
            return func()
        except Exception as ex:
            print(ex)
        finally:
            if connect:
                connect.close()
    return inner
# 获取操作游标
# cursor = db.cursor()
# 通过游标进行操作，执行sql语句
# cursor.execute()
# try:
#     def createconnect(sql):
#         pass
#
# except Exception as ex:
#     print(ex)
