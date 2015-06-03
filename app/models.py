# coding=utf-8

from app import db
from sqlalchemy import Column, Integer, String, SmallInteger

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    """
    :summary:
    """
    __tablename__ = 't_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    role = Column(SmallInteger, default=ROLE_USER)

    # def __init__(self, name=None, email=None, role=ROLE_USER):
    #     self.name = name
    #     self.email = email
    #     self.role = role

    def __repr__(self):
        return '<User %r>' % (self.name)
