from app.dao import *
from datetime import datetime


# 添加用户
def addUser(user):
    result = None
    registtime = datetime.now().date()
    connect = createconnect()
    sql = "insert into user (telephone, password, email, regist_date) " \
          "values ('{0}','{1}','{2}', '{3}')" \
        .format(user['telephone'], user['password'], user['email'], registtime)
    cursor = connect.cursor()
    result = cursor.execute(sql)
    if result:
        connect.commit()
        return result
    else:
        connect.rollback()
    return result

# user = {
#     "telephone":"15776554544",
#     "password":"123456",
#     "email":"2312@23.com"
# }

# print(addUser(user))
