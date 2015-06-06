#coding=utf-8

"""
Blueprint的错误处理
1. 在蓝图中写错误处理的不同之处是，如果使用了errorhandler装饰器，则只会调用在蓝图中
引起的错误处理；而应用程序范围内的错误处理则必须使用app_errorhandler。
"""

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    from app.database import db_session
    db_session.rollback()
    return render_template('500.html'), 500
