from . import *


# 签发token
def addtoken(user):
    option = {
        'iss': ISS,  # token的签发者
        'exp': datetimeInt,  # 过期时间
        'aud': AUD,  # token的接收者，这里指定为浏览器
        'user_id': user  # 放入用户信息，唯一标识，解析后可以使用该消息
    }
    token = jwt.encode(option, SECRECT_KEY, 'HS256')
    return token


# 解析token
def analysis():
    print("执行到这里")
    token = request.headers["token"]
    print(type(token))
    decoded = jwt.decode(str(token), SECRECT_KEY, audience='webkit', algorithms=['HS256'])
    print(decoded)
    decoded = json.jsonify(decoded) # 注意要进行类型转换，否则无法返回，return会报错,此时decode的类型为<class 'flask.wrappers.Response'>
    print(type(decoded))
    return decoded
