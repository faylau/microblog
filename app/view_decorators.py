# coding=utf-8

from functools import wraps
from flask import redirect, url_for, g


def log_required(fn):
    """
    :summary: 过滤未登录用户的装饰器
    :param f:
    :return:
    """
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return fn(*args, **kwargs)
    return decorated_function

