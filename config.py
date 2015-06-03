#coding=utf-8

"""
该配置文件在__init__.py中读取
"""

import os

# CSRF_ENABLED 配置是为了激活跨站点请求伪造保护。
SCRF_ENABLED = True

# SECRET_KEY配置仅仅当CSRF激活的时候才需要，建立一个加密的令牌，用于验证一个表单。
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

# sqlite数据库文件路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# 存储SQLALCHEMY-migrate数据库文件的文件夹
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')