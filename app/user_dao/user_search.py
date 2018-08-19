from . import *


# 查询用户
# @check
def usersearch(userid):
    result = None
    connent = createconnect()
    sql = "select * from user where telephone = '{0}'".format(userid)
    cursor = connent.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    if result:
        return result  # 该用户ID存在
        return 0  # 该用户ID存在
