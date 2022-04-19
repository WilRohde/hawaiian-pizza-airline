from os import POSIX_FADV_NOREUSE
from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

dbName = "workshop_schema"

class baseClass():
    pass

    @classmethod
    def get(cls, data = None):
        pass

    @classmethod
    def get_all(cls, data = None):
        pass
    
    @classmethod
    def set(cls, data = None):
        pass

    @classmethod
    def update(cls, data = None):
        pass

    @classmethod
    def delete(cls, data = None):
        pass

    