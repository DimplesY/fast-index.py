# -*- coding = utf-8 -*-
# @Time: 2020/9/4 20:39
# @Author: dimples_yj
# @File: db.py
# @Software: PyCharm
from databases import Database
from indexpy import Config


DATABASE_URL = Config().datasource_url
database = Database(DATABASE_URL)

