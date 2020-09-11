# -*- coding = utf-8 -*-
# @Time: 2020/9/4 19:25
# @Author: dimples_yj
# @File: authMiddleware.py
# @Software: PyCharm
from utils.jwtUtil import *


def authMiddleware(endpoint):
    """
    用户认证中间件
    :param endpoint: toekn认证中间件
    :return:
    """

    async def oauth(request):
        try:
            token = request.headers['x-token']
            if token:
                user_info = get_user_info(token)
                if user_info:
                    respone = await endpoint(request, user_info)
                return respone
        except KeyError:
            return {"msg": "请登录后再访问", "code": 403}

    return oauth
