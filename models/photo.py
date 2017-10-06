from flask import Flask
from . import db


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    base64 = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<User %r>' % self.name