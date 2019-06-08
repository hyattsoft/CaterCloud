# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:57
# Email: Hyattsoft@sina.com
# FileName: __init__.py.py
from flask import Blueprint, render_template

home_route = Blueprint("home_route", __name__)


@home_route.route("/")
def home():
    return render_template("index.html")
