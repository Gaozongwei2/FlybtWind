from app.service import *


# 用户登录
def user_login_service():
    user = {
        "telephone": request.values["telephone"],
        "password": request.values["password"]
    }
    # 判断输入条件不能为空
    if user["telephone"] and user["password"]:
        re = getUserByTelephone(user["telephone"])
        # 判断用户是否存在
        if re:
            # 判断密码是否符合

            if check_password_hash(re[2], user["password"]):
                result = "欢迎回来: " + re[1]
            else:
                result = "密码错误"
        else:
            result = "该用户不存在"
    else:
        result = "输入条件不能为空"
    return result


# 用户注册
def user_regist_service(request):  # 将用户的注册信息装入user字典
    # user = {
    #     "telephone": request.values["telephone"],
    #     "password": request.values["password"],
    #     "repassword": request.values["repassword"],
    #     "email": request.values["email"]
    # }
    # user = {
    #     "telephone": request["telephone"],
    #     "password": request["password"],
    #     "repassword": request["repassword"],
    #     "email": request["email"]
    # }
    telephone = request.values["telephone"]
    password = request.values["password"]
    repassword = request.values["repassword"]
    email = request.values["email"]
    # 判断输入条件不能为空
    if telephone and password:
        # 判断此密码输入是否一致
        if password == repassword:
            # 查询用户名是否存在
            re = getUserByTelephone(telephone)
            if re:
                result = "该用户名已存在"
            else:
                password = generate_password_hash(password, method='pbkdf2:sha1:2000', salt_length=8)
                # 执行注册的插入操作
                result = addUser({"telephone": telephone, "password": password, "repassword":repassword, "email":email})
                if result:
                    # 签发token
                    token = addtoken(telephone).decode()
                    print(token)
                    return json.jsonify({"statuscode": "202"}), 200, {"token": token}
                else:
                    return "注册失败"
        else:
            result = "两次密码输入不一致"
    else:
        result = "用户名或密码为空"
    return result


# 修改密码
def user_pswfix_service():
    print("here")
    # token = str(request.headers["token"])
    # 解析token
    token = analysis()
    if token:
        # 证明用户已经登录，进行修改密码的操作

        telephone = token[""]
        password = {
            "password": request.values["password"],
            "repassword": request.values["repassword"]
        }
        if password["password"] and password["repassword"]:
            if password["password"] == password["repassword"]:
                pass
        else:
            result = 0

    return result


# userLogin
def logIn():

    user = {
        "telephone":request.values["telephone"],
        "password": request.values["password"]
    }

    result = logIn()

    pass