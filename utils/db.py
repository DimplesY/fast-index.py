# -*- coding = utf-8 -*-
# @Time: 2020/9/4 20:39
# @Author: dimples_yj
# @File: db.py
# @Software: PyCharm
from databases import Database


DATABASE_URL = "mysql://root:yanjie@localhost:3306/jpa?min_size=5&max_size=20"
database = Database(DATABASE_URL)

