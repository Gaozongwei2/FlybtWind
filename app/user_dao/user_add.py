from . import *
from datetime import datetime, timedelta


# @check
def useradd(user):
    result = None
    nowtime = datetime.now()
    connect = createconnect()
    print(user["telephone"])
    print(user["password"])
    sql = "insert into user (telephone, password, email, regist_date ) " \
          "values ('{0}', '{1}','{2}')" \
        .format(user["telephone"], user["password"], "lucky@gmail.com", nowtime)

    cursor = connect.cursor()
    result = cursor.execute(sql)

    print(cursor.execute(sql))
    if result:
        connect.commit()
        return 1
    else:
        return 0
