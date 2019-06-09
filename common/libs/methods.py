# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/10 6:12
# Email: Hyattsoft@sina.com
# FileName: methods.py
from flask import request
import json


def to_data():
    data = json.loads(request.get_data().decode("utf-8"))
    if data:
        return data
    else:
        return {}
