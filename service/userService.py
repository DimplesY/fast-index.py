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


def userLogin(username: str, password: str):
    """
    用户登录业务
    :param username: 注册的账号
    :param password: 注册的密码
    :return: jwt
    """
    if username == 'admin' and password == '123456':
        user = {'username': username}
        token = create_access_token(user)
        return token


async def userRegister(user_info: Dict):
    """
    用户注册
    :param user_info: 注册的用户信息
    :return: 是否注册成功
    """
    user = {"cust_address": user_info['username'], "cust_industry": pwd_context.hash(user_info['password'])}
    sql = "insert into cst_customer(cust_address,cust_industry) values (:cust_address,:cust_industry)"
    isS = await database.execute(sql, values=user)
    return isinstance(isS, int)
