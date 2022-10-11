from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from config import config


bootstrap = Bootstrap()
mail = Mail()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)

    from .send_message import email
    app.register_blueprint(email)

    return app
