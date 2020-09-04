# -*- coding = utf-8 -*-
# @Time: 2020/9/4 18:53
# @Author: dimples_yj
# @File: index.py
# @Software: PyCharm
from indexpy.http.responses import TemplateResponse
from indexpy.routing import Routes
from utils.db import database

index_routes = Routes(http_middlewares=[])


@index_routes.http("/", name="index", method="get")
async def index(request):
    return TemplateResponse("index.html", {"request": request, "author": "dimples_yj"})


@index_routes.http("/all", name="get-all", method="get")
async def get_all(request):
    query = "select * from cst_customer"
    result = await database.fetch_all(query=query)
    list = [tuple(i) for i in result]
    return {"msg": "查询成功", "data": list}
