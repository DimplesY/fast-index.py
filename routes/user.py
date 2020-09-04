# -*- coding = utf-8 -*-
# @Time: 2020/9/4 21:48
# @Author: dimples_yj
# @File: user.py
# @Software: PyCharm
from indexpy.routing import Routes
from utils.jwtUtil import *
from utils.db import database
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user_routes = Routes()


@user_routes.http('/login', name="user-login", method='post')
async def user_login(request):
    """
    用户登录接口
    """
    login_p = await request.form()
    username = login_p['username']
    password = login_p['password']
    if username == 'admin' and password == '123456':
        user = {'username': username}
        token = create_access_token(user)
        return {"msg": "登录成功", 'token': token}


@user_routes.http('/register', name="user-register", method='post')
async def user_reg(request):
    """
    用户注册接口
    """
    user_info = await request.form()
    user = {"cust_address": user_info['username'], "cust_industry": pwd_context.hash(user_info['password'])}
    sql = "insert into cst_customer(cust_address,cust_industry) values (:cust_address,:cust_industry)"
    isS = await database.execute(sql, values=user)
    if isinstance(isS, int):
        return {"msg": "注册成功"}
