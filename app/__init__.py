# encoding:utf-8


"""
V0.1    创建应用对象，导入视图模块；
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 从config.py中读取配置信息
app.config.from_object('config')

# 使用SQLAlchemy初始化数据库（根据app.config.from_object('config')读取db配置信息）
db = SQLAlchemy(app=app)

from app import views, models