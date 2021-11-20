# coding=utf-8
import os
import psycopg2
import yaml
from flask import request

from config import Config
from db import cursor
QUERY = {}


def init_query_dict():
    for file in [
        file for file in os.listdir(
            os.path.join(
            Config.ROOT_DIR,
            'query')) if file.endswith(".yaml")]:
        with open(os.path.join(Config.ROOT_DIR, 'query', file), encoding='utf8') as stream:
            try:
                QUERY[file] = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


def use_db():
    _db = psycopg2.connect(dbname=Config.DB_NAME,
                           user=Config.DB_USER,
                           password=Config.DB_PASS,
                           host=Config.DB_HOST,
                           port=Config.DB_PORT)

    return _db


def use_p():
    try:
        if request.args:
            p = request.args.to_dict().copy()
        elif request.form:
            p = request.form.copy()
        elif request.get_json():
            p = request.get_json()
        else:
            p = {}
    except Exception:
        p = {}

    return p


def query(conn, sql, params=None):
    with cursor(conn=conn) as cus:
        return cus.query(sql, params)


def query_nofactory(conn, sql, params=None):
    with cursor(conn=conn, cursor_factory=None) as cus:
        return cus.query(sql, params)
