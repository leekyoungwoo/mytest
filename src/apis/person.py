# coding=utf-8
import os

from flasgger import swag_from
from flask_restful import Resource

from util import use_db, use_p, query, QUERY
from config import Config
from jinja_sql import JinjaSql
SQL = JinjaSql(param_style='pyformat')


class Person(Resource):

    def __init__(self):
        self.db = use_db()
        self.p = use_p()

    @swag_from(os.path.join(Config.ROOT_DIR, 'swagger', 'get_person.yaml'))
    def get(self):
        p = self.p

        params = {
            'offset': int(p['page']) * 10 if 'page' in p and p['page'] else 0,
            'limit': 10,
            **p
        }
        sql, bind_param = SQL.prepare_query(QUERY['person.yaml'], '환자 정보 조회', params)
        patient = query(self.db, sql, bind_param)
        return patient

