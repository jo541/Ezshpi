from flask import Flask
from . import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    base_64 = db.Column(db.String(120), unique=True)

    def __init__(self, base_64, name):
        self.name = name
        self.base_64 = base_64

    def __repr__(self):
        return '<User %r>' % self.name