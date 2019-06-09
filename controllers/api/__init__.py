# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:57
# Email: Hyattsoft@sina.com
# FileName: __init__.py.py
from flask import Blueprint

blue_api = Blueprint("blue_api", __name__)


@blue_api.route("/")
def index():
    return "欢迎使用，凯悦云餐饮管理系统API接口"
