#coding=utf-8

"""

"""

import pickle
from datetime import datetime

from flask import render_template, flash, session, redirect, url_for, g, request

from . import main
from app.main.forms import LoginForm, EditForm
# from app.database import db_session
from app.view_decorators import log_required


# @main.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()


@main.before_request
def before_request():
    if 'user' in session:
        g.user = pickle.loads(session['user'])
        g.user.last_seen = datetime.now()
        from app.database import db_session
        db_session.add(g.user)
        db_session.commit()
    else:
        g.user = None


@main.route('/')
@main.route('/index')
@log_required
def index():
    user = g.user
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Beijing!'},
        {'author': {'nickname': 'Susan'},
         'body': 'Beautiful day in Wuhan!'},
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@main.route('/login', methods=['GET', 'POST'])
def login():
    """
    :summary:
    :return:
    """
    form = LoginForm()

    if 'user' in session:
        # 使用blueprint后，index前加blueprint名称；
        return redirect(url_for('main.index'))

    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        from app.models import User
        u = User.query.filter(User.username == form.username.data).first()
        if u is not None and form.password.data == u.password:
            session['user'] = pickle.dumps(u)
            return redirect(url_for('.index'))
        else:
            error = 'Incorrect username or password. Please try again.'
            return render_template('login.html', title='Sign In',
                                   form=form, error=error)
    return render_template('login.html', title='Sign In', form=form)


@main.route('/logout')
@log_required
def logout():
    session.pop('user')
    flash('You have been logged out.')
    return redirect(url_for('main.login'))


@main.route('/user/<username>')
@log_required
def user(username):
    if g.user.username != username:
        return redirect(url_for('.index'))

    from app.models import User
    user = User.query.filter(User.username == username).first()
    if user is None:
        flash('不存在用户：{0}！'.format(username))
        return redirect(url_for('.index'))
    posts = [
        { 'author': user, 'body': 'Test post #1' },
        { 'author': user, 'body': 'Test post #2' }
    ]
    return render_template('user.html', user=user, posts=posts)


@main.route('/edit', methods=['GET', 'POST'])
@log_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        g.user.email = form.email.data
        from app.database import db_session
        db_session.add(g.user)
        db_session.commit()
        flash(u'您的修改已经保存生效')
        return redirect(url_for('main.user', username=g.user.username))
    else:
        form.nickname.data = g.user.nickname
        form.email.data = g.user.email
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)
