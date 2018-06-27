import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    SECRET_KEY = 'YmVybmFyZG8gZSp238sdFDFYWRvci4gTmFvIG1leGUgY29tIGVsZQ=='
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'postgres'
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )


class ProdConfig(Config):
    ENV = 'prod'
    CACHE_TYPE = 'simple'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
