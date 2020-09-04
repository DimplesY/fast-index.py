# -*- coding = utf-8 -*-
# @Time: 2020/9/4 19:23
# @Author: dimples_yj
# @File: jwtUtil.py
# @Software: PyCharm
import jwt
import datetime


ALGORITHM = 'HS256'
SECRET = 'sadjdasidhfdsfsfdyyashdaishdia&'
ISSUER = 'dimples_yj'

dic = {
    'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
    'iat': datetime.datetime.now(),  # 开始时间
    'iss': ISSUER,  # 签名
}


def create_access_token(data: dict):
    dic['data'] = data
    token = jwt.encode(data, SECRET, algorithm=ALGORITHM)
    return token.decode('utf-8')


def get_user_info(token: str):
    return jwt.decode(token, SECRET, ISSUER, ALGORITHM)


if __name__ == '__main__':
    data = {"username": "dimples"}
    print(type(data))
    token = create_access_token(data)
    print(token)
    user_info = get_user_info(token)
    print(user_info)
