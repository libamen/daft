from flask import Flask
from flask_restful import Api

from config import DevConfig

app = Flask(__name__)


def create_app():
    configure_app(DevConfig)

    api = Api(app, prefix='/api')
    init_api(api)

    return app


def configure_app(config):
    """
    Fetch configuration.
    :param config: Config object.
    """
    app.config.from_object(config)


def init_api(api):
    """
    Fetches all the different parts of the api and initializes them.
    :param api: Flask_Restful api application.
    """
    from api import stock
    stock.init_api(api=api)
