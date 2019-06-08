# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:52
# Email: Hyattsoft@sina.com
# FileName: manager.py
from application import app, manager
from flask_script import Server
import global_route


manager.add_command("runserver", Server(port=8999))


def app_run():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(app_run())
    except Exception as e:
        import traceback
        traceback.print_exc()
