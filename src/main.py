# coding=utf-8
import importlib

from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from config import Config
from util import init_query_dict
from apis.statistics import Statistics
from apis.concept import Concept
from apis.person import Person
from apis.visit import Visit
from apis.condition import Condition
from apis.drug import Drug

# flask
app = Flask(__name__)
# flask app에 config 적용
app.config.from_object(Config)
# 쿼리 저장
init_query_dict()
# api
api = Api(app)
swagger = Swagger(app, config=app.config['SWAGGER_CONFIG'])
api.add_resource(Statistics, '/api/v1/Statistics', endpoint='Statistics')
api.add_resource(Concept, '/api/v1/Concept', endpoint='Concept')
api.add_resource(Person, '/api/v1/Person', endpoint='Person')
api.add_resource(Visit, '/api/v1/Visit', endpoint='Visit')
api.add_resource(Condition, '/api/v1/Condition', endpoint='Condition')
api.add_resource(Drug, '/api/v1/Drug', endpoint='Drug')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)