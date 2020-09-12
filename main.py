# -*- coding = utf-8 -*-
# @Time: 2020/9/4 18:51
# @Author: dimples_yj
# @File: main.py
# @Software: PyCharm
from indexpy import Index
# 路由
from indexpy.http import Request
from indexpy.http.responses import Response, JSONResponse
from indexpy.openapi import OpenAPI
from jwt import ExpiredSignatureError
import redis

from routes.index import index_routes
from routes.user import user_routes
from utils.logger import AppLog
from utils.db import database

app = Index(templates=["templates"])
log = AppLog("test")

# openAPI 文档自动生成，不需要的可以注释掉
# app.mount_asgi(
#     "/v1",
#     OpenAPI("xxxx后端接口", "作者：dimples_yj", "0.1.0", tags={
#         "user": {
#             "description": "用户登录、注册接口",
#             "paths": ["/login", "/register"]
#         }
#     })
# )

app.router.extend(index_routes)
app.router.extend(user_routes)


@app.on_startup
async def app_startup():
    await database.connect()
    redis.ConnectionPool(host="127.0.0.1", port=6379, decode_responses=True)
    log.info("redis连接成功")
    log.info("数据库连接成功！")


@app.on_shutdown
async def app_shutdown():
    await database.disconnect()
    log.info("系统退出,数据库连接关闭！")


@app.exception_handler(ExpiredSignatureError)
def token_exp(request: Request, exc: ExpiredSignatureError) -> Response:
    resp = {"msg": "token过期", "code": 456}
    return JSONResponse(resp, status_code=456)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, interface="asgi3", host="127.0.0.1", port=8000)
