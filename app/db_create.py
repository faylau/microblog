# coding=utf-8

import os.path

from migrate.versioning import api
import imp
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import db


def db_create():
    db.create_all()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI,
                            SQLALCHEMY_MIGRATE_REPO,
                            api.version(SQLALCHEMY_MIGRATE_REPO))


def db_migrate():
    """
    SQLAlchemy-migrate 迁移的方式就是比较数据库(在本例中从app.db中获取)与我们模型
    的结构(从文件 app/models.py 获取)；两者间的不同将会被记录成一个迁移脚本存放在
    迁移仓库中；迁移脚本知道如何去迁移或撤销它，所以它始终是可能用于升级或降级一个
    数据库。
    :return:
    """
    migration = SQLALCHEMY_MIGRATE_REPO\
                + '/versions/%03d_migration.py' \
                % (api.db_version(SQLALCHEMY_DATABASE_URI,
                                  SQLALCHEMY_MIGRATE_REPO) + 1)
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI,
                                 SQLALCHEMY_MIGRATE_REPO)
    exec old_model in tmp_module.__dict__
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                              SQLALCHEMY_MIGRATE_REPO,
                                              tmp_module.meta,
                                              db.metadata)
    open(migration, 'wt').write(script)
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print 'New migration saved as {0}.'.format(migration)
    print 'Current database version: {0}'.format(
        str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
    )


def db_upgrade():
    """
    :summary: 数据库升级
    :return:
    """
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print 'Current database version: ' + str(
        api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    )


def db_downgrade():
    """
    :summary: 数据库降级
    :return:
    """
    v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)
    print 'Current database version: ' + str(
        api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    )

if __name__ == '__main__':
    db_create()
