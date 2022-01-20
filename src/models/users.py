from datetime import datetime
from src import db
from .booking import *
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from src import app
# from flask_bcrypt import Bcrypt


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey("user_role.id"), nullable=False)
    given_name = db.Column(db.String, nullable=False)
    family_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
        
    def __repr__(self):
        return f"User: ( '{self.id}', Role ID: '{self.role_id}'  Name: '{self.given_name}' Family Name: '{self.family_name}' "


class UserRole(db.Model):
    __tablename__ = "user_role"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"User Role: ( '{self.name}' ) "
    
    