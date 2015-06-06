#encoding:utf-8


"""
V0.1    创建应用对象，导入视图模块；
"""

# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)

# 从config.py中读取配置信息
# app.config.from_object('config')

# 使用SQLAlchemy初始化数据库（根据app.config.from_object('config')读取db配置信息）
# db = SQLAlchemy(app=app)


import os
from flask import Flask
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


# bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)

    # register blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')