# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:59
# Email: Hyattsoft@sina.com
# FileName: global_route.py
from application import app
from controllers import home_route


app.register_blueprint(home_route, url_prefix="/")