# coding=utf-8

"""
1. SQLAlchemy-migration现在是openstack社区维护的一个项目，主要用于实现SQLAlchemy相
关数据误置的创建、版本管理、迁移等功能；它对SQLAlchemy的版本有一定要求；它对于一般项
目而言并不是必需的；
2. 下面的db_create、db_migrate、db_upgrade、db_downgrade等方法均使用SQLAlchemy-
migration实现；
3. 如果不需要实现数据库版本管理及迁移，可以不使用SQLAlchemy-migration。
"""

import os.path

from migrate.versioning import api
import imp
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import db

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)

init_db()

# def db_create():
#     """
#     :summary: 使用SQLAlchmy-migration进行数据库创建及版本管理
#     """
#     db.create_all()
#     if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#         api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#         api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     else:
#         api.version_control(SQLALCHEMY_DATABASE_URI,
#                             SQLALCHEMY_MIGRATE_REPO,
#                             api.version(SQLALCHEMY_MIGRATE_REPO))
#
#
# def db_migrate():
#     """
#     :summary: SQLAlchemy-migrate 迁移的方式就是比较数据库(在本例中从app.db中获取)
#     与我们模型的结构(从文件 app/models.py 获取)；两者间的不同将会被记录成一个迁移
#     脚本存放在迁移仓库中；迁移脚本知道如何去迁移或撤销它，所以它始终是可能用于升级
#     或降级一个数据库。
#     """
#     migration = SQLALCHEMY_MIGRATE_REPO\
#                 + '/versions/%03d_migration.py' \
#                 % (api.db_version(SQLALCHEMY_DATABASE_URI,
#                                   SQLALCHEMY_MIGRATE_REPO) + 1)
#     tmp_module = imp.new_module('old_model')
#     old_model = api.create_model(SQLALCHEMY_DATABASE_URI,
#                                  SQLALCHEMY_MIGRATE_REPO)
#     exec old_model in tmp_module.__dict__
#     script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
#                                               SQLALCHEMY_MIGRATE_REPO,
#                                               tmp_module.meta,
#                                               db.metadata)
#     open(migration, 'wt').write(script)
#     api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     print 'New migration saved as {0}.'.format(migration)
#     print 'Current database version: {0}'.format(
#         str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
#     )
#
#
# def db_upgrade():
#     """
#     :summary: 数据库升级，使用SQLAlchemy-migration实现。
#     """
#     api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     print 'Current database version: ' + str(
#         api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     )
#
#
# def db_downgrade():
#     """
#     :summary: 数据库降级，使用SQLAlchemy-migration实现。
#     """
#     v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
#     print 'Current database version: ' + str(
#         api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#     )


if __name__ == '__main__':
    init_db()
