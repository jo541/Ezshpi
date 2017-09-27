from flask import Flask
from . import db
import random
import string

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    code = db.Column(db.String(10), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        if username == "admin":
            self.id = 1
        self.username = username
        self.email = email
        self.code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))

    def __repr__(self):
        return '<User %r>' % self.username

