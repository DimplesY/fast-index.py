# -*- coding = utf-8 -*-
# @Time: 2020/9/4 19:23
# @Author: dimples_yj
# @File: jwtUtil.py
# @Software: PyCharm
from typing import Optional

import jwt
from datetime import datetime, timedelta

ALGORITHM = 'HS256'
SECRET_KEY = 'sadjdasidhfdsfsfdyyashdaishdia&'
ISSUER = 'dimples_yj'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(microseconds=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt.decode()


def get_user_info(token: str):
    return jwt.decode(token, SECRET_KEY, ISSUER, ALGORITHM)


if __name__ == '__main__':
    data = {"username": "dimples"}
    print(type(data))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data, access_token_expires)
    print(token)
    user_info = get_user_info(token)
    print(user_info)
