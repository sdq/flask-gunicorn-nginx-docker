#!flask/bin/python
from flask import Flask, redirect
from flask_restful import Api
from flask_cors import CORS
from api import api_blueprint
from extensions import mongo
from config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=False) 
    CORS(app)
    with app.app_context():
        app.config.from_object(Config)
        # app.config.from_pyfile('config.py')
        mongo.init_app(app)
        app.register_blueprint(api_blueprint, url_prefix = '/api')
        return app

