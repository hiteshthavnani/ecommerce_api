from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

# @app.route('/')
class home(Resource):

    def get(self):
        return {'Hello': 'world'}


api.add_resource(home, '/')


app.run()