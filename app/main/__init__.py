# coding=utf-8

from flask import Blueprint

# create blueprint
main = Blueprint('main', __name__) 

from . import views, errors
