#coding=utf-8

"""
该配置文件在__init__.py中读取
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    :summary:
    """
    SCRF_ENABLED = True     # 激活跨站点请求伪造保护
    # SECRET_KEY配置仅仅当CSRF激活的时候才需要，建立一个加密的令牌用于验证表单。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    :summary:
    """
    DEBUG = True

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class TestingConfig(Config):
    """
    :summary:
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir,
                                                          'data-test.db')


class ProductionConfig(Config):
    """
    :summary:
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.db')


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}