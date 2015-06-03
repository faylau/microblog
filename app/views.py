# coding=utf-8

"""

"""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Andy'}
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Beijing!'},
        {'author': {'nickname': 'Susan'},
         'body': 'Beautiful day in Wuhan!'},
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 提交请求时调用表单的 validate_on_submit() 方法，它会从请求中获取所有提交的
    # 数据，然后使用表单字段中绑定的验证函数进行数据验证。
    if form.validate_on_submit():
        flash('Login requested for OpenID={0}, remember_me={1}'
              .format(form.openid.data, str(form.remember_me.data)))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
