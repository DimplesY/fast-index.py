# -*- coding = utf-8 -*-
# @Time: 2020/9/4 18:53
# @Author: dimples_yj
# @File: index.py
# @Software: PyCharm
from indexpy.http.responses import TemplateResponse
from indexpy.routing import Routes
from utils.db import database
from middleware.authMiddleware import authMiddleware

index_routes = Routes(http_middlewares=[authMiddleware])


@index_routes.http("/", name="index", method="get")
async def index(request):
    return TemplateResponse("index.html", {"request": request, "author": "dimples_yj"})


@index_routes.http("/all", name="get-all", method="get")
async def get_all(request, userinfo):
    query = "select id,username from sys_user"
    result = await database.fetch_all(query=query)
    # list = [tuple(i) for i in result]
    list = []
    for item in result:
        data = dict()
        data["id"] = item[0]
        data["username"] = item[1]
        list.append(data)

    return {"msg": "查询成功", "data": list}


@index_routes.http("/user", name="index-user", method="get")
async def user(request, userinfo):
    return f"当前登录的用户是{userinfo}"
