# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:51
# Email: Hyattsoft@sina.com
# FileName: base_settings.py

DEBUG = True

DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'hyatt'
PASSWORD = 'Tt20130325!'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'cater_shop'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_BINDS = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
