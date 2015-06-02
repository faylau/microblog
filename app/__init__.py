# encoding:utf-8


"""
V0.1    创建应用对象，导入视图模块；
"""

from flask import Flask

app = Flask(__name__)

# 从config.py中读取配置信息
app.config.from_object('config')

from app import views