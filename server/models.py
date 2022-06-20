from enum import unique
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

def get_uuid():
    return uuid4().hex

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key = True, unique=True, default=get_uuid)
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)