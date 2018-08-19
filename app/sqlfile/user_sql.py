


# 与用户相关的sql语句
usersql = {
    "searchUserById": "select * from user where id = {0}",
    "searchUserByTelephone": "select * from user where telephone = {0}",
    "addUser": "insert into user (telephone, password, email, province, city, street, regist_date) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','{6}','{7}' )",
}