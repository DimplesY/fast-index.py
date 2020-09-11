# -*- coding = utf-8 -*-
# @Time: 2020/9/4 21:48
# @Author: dimples_yj
# @File: user.py
# @Software: PyCharm
from indexpy.routing import Routes
# service
from service.userService import userLogin, userRegister

user_routes = Routes()


@user_routes.http('/login', name="user-login", method='post')
async def user_login(request):
    """
    用户登录接口
    """
    login_p = await request.form()
    username = login_p['username']
    password = login_p['password']
    token = await userLogin(username, password)
    return {"msg": "登录成功", 'token': token}


@user_routes.http('/register', name="user-register", method='post')
async def user_reg(request):
    """
    用户注册接口
    """
    user_info = await request.form()
    is_success = await userRegister(user_info)
    if is_success:
        return {"msg": "注册成功"}
    return {"msg": "注册失败"}
