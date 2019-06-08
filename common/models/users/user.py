# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 17:39
# Email: Hyattsoft@sina.com
# FileName: user.py
from application import db


class User(db.Model):
    __tablename__ = "sys_user"
    code = db.Column(db.String(6), primary_key=True, comment="编码")
    nick_name = db.Column(db.String(20), comment="姓名", nullable=False)
    login_name = db.Column(db.String(20), unique=True, comment="登陆名称", nullable=False)
    login_pass = db.Column(db.String(32), comment="登陆密码", nullable=False)
    isDownload = db.Column(db.Integer, default=0, comment="是否可下载", nullable=False)
    isServices = db.Column(db.Integer, default=0, comment="是否服务员", nullable=False)
