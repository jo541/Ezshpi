from flask import Flask
from . import db
from werkzeug.security import generate_password_hash
import random
import string


def gen_password():
    password = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))
    print password
    return generate_password_hash(password)

class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), default=gen_password)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
