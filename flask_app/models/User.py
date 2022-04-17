from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{3,}$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9#%&!@]{8,}$')
dbName = "workshop_schema"

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.first_name = data['firstname']
        self.last_name = data['lastname']
        self.password = data['password']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO Authors (email, firstname, lastname, password) VALUES (%(email)s, %(firstname)s, %(lastname)s, %(password)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def login(cls,data):
        query = "SELECT * FROM Authors WHERE email = %(email)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def get_Author_by_email(cls,data):
        query = "SELECT * FROM Authors WHERE email = %(email)s;"
        result = MySQLConnection(dbName).query_db( query, data )
        print(result)
        if len(result) <= 0:
            print('get_Author_by_email Returned False')
            return False
        return cls(result[0])

    @classmethod
    def get_Author_by_id(cls,data):
        query = "SELECT * FROM Authors WHERE id = %(Author_id)s;"
        print(f"get_Author_by_id query = {query}")
        result = MySQLConnection(dbName).query_db( query, data )
        if len(result) <= 0:
            print('get_Author_by_id Returned False')
            return False
        return cls(result[0])

    @classmethod
    def get_group_members(cls,data):
        query = "SELECT Authors.* FROM Authors LEFT JOIN GroupMembers "\
                "ON authors.id = GroupMembers.author_id LEFT JOIN WritingGroups ON GroupMembers.Group_id = "\
                "WritingGroups.id WHERE WritingGroups.id = %(id)s;"
        members = []
        results = MySQLConnection(dbName).query_db( query, data )
        for result in results:
            members.append(cls(result))
        return members


    @staticmethod
    def validate(data):
        is_valid = True
        print(f"validate data = {data}")
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!","register")
            is_valid = False
        if not NAME_REGEX.match(data['firstname']):
            flash("First Name is invalid!","register")
            is_valid = False
        if not NAME_REGEX.match(data['lastname']):
            flash("Last Name is invalid!","register")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Password must be 8 valid characters!","register")
            is_valid = False
        if (data['password']!=data['confirm-password']):
            flash("Password entries do not match!","register")
            is_valid = False
        results = Author.get_Author_by_email(data)
        if results != False:
            flash(f"Author email {data['email']} already exists in database!","register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        print(f"login data {data}")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!","login")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Password must be 8 valid characters!","login")
        return is_valid