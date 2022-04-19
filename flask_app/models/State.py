from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

dbName = "airlineapi_schema"

class state:
    def __init__(self, data):
        self.abbreviation = data['abbreviation']
        self.name = data['name']
        self.statecol = data['statecol']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
            
    @classmethod
    def get_all(cls, data = None):
        return MySQLConnection(dbName).call_proc('get_states')
