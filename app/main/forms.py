#coding=utf-8

from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    """
    :summary: 用户登录的Form
    """
    # 表单验证函数 DataRequired() 用于防止提交空数据
    # openid = StringField('openid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    """
    :summary: 用户编辑个人资料的Form
    """
    nickname = StringField('nickname', validators=[DataRequired()])
    email = StringField('email', validators=[Email(), DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        """
        :summary: 初始化方法
        :param original_nickname: 用户的原昵称
        :param args:
        :param kwargs:
        :return: Void
        """
        super(EditForm, self).__init__(*args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        """
        :summary: 重写validate方法，添加对于nickname字段的验重功能；
        :return: Boolean
        """
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        from app.models import User
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user is not None:
            self.nickname.errors.append(
                u'这个昵称已经被使用，请选择其他的昵称，如<{0}>。'
                    .format(User.make_unique_nickname(self.nickname.data)))
            return False
        return True

class RegisterForm(Form):
    """
    :summary:
    """
    username = StringField('username', validators=[DataRequired])
    nickname = StringField('nickname', validators=[DataRequired])
    email = StringField('email', validators=[Email, DataRequired])
    password = PasswordField('password', validators=[DataRequired])
    confirm_password = PasswordField('confirm_password',
                                     validators=[DataRequired])

    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)

    def validate(self):
        """
        :summary: 重写validate方法，对username/nickname验重
        :return: Boolean
        """
        if not Form.validate(self):
            return False
        from app.models import User
        u1 = User.query.filter_by(username = self.username.data).first()
        if u1 is not None:
            self.username.errors.append(u'这个用户名已经被使用！')
            return False
        u2 = User.query.filter_by(nickname = self.nickname.data).first()
        if u2 is not None:
            self.nickname.errors.append(
                u'这个昵称已经被使用，请选择其他的昵称，如<{0}>。'
                    .format(User.make_unique_nickname(self.nickname.data)))
            return False
        if self.password != self.confirm_password:
            self.confirm_password.errors.append(
                u'两次输入的密码不一致，请重新输入！')
            return False
        return True
