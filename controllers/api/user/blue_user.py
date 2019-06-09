# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/10 6:07
# Email: Hyattsoft@sina.com
# FileName: blue_user.py
from flask import Blueprint, jsonify, make_response
from common.libs.methods import to_data
from common.models.users.user import User
import json


blue_user = Blueprint("blue_user", __name__)


@blue_user.route("/login", methods=["POST"])
def login():
    resp = {{'code': 200}, {"msg": "登陆成功"}, {"data": {}}}
    data = to_data()
    login_name = data["login_name"]
    login_pass = data["login_pass"]
    if login_name is None or len(login_name) < 1:
        resp["code"] = -1
        resp["msg"] = "请输入正确的登陆名称"
        return jsonify(resp)
    if login_pass is None or len(login_pass) < 1:
        resp['code'] = -1
        resp["msg"] = "请输入正确的登陆密码"
        return jsonify(resp)
    user = User.query.filterby(login_name=login_name).first()
    if not user:
        resp["code"] = -1
        resp["msg"] = "请输入正确的登陆名称及密码"
        return jsonify(resp)

    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    return response


