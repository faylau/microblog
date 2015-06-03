# coding=utf-8

from app import db
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, \
    ForeignKey
from database import Base

ROLE_USER = 0
ROLE_ADMIN = 1

class User(Base):
    """
    :summary:
    """
    __tablename__ = 't_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    role = Column(SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Posts(Base):
    """
    :summary:
    """
    __tablename__ = 't_posts'

    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('t_users.id'))
