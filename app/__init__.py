from flask import Flask

from .extensions import rest_api, db
from .api import rest_api_ns

def create_app():
    flask_app = Flask(__name__)

    rest_api.init_app(flask_app)

    rest_api.add_namespace(rest_api_ns)

    return flask_app