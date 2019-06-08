# -*- coding:utf8 -*-
# Author: HyattSoft
# Date: 2019/6/8 16:41
# Email: Hyattsoft@sina.com
# FileName: application.py
from flask import Flask
from flask_script import Manager
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
import os


class Application(Flask):
    def __init__(self, import_name, template_folder, root_path, static_folder):
        super(Application, self).__init__(import_name=import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=static_folder)
        self.config.from_pyfile("config/base_settings.py")
        if "ops_config" in os.environ:
            self.config.from_pyfile("config/%s_settings.py" % os.environ["ops_config"])
        # db.init_app(self)


# db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd()+"/front_end/dist", root_path=os.getcwd(),
                  static_folder=os.getcwd()+"/front_end/dist/static")
manager = Manager(app)
# migrate = Migrate(app, db)