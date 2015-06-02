# coding=utf-8

"""

"""

from flask import render_template
from app import app


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
