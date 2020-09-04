# -*- coding = utf-8 -*-
# @Time: 2020/9/4 18:51
# @Author: dimples_yj
# @File: main.py
# @Software: PyCharm
from indexpy import Index
# 路由
from indexpy.openapi import OpenAPI

from routes.index import index_routes
from routes.user import user_routes
from utils.logger import AppLog
from utils.db import database

app = Index(templates=["templates"])
log = AppLog("test")

app.mount_asgi(
    "/v1",
    OpenAPI("员工管理系统后端接口", "作者：dimples_yj", "0.1.0", tags={
        "user": {
            "description": "用户登录、注册接口",
            "paths": ["/login", "/register"]
        }
    })
)

app.router.extend(index_routes)
app.router.extend(user_routes)


@app.on_startup
async def app_startup():
    await database.connect()
    log.info("数据库连接成功！")


@app.on_shutdown
async def app_shutdown():
    await database.disconnect()
    log.info("系统退出,数据库连接关闭！")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, interface="asgi3", host="127.0.0.1", port=8000)
