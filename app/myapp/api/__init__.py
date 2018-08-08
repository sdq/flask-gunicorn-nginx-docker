from flask import Blueprint
from flask_restful import Api
from ..extensions import auth
from feature1 import Feature1
from feature2 import Feature2

users = {
    "admin": "admin"
}

api_blueprint = Blueprint("myapp", __name__)
api = Api(app_blueprint)

api.add_resource(Feature1, '/feature1')
api.add_resource(Feature2, '/feature2')

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None