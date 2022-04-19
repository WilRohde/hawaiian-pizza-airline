from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

dbName = "airlineapi_schema"

class country:
    def __init__(self, data):
        self.code = data['code']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls, data):
        return MySQLConnection(dbName).call_proc('get_countries')
