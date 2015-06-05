# coding=utf-8

"""

"""

from flask import render_template, flash, session, redirect, url_for, g, request

from . import main
from app.main.forms import LoginForm
# from app.database import db_session
from app.view_decorators import log_required


# @main.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()


@main.before_request
def before_request():
    if 'user_name' in session:
        g.user = session['user_name']
    else:
        g.user = None


@main.route('/')
@main.route('/index')
@log_required
def index():
    # user = {'nickname': 'Andy'}
    user = {'user_name': session['user_name']}
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

    if request.method == 'GET':
        return render_template('login.html', title='Sign In', form=form)
    else:
        if 'user_name' in session:
            # 使用blueprint后，index前加blueprint名称；
            return redirect(url_for('main.index'))

        if form.validate_on_submit():
            session['remember_me'] = form.remember_me.data
            from app.models import User
            try:
                u = User.query.filter(User.username == form.username.data).one()
            except Exception:
                error = 'User <{0}> does not exist.'.format(form.username.data)
                return render_template('login.html', title='Sign In',
                                       form=form, error=error)
            else:
                if form.password.data == u.password:
                    session['user_name'] = u.username
                    return redirect(url_for('main.index'))
                else:
                    error = 'Password is incorrect.'
                    return render_template('login.html', title='Sign In',
                                           form=form, error=error)
        return render_template('login.html', title='Sign In', form=form)


@main.route('/logout')
def logout():
    pass
