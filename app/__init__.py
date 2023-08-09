from flask import Flask

from .extensions import rest_api, db


def create_app():
    flask_app = Flask(__name__)

    rest_api.init_app(flask_app)

    return flask_app