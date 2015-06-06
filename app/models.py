#coding=utf-8

from hashlib import md5
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, \
    ForeignKey, create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from app import app
from database import Base, engine

print app.config
ROLE_USER = 0
ROLE_ADMIN = 1

# SQLALCHEMY_DATABASE_URI = 'sqlite:///E:\GitHub\microblog\data-dev.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=True)
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
#                        convert_unicode=True,
#                        echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
#
# Base = declarative_base()
# Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

class User(Base):
    """
    :summary:
    """
    __tablename__ = 't_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), index=True, unique=True, nullable=False)
    nickname = Column(String(40), index=True, unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(120), index=True, unique=True)
    role = Column(SmallInteger, default=ROLE_USER)
    posts = relationship('Post', backref='author', lazy='dynamic')
    about_me = Column(String(140))
    last_seen = Column(DateTime)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            version += 1
        return new_nickname

    # def is_authenticated(self):
    #     """ Use Flask-Login to deal with login, you must implement this method.
    #     """
    #     return True
    #
    # def is_active(self):
    #     """ Use Flask-Login to deal with login, you must implement this method.
    #     """
    #     return True
    #
    # def is_anonymous(self):
    #     """ Use Flask-Login to deal with login, you must implement this method.
    #     """
    #     return False
    #
    # def get_id(self):
    #     """ Use Flask-Login to deal with login, you must implement this method.
    #     Returned user id should be unicode type.
    #     """
    #     return unicode(self.id)


class Post(Base):
    """
    :summary:
    """
    __tablename__ = 't_posts'

    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('t_users.id'))

    def __repr__(self):
        return '<Post %s>' % self.body


if __name__ == "__main__":
    # init_db()
    # drop_db()
    # u1 = User(username='admin', nickname=u'系统管理员', password='111111',
    #           email='admin@qq.com', about_me='', role=ROLE_ADMIN)
    # u2 = User(username='andy', nickname=u'D调的华丽', password='111111',
    #           email='andy@qq.com', about_me='', role=ROLE_USER)
    # db_session.add(u1)
    # db_session.add(u2)
    # db_session.commit()
    pass
