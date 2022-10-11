import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'sendertestmail@yandex.ru'
    MAIL_PASSWORD = 'mugtpwxvxixctlrp'
    MAIL_DEFAULT_SENDER = 'sendertestmail@yandex.ru'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Artes228@localhost:5432/users"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Artes228@localhost:5432/users'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///send_message/develop.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
