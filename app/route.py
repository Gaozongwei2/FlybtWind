from app.app import app
from flask import redirect, url_for, request, render_template

from .route_user import user_app

# 注册route_user蓝图
app.register_blueprint(user_app, url_prefix='/userapp')
# 首页
@app.route('/')
def index():
    return render_template("index.html")