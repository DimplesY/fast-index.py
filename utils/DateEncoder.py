# -*- coding = utf-8 -*-
# @Time: 2020/9/4 22:00
# @Author: dimples_yj
# @File: DateEncoder.py
# @Software: PyCharm
import json

import datetime


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)
