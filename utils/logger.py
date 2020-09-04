# -*- coding = utf-8 -*-
# @Time: 2020/9/4 18:52
# @Author: dimples_yj
# @File: logger.py
# @Software: PyCharm
from enum import Enum

import logging


class AppLog:
    level = Enum('level',
                 {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR,
                  'critical': logging.CRITICAL})

    logger = None

    lvl = None

    def __init__(self, name):

        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.DEBUG)

        self.setLogHandle()

    def setLogHandle(self):
        import os
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if not os.path.exists(os.path.join(BASE_DIR, "log")):
            os.mkdir(os.path.join(BASE_DIR, "log"))
        fhandler = logging.FileHandler('log/app.log', 'a', 'utf-8')

        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

        fhandler.setFormatter(formatter)

        fhandler.setLevel(logging.DEBUG)

        console = logging.StreamHandler()

        console.setFormatter(formatter)

        console.setLevel(logging.INFO)

        self.logger.addHandler(fhandler)

        self.logger.addHandler(console)

    def __getattr__(self, name):

        if (name in ('debug', 'info', 'warn', 'error', 'critical')):

            self.lvl = self.level[name].value

            return self

        else:

            raise AttributeError('Attr not Correct')

    def __call__(self, msg):

        self.logger.log(self.lvl, msg)
