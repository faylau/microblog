#coding=utf-8

"""
该配置文件在__init__.py中读取
"""

# CSRF_ENABLED 配置是为了激活跨站点请求伪造保护。
SCRF_ENABLED = True

# SECRET_KEY配置仅仅当CSRF激活的时候才需要，建立一个加密的令牌，用于验证一个表单。
SECRET_KEY = 'you-will-never-guess'