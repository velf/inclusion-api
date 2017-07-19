from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Results(Resource):
    def get(self):
        return {'test': 'hola'} # Fetches first column that is Employee ID

api.add_resource(Results, '/results')

if __name__ == '__main__':
     app.run(port='5002')
