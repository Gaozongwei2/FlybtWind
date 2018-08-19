from app.dao import *


# 通过用户telephone查找
def getUserByTelephone(usertelephone):
    connect = createconnect()
    sql = "select * from user where telephone = '{0}'".format(usertelephone)
    cursor = connect.cursor()
    result = cursor.execute(sql)
    if result:
        result = list(cursor.fetchone())
        print(result)
        return result
    else:
        return result

    # if result:
    #     return result  # 该用户ID存在
    # else:
    #     return 0  # 该用户ID存在
#
# user = "15776554504"
# getUserByTelephone(user)
