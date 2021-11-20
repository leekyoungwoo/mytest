# coding=utf-8
import os

from flasgger import swag_from
from flask_restful import Resource

from util import use_db, use_p, query, QUERY
from config import Config
from jinja_sql import JinjaSql
SQL = JinjaSql(param_style='pyformat')


class Statistics(Resource):

    def __init__(self):
        self.db = use_db()
        self.p = use_p()

    @swag_from(os.path.join(Config.ROOT_DIR, 'swagger', 'get_statistics.yaml'))
    def get(self):

        patient = query(self.db, QUERY['statistics.yaml']['환자 통계'], [])
        visit = query(self.db, QUERY['statistics.yaml']['방문 통계'], [])
        return {'patient': patient[0], 'visit': visit[0]}
