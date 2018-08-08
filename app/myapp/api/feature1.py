from flask_restful import reqparse, abort, Resource
from flask_httpauth import HTTPBasicAuth
from ..extensions import auth, mongo
from datetime import datetime, date, timedelta as td
import json
from flask import Response

class Feature1(Resource):
    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('date', required=True, help="date cannot be blank!")
        args = parser.parse_args()
        date = args['date']
        # mycollection = mongo.db.mycollection
        
        return Response({
            "success": True
        },  mimetype='application/json')