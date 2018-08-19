import pymysql


# 建立数据库连接
def createconnect():
    db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="travel")
    return db
