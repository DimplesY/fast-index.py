# -*- coding = utf-8 -*-
# @Time: 2020/9/6 0:10
# @Author: dimples_yj
# @File: userService.py
# @Software: PyCharm
from utils.jwtUtil import *
from utils.db import database
from typing import Dict
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def userLogin(username: str, password: str):
    """
    用户登录业务
    :param username: 注册的账号
    :param password: 注册的密码
    :return: jwt
    """
    sql = "select username,password from sys_user where username= :username"
    user_info = await database.fetch_one(query=sql, values={"username": username})
    if username == user_info[0] and pwd_context.verify(password, user_info[1]):
        user = {'username': username}
        token = create_access_token(user)
        return token


async def userRegister(user_info: Dict):
    """
    用户注册
    :param user_info: 注册的用户信息
    :return: 是否注册成功
    """
    user = {"username": user_info['username'], "password": pwd_context.hash(user_info['password'])}
    sql = "insert into sys_user(username,password) values (:username,:password)"
    isS = await database.execute(query=sql, values=user)
    return isinstance(isS, int)
