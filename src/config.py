# coding=utf-8
import os


class Config:
    HOST = '127.0.0.1'
    PORT = 5000

    DB_NAME = ''
    DB_USER = ''
    DB_PASS = ''
    DB_HOST = ''
    DB_PORT = ''

    ROOT_DIR = os.getcwd()

    SWAGGER = {
        'uiversion': 2,
    }

    SWAGGER_CONFIG = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'api',
                "route": '/api/api.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/api/static",
        "specs_route": "/api/docs"
    }
