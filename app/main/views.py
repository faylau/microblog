# coding=utf-8

"""

"""

from flask import render_template, flash, session, redirect, url_for

from . import main
from app.main.forms import LoginForm
# from app.database import db_session


# @main.teardown_request
# def shutdown_session(exception=None):
#     db_session.remove()



@main.route('/')
@main.route('/index')
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
    if 'username' in session:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        error = None
        session['remember_me'] = form.remember_me.data
        from app.models import User
        u = User.query.filter(User.username == form.username.data).one()
        print u
        if u is not None and form.password.data == u.password:
            flash('Welcome {0}!'.format(u.username))
            session['user_name'] = u.username
            return redirect(url_for('.index'))
        elif u is None:
            error = 'User <{0}> does not exist.'.format(u.username)
        else:
            error = 'Password is incorrect.'
        return render_template('login.html', title='Sign In', form=form,
                               error=error)
    return render_template('login.html', title='Sign In', form=form)
