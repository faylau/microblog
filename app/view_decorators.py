# coding=utf-8

from functools import wraps
from flask import redirect, url_for, g


def log_required(f):
    """
    :summary: 过滤未登录用户的装饰器
    :param f:
    :return:
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('.login'))
        return f(*args, **kwargs)
    return decorated_function

