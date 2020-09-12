# -*- coding = utf-8 -*-
# @Time: 2020/9/4 21:48
# @Author: dimples_yj
# @File: user.py
# @Software: PyCharm
from indexpy.routing import SubRoutes
# service
from service.userService import userLogin, userRegister
import gvcode
import redis
import uuid

user_routes = SubRoutes("/user")
r = redis.Redis(host="localhost", port=6379, decode_responses=True)


@user_routes.http('/login', name="user-login", method='post')
async def user_login(request):
    """
    用户登录接口
    """
    login_p = await request.json()
    username = login_p['username']
    password = login_p['password']
    verify_key = login_p['verify_key']
    code = login_p['code']
    verify_code = r.get(verify_key)
    r.delete(verify_key)
    if str(code).upper() == verify_code:
        token = await userLogin(username, password)
        if token:
            return {"msg": "登录成功", "data": {"token": token}, "code": 2000}
        else:
            return {"msg": "登录失败!账号或密码错误"}
    return {"msg": "登录失败!验证码错误"}


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


@user_routes.http('/captcha', name='captcha', method='get')
async def get_captcha(request):
    """
    获取验证码接口,60秒过期
    """
    captcha_id = str(uuid.uuid4())
    image, code = gvcode.base64()
    r.set(captcha_id, code.upper(), ex=60)
    return {"msg": "请求成功", "data": {"captcha": image, "verify_key": captcha_id},
            "code": 2000}
