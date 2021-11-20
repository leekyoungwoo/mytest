# coding=utf-8
import importlib

# from flasgger import Swagger
from config import Config
from flask import Flask
from flask_restful import Api

from apis.time import Time

# flask
app = Flask(__name__)
# flask app에 config 적용
app.config.from_object(Config)

# api
api = Api(app)
api.add_resource(Time, '/api/v1/Time', endpoint='Time')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])