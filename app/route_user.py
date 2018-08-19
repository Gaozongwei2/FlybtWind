from flask import Blueprint, session, render_template, redirect
from app.user_dao.user_search import *
from app.service.userService.user_service import *

user_app = Blueprint("userapp", __name__)


# 用户首页
@user_app.route("/")
def index():
    return "用户首页"


# 用户登录
@user_app.route("/login", methods=["GET", "POST"])
def login():
    # 获取method
    md = str(request.method).upper()
    if md == "GET":
        # 跳转到登录界面
        return "用户登录"
    elif md == "POST":
        result = user_login_service()
        return result


# 用户注册
@user_app.route("/regist", methods=["GET", "POST"])
def regist():
    md = str(request.method).upper()
    if md == "POST":
        # 调用用户注册service
        print("haha")
        result = user_regist_service(request)
        return result
    elif md == "GET":
        return "用户登录"


@user_app.route("/pswfix", methods=["GET", "POST"])
def pswfix():
    md = str(request.method).upper()
    if md == "GET":
        return "修改密码"
    elif md == "POST":
        result = user_pswfix_service()
        return result


# 推出登录
@user_app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
