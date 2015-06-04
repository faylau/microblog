# coding=utf-8

from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """

    """
    # 表单验证函数 DataRequired() 用于防止提交空数据
    # openid = StringField('openid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)