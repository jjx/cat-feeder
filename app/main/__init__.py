from __future__ import absolute_import

from flask import Flask

from app.main.config import config_by_name


def create_app(env='prod'):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_by_name[env])

    with app.app_context():
        return app
