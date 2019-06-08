# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:52
# Email: Hyattsoft@sina.com
# FileName: manager.py
from application import app, manager, db
from flask_script import Server, Shell
from flask_migrate import MigrateCommand
from common.models.users.user import User
import global_route


def make_shell_context():
    return dict(app=app, db=db, user=User)


manager.add_command("runserver", Server(port=8999))
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


def app_run():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(app_run())
    except Exception as e:
        import traceback
        traceback.print_exc()
